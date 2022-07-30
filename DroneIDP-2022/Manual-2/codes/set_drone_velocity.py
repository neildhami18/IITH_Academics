######### Dependencies ####################

from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
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

def set_velocity(Vx,Vy,Vz):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
            0,
            0,0,
            mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED,
            0b0000111111000111, #BITMASK -> Consider only the velocities
            0,0,0, #position
            Vx,Vy,Vz, #velocity
            0,0,0, #Accelerations
            0,0)
    vehicle.send_mavlink(msg)
    vehicle.flush()



############# Mission ###########

vehicle = connectMyCopter()
print("About to takeoff..")

vehicle.mode=VehicleMode("GUIDED")
arm_and_takeoff(3) #Target altitude is set to 3 meters.

counter=0
while counter<2:
    set_velocity(1,0,0)
    print("Direction: NORTH relative to heading of drone")
    time.sleep(1)
    counter+=1

counter=0
while counter<2:
    set_velocity(-1,0,0)
    print("Direction: SOUTH relative to heading of drone")
    time.sleep(1)
    counter+=1

counter=0
while counter<2:
    set_velocity(0,1,0)
    print("Direction: EAST relative to heading of drone")
    time.sleep(1)
    counter+=1

counter=0
while counter<2:
    set_velocity(0,-1,0)
    print("Direction: WEST relative to heading of drone")
    time.sleep(1)
    counter+=1


vehicle.mode=VehicleMode("LAND")
time.sleep(2)
print("Mission Successfull")
print("Arducopter version: %s"%vehicle.version)

time.sleep(2)
vehicle.close()

###################################



