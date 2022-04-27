import os
import subprocess

project_slug = "{{ cookiecutter.project_slug }}"
project_packages = '{{ cookiecutter.project_packages }}'

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")

# Creating a virtual environment for Scripts
if project_packages == 'Script':
    subprocess.call(['pip', 'install', '-r', 'requirements.txt'])
# Creating a virtual environment for Notebooks
if project_packages == 'Notebook':
    subprocess.call(['conda', 'create', '-n', project_slug])
    subprocess.call(['mamba','env','update','-n', project_slug,'-f','environment.yml'])
    subprocess.call(['ipython','kernel', 'install', '--user', '--name', project_slug])

# Initializing git repository
print(f"Initializing a git repository...{RESET_ALL}")
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")