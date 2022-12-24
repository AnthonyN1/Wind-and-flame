#!/bin/sh

# Pulls any updates from the remote repository.
echo "W&F: Pulling from repository..."
git pull

# If a virtual environment doesn't exist, creates one.
if [ ! -d ".venv" ]; then
	echo "W&F: Creating virtual environment..."
	python3 -m venv .venv
fi

# Activates the virtual environment.
echo "W&F: Activating virtual environment..."
source .venv/bin/activate

# Installs required Python packages.
echo "W&F: Installing packages..."
pip3 install -r requirements.txt | grep -v "already satisfied"

