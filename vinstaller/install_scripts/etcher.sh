# Debian and Ubuntu based Package Repository (GNU/Linux x86/x64)

# Add Etcher debian repository:
echo "deb https://deb.etcher.io stable etcher" | sudo tee /etc/apt/sources.list.d/balena-etcher.list

# Trust Bintray.com’s GPG key:
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 379CE192D401AB61

# Update and install:
sudo apt-get update
sudo apt-get install balena-etcher-electron -y

# Uninstall
#sudo apt-get remove balena-etcher-electron
#sudo rm /etc/apt/sources.list.d/balena-etcher.list
#sudo apt-get update
