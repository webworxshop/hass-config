#!/srv/homeassistant/bin/python3.6

from pychromecast import Chromecast
import sys

CAST_IP = "10.0.0.120"

if __name__ == "__main__":

	cast = Chromecast(CAST_IP)
	cast.reboot()

