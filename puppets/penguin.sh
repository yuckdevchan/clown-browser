#!/bin/bash
# Linux Install Script
git clone https://github.com/yuckdevchan/clown-browser
cd clown-browser
pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
python3 main.py
