import os
import subprocess

# Clear terminal
os.system('clear')

# Set Banner
subprocess.call('figlet -f slant "Kali Linux" | lolcat', shell=True)

# Display system info
subprocess.call('neofetch', shell=True)

# Custom Prompt (simulated as a message, since PS1 is not configurable in Python directly)
print("\033[1;34m\n╭──────(\033[1;31m Root@Kali \033[1;34m)-[\033[1;32m \w \033[1;34m]\n╰────\033[1;36m$ \033[0m")

# Display ASCII art
subprocess.call('figlet -f small "MatrixMan"', shell=True)
