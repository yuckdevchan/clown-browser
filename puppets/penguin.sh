#!/bin/bash
# Linux Install Script
git clone https://github.com/yuckdevchan/clown-browser
cd clown-browser
pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
cd ..
mv clown-browser ~/.local/bin/clown-browser
chmod +x ~/.local/bin/clown-browser/puppets/clown-browser
mv ~/.local/bin/clown-browser/puppets/clown-browser ~/.local/bin/clown-browser
cp ~/.local/bin/clown-browser/puppets/clown-browser /usr/bin/clown-browser
