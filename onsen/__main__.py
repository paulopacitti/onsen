import sys
import os
import signal
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt

# Disable print
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Enable print
def enablePrint():
    sys.stdout = sys.__stdout__

blockPrint()
import pygame.mixer as mixer
enablePrint()

def main():
    signal.signal(signal.SIGINT, signal_handler)
    init()
    cli()

def cli():
    console.clear()
    welcome()
    rain()

    console.print(Panel('[bold]Welcome to [default on red]onsen[/]![/] ([italic]tattoo-friendly)[/]', expand=True))
    console.print('[italic]May I help you? (いらっしゃいませ)[/] type [default on red]help[/]')
    while True:
        command = console.input(":hotsprings:  [bold red]>[/] ")
       
        if command == 'bath':
            console.print('[blue]Relax...')
            rain()
        if command == 'volume':
            value = IntPrompt.ask(':cloud_with_rain:  [bold blue]How much water do you want? (1 to 100)[/]')
            set_volume(value)
        if command == 'help':
            console.print(help_commands)
        if command == 'stop':
            stop()
        if command == 'quit':
            console.print('[italic]Come back soon![/] (ありがとうございました)')
            break
        
    return

def init():
    global channel1
    global channel2
    global console
    global help_commands

    mixer.init()
    channel1 = mixer.Channel(0)
    channel2 = mixer.Channel(1)
    console = Console()
    help_commands = """[default on red]bath[/] - take a bath in our hot springs :umbrella: 
[default on red]volume[/] - turn down [strike]for what[/] :arrow_up_down:
[default on red]stop[/] - shut [bold]everything[/] up :speaker:
[default on red]quit[/] - I [italic]think[/] you know what this does :x:"""

def rain():
    current_path = Path(__file__).parent.absolute()
    rain = mixer.Sound(str(current_path) + '/assets/water.wav')
    channel1.play(rain, loops = -1)

def stop():
    channel1.stop()

def set_volume(value):
    console.print('[blue]setting volume to ' + str(value) + '...')
    channel1.set_volume(value / 100)

# sounds have to be .wav
# def welcome():
#     current_path = Path(__file__).parent.absolute()
#     welcome_sound = mixer.Sound(str(current_path) + '/assets/welcome.mp3')
#     channel1.play(welcome_sound)

## handle CTRL + C
def signal_handler(signal, frame):
    print()
    console.print('[italic]Come back soon![/] (ありがとうございました)')
    sys.exit(0)

if __name__ == '__main__':
    main()