#!/usr/bin/bash

# Check if /usr/bin/code already exists
if [ -e /usr/bin/code ]; then
    echo "'/urs/bin/code already exists. Delete before trying to reinstall."
    exit 1
fi

# Install dependencies
sudo apt-get install wget gpg apt-transport-https -y

# Download & install the apt repository and signing key
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
rm -f packages.microsoft.gpg

# Then update the package cache and install the package using:
sudo apt install
sudo apt update
sudo apt install code -y # or code-insiders
