import rich

from googletrans import Translator
from rich.console import Console

console = Console()
translator = Translator()

console.print(
    "[bold magenta]Google Translate[/]\n",
    "[bold white]Channel: https://t.me/termuxtop[/]",
    
    justify="center",
    sep="\n"
)

console.print("\n[bold blue]Language code", justify="center")

language = console.input("[bold red]Enter code[/]: ")
text = console.input("[bold yellow]Enter what you want, translated[/]: ")

with console.status("[bold green]Translation[/]"):
     translation = translator.translate(text, dest=language)

console.print(
    "\n[bold green]Translated[/]: {translation}"
    .format(translation=translation.text),
    
    justify="center"
)
