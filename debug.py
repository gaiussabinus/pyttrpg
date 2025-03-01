#!/usr/bin/env python3

import os

def launch_terminal():
    os.system("gnome-terminal -e 'bash -c \"python3 main.py\"'")

if __name__ == "__main__":
    launch_terminal()
