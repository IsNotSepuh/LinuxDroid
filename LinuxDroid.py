import os
import sys
import subprocess

# Set Banner
os.system('clear')
os.system('figlet -f slant "Kali Linux" | lolcat')

# Info System
subprocess.run(['neofetch'])

# Customize Terminal Prompt (this is specific to bash, but you can modify .bashrc if needed for permanence)
os.environ['PS1'] = "\n╭──────( Root@Kali )-[ \w ]\n╰────$ "

# Print Custom Message
os.system('echo -e "\n\033[1;35m" + $(figlet -f small "MatrixMan") + "\033[0m"')
