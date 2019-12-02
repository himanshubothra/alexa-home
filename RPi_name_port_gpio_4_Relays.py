 
import fauxmo
import logging
import time
import sys
import RPi.GPIO as GPIO ## Import GPIO library
 
from debounce_handler import debounce_handler
 
logging.basicConfig(level=logging.DEBUG)
 
class device_handler(debounce_handler):
    """Publishes the on/off state requested,
       and the IP address of the Echo making the request.
    """
    #TRIGGERS = {str(sys.argv[1]): int(sys.argv[2])}
    #TRIGGERS = {"room": 52000}
    TRIGGERS = {"light one": 52000, "light two": 51000, "light three": 53000, "fan": 52002}

    def act(self, client_address, state, name):
        print("State", state, "from client @", client_address)
        

        if name=="light one":
            GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
            GPIO.setup(int(7), GPIO.OUT)   ## Setup Physical Pin to not gpio pin
            GPIO.output(int(7), state) ## State is true/false
        elif name =="light two":
            GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
            GPIO.setup(int(11), GPIO.OUT)   ## Setup Physical Pin to not gpio pin
            GPIO.output(int(11), state) ## State is true/false
        elif name =="light three":
            GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
            GPIO.setup(int(13), GPIO.OUT)   ## Setup Physical Pin to not gpio pin
            GPIO.output(int(13), state) ## State is true/false
        elif name == "fan":
            GPIO.setmode(GPIO.BOARD)  ## Use board pin numbering
            GPIO.setup(int(5), GPIO.OUT)  ## Setup Physical Pin to not gpio pin
            GPIO.output(int(5), state)  ## State is true/false
        else:
            print("Device not found!")




        return True
 
if __name__ == "__main__":
    # Startup the fauxmo server
    fauxmo.DEBUG = True
    p = fauxmo.poller()
    u = fauxmo.upnp_broadcast_responder()
    u.init_socket()
    p.add(u)     # Add the UPnP broadcast listener to the poller so we can respond when a broadcast is received.
 
    # Register the device callback as a fauxmo handler
    d = device_handler()
    for trig, port in d.TRIGGERS.items():
        fauxmo.fauxmo(trig, u, p, None, port, d)
 
    # Loop and poll for incoming Echo requests
    logging.debug("Entering fauxmo polling loop")
    while True:
        try:
            # Allow time for a ctrl-c to stop the process
            p.poll(100)
            time.sleep(0.1)
        except Exception as e:
            logging.critical("Critical exception: "+ e.args  )
            break
