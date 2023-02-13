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
    bath()

    console.print(Panel('[bold]Welcome to [default on red]onsen[/]![/] ([italic]tattoo-friendly)[/]', expand=True))
    console.print('[italic]May I help you? (いらっしゃいませ)[/] type [default on red]help[/]')
    while True:
        command = console.input(":hotsprings:  [bold red]>[/] ").strip().lower()
       
        if command == 'bath':
            console.print('[blue]Relax...')
            bath()
        if "volume" in command:
            if len(command.split()) > 1 and command.split()[0] == "volume" and command.split()[1].isdigit(): 
                value = int(command.split()[1])
            else:
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
    global channel3
    global console
    global help_commands

    mixer.init()
    channel1 = mixer.Channel(0)
    channel2 = mixer.Channel(1)
    channel3 = mixer.Channel(2)
    channel2.set_volume(0.25)
    channel3.set_volume(0.25)
    
    console = Console()
    help_commands = """[default on red]bath[/] - take a bath in our hot springs :umbrella: 
[default on red]volume[/] - turn down [strike]for what[/] :arrow_up_down:
[default on red]stop[/] - shut [bold]everything[/] up :speaker:
[default on red]quit[/] - I [italic]think[/] you know what this does :x:"""

def bath():
    current_path = Path(__file__).parent.absolute()
    water = mixer.Sound(str(current_path) + '/assets/water.wav')
    bell = mixer.Sound(str(current_path) + '/assets/bell.wav')
    channel1.play(water, loops = -1)
    channel3.play(bell)

def stop():
    channel1.stop()
    current_path = Path(__file__).parent.absolute()
    bell = mixer.Sound(str(current_path) + '/assets/bell.wav')
    channel3.play(bell)

def set_volume(value):
    console.print('[blue]setting volume to ' + str(value) + '...')
    channel1.set_volume(value / 100)

def welcome():
    current_path = Path(__file__).parent.absolute()
    welcome_sound = mixer.Sound(str(current_path) + '/assets/welcome.wav')
    channel2.play(welcome_sound)

## handle CTRL + C
def signal_handler(signal, frame):
    print()
    console.print('[italic]Come back soon![/] (ありがとうございました)')
    sys.exit(0)

if __name__ == '__main__':
    main()
