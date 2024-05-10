#!/usr/bin/env bash

CONFIG=$1
GPUS=$2
PORT=${PORT:-28500}

PYTHONPATH="$(dirname $0)/..":$PYTHONPATH \
python -m torch.distributed.launch --nproc_per_node=$GPUS --master_port=$PORT \
    $(dirname "$0")/train.py $CONFIG --resume-from "/home/gofuuu/BEVFormer_1_linear/work_dirs/bevformer_tiny/latest.pth" --launcher pytorch ${@:3} --deterministic
