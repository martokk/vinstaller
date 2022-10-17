#!/usr/bin/bash

# Download to /usr/local/bin
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp

# Make Executable
sudo chmod a+rx /usr/local/bin/yt-dlp
