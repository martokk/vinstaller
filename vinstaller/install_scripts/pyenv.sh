# PyEnv Install Script
# package: pyenv
# about: PyEnv controls and sets the system-wide Python Versions.


# Download and run installer script:
curl -sS https://webi.sh/pyenv | sh

# Add to PATH
echo "export PATH="$HOME/.pyenv/bin:$HOME/.pyenv/shims:$PATH" >> ~/.path
source ~/.path

# Install Python 3.10.8
pyenv install -v 3.10.8

# View installed Python Versions
pyenv versions

# Set Global python to 3.10.8
pyenv global 3.10.8


