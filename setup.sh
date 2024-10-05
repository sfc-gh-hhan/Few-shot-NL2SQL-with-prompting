#!/bin/bash

#wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
#chmod +x Miniconda3-latest-Linux-x86_64.sh
#./Miniconda3-latest-Linux-x86_64.sh -b
#conda install conda-forge::conda-ecosystem-user-package-isolation
# Restart the kernel

eval "$(conda shell.bash hook)"

conda create --name sql python=3.9
conda activate sql

pip install -r requirements.txt

wget https://bird-bench.oss-cn-beijing.aliyuncs.com/dev.zip
unzip dev.zip
rm dev.zip
cd dev_20240627/
unzip dev_databases.zip
rm dev_databases.zip
cd ..
mv dev_20240627 dev

pip install langchain
pip install -U langchain-community
pip install --upgrade --quiet  langchain-openai
