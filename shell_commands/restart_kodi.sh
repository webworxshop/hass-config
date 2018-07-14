#!/bin/bash

source /home/homeassistant/.homeassistant/shell_commands/secrets.sh

/usr/bin/ssh osmc@$KODI_IP pkill kodi.bin

