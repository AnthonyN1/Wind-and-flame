#!/bin/sh

# Pulls any updates from the remote repository.
printf "W&F: Pulling from repository...\n"
git pull
printf "==================================================\n\n"

# If a virtual environment doesn't exist, creates one.
if [ ! -d ".venv" ]; then
	printf "W&F: Creating virtual environment...\n"
	python3 -m venv .venv
	printf "==================================================\n\n"
fi

# Activates the virtual environment.
printf "W&F: Activating virtual environment...\n"
source .venv/bin/activate
printf "==================================================\n\n"

# Installs required Python packages.
printf "W&F: Installing packages...\n"
pip3 install -r requirements.txt | grep -v "already satisfied"
printf "==================================================\n"
