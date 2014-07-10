#!/bin/sh
DATE=`date +%F`
MANAGE=django-admin.py
PROJECT=fortytwo_test_task
COMMAND=showmodels
PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=${PROJECT}.settings ${MANAGE} ${COMMAND} --error 2> ./$DATE.dat