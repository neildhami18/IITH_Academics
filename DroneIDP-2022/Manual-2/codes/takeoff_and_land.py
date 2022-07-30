######### Dependencies ####################

from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import socket
import argparse

########### Functions #########

# Function to connect script to the drone
def connectMyCopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()
    connection_string = args.connect
    vehicle = connect(connection_string, wait_ready=True)
    return vehicle

# Function to arm and takeoff
def arm_and_takeoff(Altitude):
    '''
    while not vehicle.is_armable:
        print("Waiting for vehicle to become armable")
        time.sleep(1)
    '''
    vehicle.mode = VehicleMode("GUIDED")
    while vehicle.mode!="GUIDED":
        print("Waiting for vehicle to enter GUIDED mode")
        time.sleep(1)

    vehicle.armed=True
    while vehicle.armed==False:
        print("Waiting for vehicle to become armed.")
        time.sleep(1)

    vehicle.simple_takeoff(Altitude)
    
    while True:
        print("Current Altitude: %d"%vehicle.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt>=Altitude*.90:
            break
        time.sleep(1)

    print("Altitude Reached!!!")
    return None


############# Mission ###########

vehicle = connectMyCopter()
print("About to takeoff..")

vehicle.mode=VehicleMode("GUIDED")
arm_and_takeoff(3) #Target altitude is set to 3 meters.
vehicle.mode=VehicleMode("LAND")
time.sleep(2)
print("Mission Successfull")
print("Arducopter version: %s"%vehicle.version)

time.sleep(2)
vehicle.close()

###################################



