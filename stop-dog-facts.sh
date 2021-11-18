#!/bin/bash
kill $(ps aux | grep '[p]ython3 -u /discord-bot/dog-facts/dog-facts.py' | awk '{print $2}')