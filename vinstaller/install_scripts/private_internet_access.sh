DL_WEBPAGE=https://www.privateinternetaccess.com/download/linux-vpn

# Get Download URL from website
echo "Getting url from download webpage: $DL_WEBPAGE"
DL_URL_BASE=https://installers.privateinternetaccess.com/download
DL_URL=$(curl -s $DL_WEBPAGE | grep -m1 -oE "$DL_URL_BASE/pia-linux[0-9.-]+.run")
FILE_NAME=${DL_URL##*/}

echo "Downloading Private Internet Access for Linux 64bit : $DL_URL"
echo "Downloading Private Internet Access for Linux 64bit : $DL_URL"

# Download install files from URL
sudo -H -u "$(logname)" curl -RL  -o /tmp/pia-linux.run $DL_URL
if [ -f /tmp/pia-linux.run ]; then
  echo "[ OK ] downloaded '$FLN'"
else
  echo "[ ERROR ] Download of '$FLN' failed file "
  exit 1
fi

# Install downloaded file
echo ""
echo "Installing '/tmp/pia-linux.run'..."
chmod 755 /tmp/pia-linux.run
bash /tmp/pia-linux.run
