#!/bin/bash

# Relies on pyenv to do the virtual environment setup.

# Install dependencies
sudo apt-get install build-essential libpoppler-cpp-dev pkg-config

# Create virtual environment
pyenv local pypy
pyenv virtualenv scrapy
pyenv local scrapy

# Fetch necessary packages
pip3 install pdftotext
