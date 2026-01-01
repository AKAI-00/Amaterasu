import os
from rich.console import Console
from rich.panel import Panel

console = Console()

def banner():
    os.system("clear")

    ascii_art = r"""
 █████╗ ███╗   ███╗ █████╗ ████████╗███████╗██████╗  █████╗ ███████╗██╗   ██╗
██╔══██╗████╗ ████║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║   ██║
███████║██╔████╔██║███████║   ██║   █████╗  ██████╔╝███████║███████╗██║   ██║
██╔══██║██║╚██╔╝██║██╔══██║   ██║   ██╔══╝  ██╔══██╗██╔══██║╚════██║██║   ██║
██║  ██║██║ ╚═╝ ██║██║  ██║   ██║   ███████╗██║  ██║██║  ██║███████║╚██████╔╝
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝
    """

    console.print(
        Panel.fit(
            f"[bold red]{ascii_art}[/bold red]\n"
            "[bold cyan]CLI Red Team C2 Framework[/bold cyan]\n"
            "[green]Status:[/green] LISTENING",
            border_style="red"
        )
    )