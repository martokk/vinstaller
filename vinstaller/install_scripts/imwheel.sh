#!/usr/bin/bash

# Install
sudo apt install imwheel


# Create ~/.imwheelrc config if doesn't exist:
FILE="$HOME/.imwheelrc"
if [[ ! -f "$FILE" ]]; then
    echo "Creating ~/.imwheelrc"
    echo $'".*"\nNone,      Up,   Button4, 10\nNone,      Down, Button5, 10\nControl_L, Up,   Control_L|Button4\nControl_L, Down, Control_L|Button5\nShift_L,   Up,   Shift_L|Button4\nShift_L,   Down, Shift_L|Button5' > "$FILE"
fi


# Add to Autostart
echo "Add to Autostart"
echo $'[Desktop Entry]\nExec=/usr/bin/imwheel\nName[en_US]=imwheel\nName=imwheel\nStartupNotify=true\nTerminal=false\nType=Application\nX-KDE-SubstituteUID=false" > "$HOME/.config/autostart/imwheel.desktop" && sudo chmod +x "$HOME/.config/autostart/imwheel.desktop'


# Run imwheel
echo "Starting imwheel"
imwheel
