#!/bin/bash

source /config/shell_commands/secrets.sh

/usr/bin/ssh osmc@"$KODI_IP" pkill kodi.bin

