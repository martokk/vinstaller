#!/usr/bin/bash

# Check if /media/martokk/FILES exists
if [ -d /media/martokk/FILES ]; then
    echo "/media/martokk/FILES was found. Creating symlinks..."

    # HOME FOLDERS
    SOURCE=/media/martokk/FILES/
    ln -sfv "$SOURCE/__INBOX__" "$HOME/__INBOX__"
    ln -sfv "$SOURCE/Audio" "$HOME/Audio"
    ln -sfv "$SOURCE/dev" "$HOME/dev"
    ln -sfv "$SOURCE/Downloads" "$HOME/Downloads"
    ln -sfv "$SOURCE/Games" "$HOME/Games"
    ln -sfv "$SOURCE/Movies" "$HOME/Movies"
    ln -sfv "$SOURCE/Music" "$HOME/Music"
    ln -sfv "$SOURCE/Notes" "$HOME/Notes"
    ln -sfv "$SOURCE/Pictures" "$HOME/Pictures"
    ln -sfv "$SOURCE/Shows" "$HOME/Shows"
    ln -sfv "$SOURCE/Videos" "$HOME/Videos"
    ln -sfv "$SOURCE/TV Shows" "$HOME/TV Shows"

    # FILES/bin -> ~/bin
    ln -sfv "$SOURCE/bin" "$HOME/bin"

    exit 1
fi
