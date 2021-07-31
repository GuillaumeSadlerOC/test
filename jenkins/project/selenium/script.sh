#!/bin/bash

python3 -m venv env
source env/bin/activate
pip install selenium

# GeckoDriver v0.29.1
wget -q "https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz" -O /tmp/geckodriver.tgz \
    && tar zxf /tmp/geckodriver.tgz -C /usr/bin/ \
    && rm /tmp/geckodriver.tgz

python3 script.py