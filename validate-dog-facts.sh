#!/bin/bash
if [[ $(ps aux | grep '[p]ython3 -u /discord-bot/dog-facts/dog-facts.py' | wc -l) != 0 ]]
then
    exit[0]
else
    exit[1]
fi