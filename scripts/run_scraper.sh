#!/bin/bash

#se mueve a la carpeta anterior donde esta localizado main.py
cd "$(dirname "$0")/.." || exit 1

.venv/bin/python main.py >> scraper.log 2>&1git 