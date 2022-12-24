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
pip3 install -U -r requirements.txt | grep -v "already up-to-date"

# Checks for a .env file.
if [ ! -f ".env" ]; then
	echo "Missing .env file with a TOKEN variable."
	exit 1
fi

# If a log directory doesn't exist, creates one.
if [ ! -d "logs" ]; then
	echo "W&F: Creating logs directory..."
	mkdir logs
fi

# Runs the Discord bot.
echo "W&F: Running bot..."
python3 src/main.py > logs/process.log 2>&1

