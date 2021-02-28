#!/bin/bash
pwd
cd kick-off
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
cd service-1
python3 -m pytest --cov application
python3 -m pytest --cov application
cd ../service-2
python3 -m pytest --cov application
cd ../service-3
python3 -m pytest --cov application
cd ../service-4
python3 -m pytest --cov application
cd ..
deactivate
