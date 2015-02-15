#!bin/bash

min = 25
echo "Waiting for $min min"
sleep($(($min * 60)))
python unfollow.py
