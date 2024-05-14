#!/bin/bash
sudo docker rm -f galaga
sudo docker rmi -f galaga
sudo docker build -t galaga .

