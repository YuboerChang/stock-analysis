#!/bin/bash
rm_type=$1

if [ -z "$rm_type" ];then
    rm -rf ../data/*
elif [ "$rm_type" = "b" ];then
    rm -rf ../data/block/*
elif [ "$rm_type" = "s" ];then
    rm -rf ../data/stock/*
else
    echo "parameter wrong"
    sleep 3
fi
