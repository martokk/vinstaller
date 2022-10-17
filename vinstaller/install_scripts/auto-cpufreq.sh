#!/bin/bash

# Install if command does not exist
COMMAND='auto-cpufreq'

if ! command -v "$COMMAND" &> /dev/null
then
    echo "Installing '$COMMAND'..."

    # Pull & Run Installer Script
    git clone https://github.com/AdnanHodzic/auto-cpufreq.git /tmp/auto-cpufreq
    sudo /tmp/auto-cpufreq/auto-cpufreq-installer --install

    # Link /etc/auto-cpufreq.conf to ~/auto-cpufreq.conf dotfile.
    touch ~/auto-cpufreq.conf
    sudo ln -s ~/auto-cpufreq.conf /etc/auto-cpufreq.conf

    # Run as Daemon
    sudo auto-cpufreq --install

    # Cleanup
    sudo rm -rf /tmp/auto-cpufreq
else
    echo "'$COMMAND' is already installed. Skipping."
fi
