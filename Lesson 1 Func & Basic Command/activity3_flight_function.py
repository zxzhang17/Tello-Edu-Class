from djitellopy import Tello  # Import the Tello library for drone control

def tello_move(tello):
    """
       Executes a predefined sequence of drone commands:
       1. Take off
       2. Move forward 50 cm
       3. Perform a forward flip
       4. Perform a backward flip
       5. Move back 100 cm
       6. Land
       """
    # Take off
    tello.takeoff()

    # Move forward 50 cm
    tello.move_forward(50)

    # Flip forward
    tello.flip("f")

    # Flip backward
    tello.flip("b")

    # Move back 100 cm
    tello.move_back(100)

    # Land
    tello.land()

# Initialize the Tello drone
tello = Tello()

# Connect to the drone
tello.connect()

# Check the drone's battery level
print(f"Battery: {tello.get_battery()}%")

# Execute the tello_move() function
tello_move(tello)
