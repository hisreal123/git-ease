#!/usr/bin/python3
import subprocess

initializer = __import__('initializer').git_initializer
push_command = __import__('push_command').push_command


def had_commit():
    try:
        subprocess.run(['git', 'log'], check=True, capture_output=True)
        push_command()

    except:
        initializer()
