#!/bin/bash
yum update -y

curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user

wget https://github.com/tomas-lucena/gunicorn-prime/archive/main.zip
unzip main.zip
cd gunicorn-prime-main/
pip3 install -r requirements.txt

gunicorn --workers=2 --bind 0.0.0.0:8000 gunicorn-prime-main/app:app
