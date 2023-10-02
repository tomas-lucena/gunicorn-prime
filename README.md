#!/bin/bash
yum update -y

curl -O https://bootstrap.pypa.io/get-pip.py
sudo yum install gcc openssl-devel bzip2-devel libffi-devel zlib-devel -y 
wget https://www.python.org/ftp/python/3.11.4/Python-3.11.4.tgz 
tar xzf Python-3.11.4.tgz 
cd Python-3.11.4 
sudo ./configure --enable-optimizations 
sudo make altinstall 
sudo rm -f /opt/Python-3.11.4.tgz 

python3.11 get-pip.py --user

wget https://github.com/tomas-lucena/gunicorn-prime/archive/main.zip
unzip main.zip
cd gunicorn-prime-main/

pip3 install -r requirements.txt

gunicorn --workers=2 --bind 0.0.0.0:8000 gunicorn-prime-main/app:app
