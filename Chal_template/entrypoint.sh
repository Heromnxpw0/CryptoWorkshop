#!/bin/bash

echo $FLAG > /app/flag.txt
./ynetd -p 1337 "python3 ./play.py"