#!/usr/bin/bash

# Dowload .deb
wget https://release.gitkraken.com/linux/gitkraken-amd64.deb -P "$HOME/Downloads"

# Install
sudo apt install "$HOME/Downloads/gitkraken-amd64.deb" -y
