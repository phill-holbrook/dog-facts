#!/bin/bash
if [[ $(ps aux | grep '[p]ython3 -u /discord-bot/dog-facts/dog-facts.py' | wc -l) != 0 ]]
then
    return 0
else
    return 1
fi