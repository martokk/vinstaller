#!/usr/bin/bash

# Download & Install via Python3
curl -sSL https://install.python-poetry.org | python3 -

# Change so venv folder in within the project:
poetry config virtualenvs.in-project true
