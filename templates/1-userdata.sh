#!/bin/sh
yum update -y
yum install -y git python3
git clone https://github.com/MarkBiesheuvel/demo-speed-agility.git
cd demo-speed-agility/source/
python3 -m pip install -r requirements.txt
gunicorn -w 4 app:app -b 0.0.0.0:80
