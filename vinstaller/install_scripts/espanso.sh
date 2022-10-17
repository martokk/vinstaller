
# Download latest release
cd /home/martokk/Downloads
curl -s https://api.github.com/repos/espanso/espanso/releases/latest | grep "espanso-debian-x11-amd64.deb" | cut -d : -f 2,3 | tr -d \" | wget -qi -

# Install
sudo apt install /home/martokk/Downloads/espanso-debian-x11-amd64.deb -y

# Cleanup
sudo rm -rf /home/martokk/Downloads/espanso-debian-x11-amd64.deb

# Register espanso as a systemd service (required only once)
sleep 2
espanso service register
sleep 1

# Start espanso
espanso start
espanso status

