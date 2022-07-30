################################
from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
import time
import socket
#import exceptions
import math
import argparse
##########  FUNCTIONS  ###################
def connectMyCopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()

    connection_string = args.connect
    baud_rate = 57600

    vehicle = connect(connection_string,baud=baud_rate,wait_ready=True)
    return vehicle

def arm():
    '''    
    while vehicle.is_armable==False:
        print("Waiting for vehicle to become armable")
        time.sleep(1)
    print("Yoooo vehicle is now armable")
    print("")
    '''
    vehicle.armed=True
    while vehicle.armed==False:
        print("Waiting for drone to be armed..")
        time.sleep(1)

    print("Vehicle is now armed..")
    print("Props are spinning... LOOKOUT!!..")

    return None

########## MAIN EXECUTABLE ###################

vehicle = connectMyCopter()
arm()
print("End of script..")







	
