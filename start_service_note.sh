#!/bin/bash
source ../heat-env/bin/activate
sudo pigpiod
export PYTHONPATH=/home/jackvlg/so2heat
python village/so2heat_app_service.py https://192.168.8.107:8443
