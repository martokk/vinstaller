
# Download latest release
cd "$HOME/Downloads"
curl -s https://api.github.com/repos/espanso/espanso/releases/latest | grep "espanso-debian-x11-amd64.deb" | cut -d : -f 2,3 | tr -d \" | wget -qi -

# Install
sudo apt install "$HOME/Downloads/espanso-debian-x11-amd64.deb" -y

# Cleanup
sudo rm -rf "$HOME/Downloads/espanso-debian-x11-amd64.deb"

# Register espanso as a systemd service (required only once)
sleep 2
espanso service register
sleep 1

# Start espanso
espanso start
espanso status
