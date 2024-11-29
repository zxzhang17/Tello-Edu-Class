from djitellopy import Tello

def drone_takeoff(tello):
    tello.takeoff()
    print("Drone has taken off!")

def drone_land(tello):
    tello.land()
    print("Drone has landed!")

# Initialize drone
tello = Tello()
tello.connect()

# Battery check
print(f"Battery: {tello.get_battery()}%")

# Call the functions
drone_takeoff(tello)
drone_land(tello)
