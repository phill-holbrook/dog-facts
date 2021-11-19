#!/bin/bash
if [[ $(ps aux | grep '[p]ython3 -u /discord-bot/dog-facts/dog-facts.py' | wc -l) != 0 ]]
then
    kill $(ps aux | grep '[p]ython3 -u /discord-bot/dog-facts/dog-facts.py' | awk '{print $2}')
else
    exit 0
fi