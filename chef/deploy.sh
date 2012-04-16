#!/bin/bash

#108.171.163.140
#testIm5ScA23i

host="${1}"
json="${2}"

if [ -z "$host" ] || [ -z "$json" ]; then
    echo "Usage: ./deploy.sh [user@host] [json]"
    exit
fi

tar cz . | ssh -o 'StrictHostKeyChecking no' "$host" "
rm -rf ~/chef &&
mkdir ~/chef &&
cd ~/chef &&
tar xz &&
bash install.sh $json"