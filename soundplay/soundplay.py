#!/usr/bin/env python

import subprocess

def play(path):
    command = ["mpg123", path]
    subprocess.call(command)

