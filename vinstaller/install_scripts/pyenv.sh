# PyEnv Install Script
# package: pyenv
# about: PyEnv controls and sets the system-wide Python Versions.


# Install Dependencies to build
sudo apt update
sudo apt install make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev


# Download & Run Installer
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

exec $SHELL


#
# # Download and run installer script:
# curl -sS https://webi.sh/pyenv | sh
#
# # Add to PATH
# echo "export PATH=$HOME/.pyenv/bin:$HOME/.pyenv/shims:$PATH" >>~/.path
# source "$HOME/.path"
#
# echo 'export PYENV_ROOT="$HOME/.pyenv"' >>"$HOME/.bashrc"
# echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >>~/.bashrc
# echo 'eval "$(pyenv init -)"' >>~/.bashrc
#
# echo 'export PYENV_ROOT="$HOME/.pyenv"' >>~/.zshrc
# echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >>~/.zshrc
# echo 'eval "$(pyenv init -)"' >>~/.zshrc

# Install Python 3.10.8
pyenv install -v 3.10.8

# View installed Python Versions
pyenv versions

# Set Global python to 3.10.8
pyenv global 3.10.8
