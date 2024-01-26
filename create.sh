#!/bin/bash
msg=$1
name=$(pwd)
if [ "$2" = "-l" ];then
    python3 ~/Documents/Programming/Python\ Projects/automation/localrepo.py "$msg" 
else
    python3 ~/Documents/Programming/Python\ Projects/automation/newrepo.py "$msg" "$name"
fi