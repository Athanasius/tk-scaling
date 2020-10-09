#!/bin/sh

export PYTHONUNBUFFERED=1
python small-ui.py 50 &
python small-ui.py 100 &
python small-ui.py 200 &
