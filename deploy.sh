#!/bin/bash

#108.171.163.140
#testIm5ScA23i

host="${1}"

if [ -z "$host" ]; then
    echo "Usage: ./deploy.sh [user@host]"
    exit
fi

tar cz . | ssh -o 'StrictHostKeyChecking no' "$host" "
rm -rf ~/app &&
mkdir ~/app &&
cd ~/app &&
tar xz"