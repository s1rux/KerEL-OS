import time
import os

# Clear the screen (cross-platform)
os.system("cls" if os.name == "nt" else "clear")

# Simulate the loading of "KerEL"
print("Loader: Initializing KerEL...")
time.sleep(2)  # Pause for dramatic effect
print("Loader: KerEL core activated!")
time.sleep(0.5)

# Simulate module loading
print("Loader: Loading essential modules...")
time.sleep(2)
print("Loader: Modules successfully integrated!")
time.sleep(0.5)

# Transition to the next script
print("Loader: Preparing to hand over control to os_starter.py...")
time.sleep(3)

# Check if the file exists
if os.path.exists("os_starter.py"):
    print("Loader: Launching os_starter.py...")
    try:
        # Execute the os_starter.py script
        if os.name == "nt":  # Windows
            os.system("python os_starter.py")
        else:  # Unix-like systems
            os.system("python3 os_starter.py")
    except Exception as e:
        print(f"Loader: Failed to launch os_starter.py. Error: {e}")
else:
    print("Loader: Critical error! os_starter.py not found. Aborting mission.")