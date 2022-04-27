import os
import subprocess

project_slug = "{{ cookiecutter.project_slug }}"

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")

# Creating a virtual environment for Scripts
if '{{ cookiecutter.project_packages }}' == 'Script':
    subprocess.call(['pip', 'install', '-r', 'requirements.txt'])
# Creating a virtual environment for Notebooks
if '{{ cookiecutter.project_packages }}' == 'Notebook':
    subprocess.call(['conda', 'env', 'create','--file','environment.yml'])
    subprocess.call(['ipython','kernel', 'install', '--user', '--name', project_slug])

# Initializing git repository
print(f"Initializing a git repository...{RESET_ALL}")
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")