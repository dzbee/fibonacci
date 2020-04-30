#!/bin/bash

find . -iname "*~" | xargs -r rm
find . | grep .py[co] | xargs -r rm -rf
if [[ -d venv ]]; then rm -rf venv; fi

# TODO: maybe remove __pycache__ directories
