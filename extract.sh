#!/bin/bash

echo "List All Available Files : "

az storage blob list \
    --account-name ethans1124etl \
    --container-name input \
    --auth-mode login \
    --output table

echo "Download employee.csv to local"

az storage blob download \
    --account-name ethans1124etl \
    --container-name input \
    --name employee.csv \
    --file /home/azureuser/ethans-1124/input/employee.csv \
    --auth-mode login

echo "File Downloaded Successfully..."

exit 0

