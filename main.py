import subprocess
from tkinter import filedialog
import sys
from spotdl import __main__ as spotdl
while True:
    while True:
        try:
            spotifylink = input("Insert a Spotify link:\n>> ")
            if "https://open.spotify.com" not in spotifylink:
                print("Invalid link.")
                continue
        except:
            continue
        break
    while True: 
        directory = filedialog.askdirectory()
        if directory:
            subprocess.check_call([sys.executable, spotdl.__file__, spotifylink, '--output', directory])
            break
        else:
            print("Please select a folder.")
            continue
    while True:
        next = input("Continue? y/n\n>> ")
        if next == "y":
            break
        if next == "n":
            quit()
        else:
            print("Invalid input.")
            continue
    continue