#!/bin/bash
git clone git@github.com:vradicevic/CI_CD_pipeline.git
cd CI_CD_pipeline

python3 -m venv ~/.repo
source ~/.repo/bin/activate

az webapp up -n myflaskapplication -l westeurope --sku B1

az webapp log tail