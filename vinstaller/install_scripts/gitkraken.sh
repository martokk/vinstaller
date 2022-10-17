#!/usr/bin/bash

# Dowload .deb
wget https://release.gitkraken.com/linux/gitkraken-amd64.deb /tmp

# Install
sudo apt install /tmp/gitkraken-amd64.deb -y
