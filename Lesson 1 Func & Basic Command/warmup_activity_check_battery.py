from djitellopy import Tello  # Import the Tello library for drone control

# Step 1: Initialize the Tello drone
tello = Tello()

# Step 2: Connect to the drone
tello.connect()

# Step 3: Check the drone's battery level
battery_level = tello.get_battery()  # Get the current battery percentage
print(f"Battery: {battery_level}%")  # Display the battery level
