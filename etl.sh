#!/bin/bash

if [ $# -ne 1 ];then
	echo "Invalid Numner of Arguments : [1.ActionType : [transform|load]]"
	exit 1
fi

action_type=$1

python3 -m venv etl-env
source etl-env/bin/activate

pip install -r /home/azureuser/ethans-1124/requirements.txt

if [ $action_type == "transform" ];then
	python3 /home/azureuser/ethans-1124/transform.py
elif [ $action_type == "load" ];then
	python3 /home/azureuser/ethans-1124/load.py
else
	echo "Invalid Action Type..."
fi


exit 0
