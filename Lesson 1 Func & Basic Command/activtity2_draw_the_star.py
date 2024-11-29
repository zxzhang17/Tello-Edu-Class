from djitellopy import Tello

def move_shape(tello):
    """
    Moves the Tello drone in a star pattern.

    Parameters:
    tello (Tello): An instance of the Tello class controlling the drone.
    """
    for _ in range(5):  # A star pattern has 5 points
        tello.move_forward(100)  # Move forward by 100 cm
        tello.rotate_clockwise(144)  # Turn 144 degrees to create the star shape

# Step 1: Initialize the Tello drone
tello = Tello()

# Step 2: Connect to the drone
tello.connect()

# Step 3: Check the drone's battery level
print(f"Battery: {tello.get_battery()}%")

# Step 4: Take off
tello.takeoff()

# Step 5: Execute the star movement
move_shape(tello)

# Step 6: Land the drone
tello.land()
