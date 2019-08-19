#!/bin/bash

source /config/shell_commands/secrets.sh

/config/shell_commands/broadlink_cli --type 0x2737 --host "$BROADLINK_IP" --mac "$BROADLINK_MAC" --send "$1"
