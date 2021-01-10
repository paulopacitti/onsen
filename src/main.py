import sys, os, signal
# Disable print
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Enable print
def enablePrint():
    sys.stdout = sys.__stdout__

blockPrint()
import pygame.mixer as mixer
enablePrint()

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import IntPrompt

def init():
    global channel1
    global console
    global manual

    mixer.init()
    channel1 = mixer.Channel(0)
    console = Console()
    
    with open("assets/manual.md") as raw:
        manual = Markdown(raw.read())

def main():
    console.clear()
    rain()

    console.print(Panel("Welcome to the [red]Onsen!", expand=True))
    console.print(manual)
    while True:
        command = console.input(":hotsprings:  [bold red]>[/] ")
        if command == 'quit':
            break
        if command == 'rain':
            console.print("[blue]Pouring rain...")
            rain()
        if command == 'stop':
            stop()
        if command == 'volume':
            value = IntPrompt.ask(":cloud_with_rain:  [bold blue]How much water do you want? (1 to 100)[/]")
            set_volume(value)
    return

def rain():
    rain = mixer.Sound('assets/rain.wav')
    channel1.play(rain, loops = -1)

def stop():
    channel1.stop()

def set_volume(value):
    console.print("[blue]setting volume to " + str(value) + "...")
    channel1.set_volume(value / 100)

## handle CTRL + C
def signal_handler(signal, frame):
    print()
    sys.exit(0)

init()
main()
signal.signal(signal.SIGINT, signal_handler)