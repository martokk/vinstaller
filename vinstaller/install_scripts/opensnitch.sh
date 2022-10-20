#!/usr/bin/bash
DOWNLOAD_FOLDER="$HOME/Downloads"
DOWNLOAD_FILENAME_DAEMON="opensnitch.*amd64.deb"
DOWNLOAD_FILENAME_UI="python3-opensnitch*"
DOWNLOAD_REPO="https://api.github.com/repos/evilsocket/opensnitch"


# Get Filename & Download Link for Daemon
RESPONSE_DAEMON=`curl -s "$DOWNLOAD_REPO/releases/latest" | awk -F\" '/opensnitch.*amd64.deb/{print $(NF-1)}'`

ACTUAL_FILENAME_DAEMON=`echo "$RESPONSE_DAEMON" | sed -n '1 p'`
# echo "ACTUAL_FILENAME_DAEMON=$ACTUAL_FILENAME_DAEMON"

ACTUAL_DOWNLOAD_DAEMON=`echo "$RESPONSE_DAEMON" | sed -n '2 p'`
# echo "ACTUAL_DOWNLOAD_DAEMON=$ACTUAL_DOWNLOAD_DAEMON"

# Download Daemon
wget "$ACTUAL_DOWNLOAD_DAEMON" -P "$DOWNLOAD_FOLDER"



# Get Filename & Download Link for UI
RESPONSE_UI=`curl -s "$DOWNLOAD_REPO/releases/latest" | awk -F\" '/python3-opensnitch*/{print $(NF-1)}'`

ACTUAL_FILENAME_UI=`echo "$RESPONSE_UI" | sed -n '1 p'`
# echo "ACTUAL_FILENAME_UI=$ACTUAL_FILENAME_UI"

ACTUAL_DOWNLOAD_UI=`echo "$RESPONSE_UI" | sed -n '2 p'`
# echo "ACTUAL_DOWNLOAD_UI=$ACTUAL_DOWNLOAD_UI"

# Download UI
wget "$ACTUAL_DOWNLOAD_UI" -P "$DOWNLOAD_FOLDER"






# Install
sudo apt install "$DOWNLOAD_FOLDER/$ACTUAL_FILENAME_DAEMON" "$DOWNLOAD_FOLDER/$ACTUAL_FILENAME_UI" -y

# Cleanup
sudo rm -rf "$DOWNLOAD_FOLDER/$ACTUAL_FILENAME_DAEMON"
sudo rm -rf "$DOWNLOAD_FOLDER/$ACTUAL_FILENAME_UI"

# Enable & Start Daemon
sudo systemctl enable opensnitch
sudo systemctl start opensnitch

