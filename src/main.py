import time
import os
import platform

# Global variable to store folder names
folders = []

def clear_screen():
    """Clear the screen (cross-platform)."""
    os.system("cls" if os.name == "nt" else "clear")

def main_loader():
    """Simulate the bootloader process."""
    print("Loader: Initializing KerEL...")
    time.sleep(2)
    print("Loader: KerEL core activated!")
    time.sleep(0.5)
    print("Loader: Loading essential modules...")
    time.sleep(2)
    print("Loader: Modules successfully integrated!")
    time.sleep(0.5)
    starter()

def starter():
    """Handle the boot process and user input."""
    clear_screen()
    while True:
        Bootloader = r"""
         _
     ---(_)
 _/  ---  \
(_) |   |  
  \  --- _/
     ---(_)
     KerEL Bootloader
        """
        print(Bootloader)
        asm_start_check = input("")
        if asm_start_check == 'bootloader.asm.start':
            clear_screen()
            print("boot: started")
            time.sleep(2)
            print("boot: initialized")
            time.sleep(2)
            main()
            break
        else:
            print("Invalid input. Try again.")

def display_neofetch():
    """Display system information in a neofetch-style format."""
    # ASCII art for Ubuntu logo
    ubuntu_logo = r"""
         _
     ---(_)
 _/  ---  \
(_) |   |
  \  --- _/
     ---(_)
    """

    # System information
    os_name = "KerEL"
    os_version = "1.0"
    kernel_version = platform.release()
    hostname = platform.node()
    cpu_info = platform.processor()
    memory = "16GB"  # Placeholder, you can use `psutil` to get real memory usage

    # Display the neofetch output
    print("\033[1;34m" + ubuntu_logo + "\033[0m")  # Blue color for the logo
    print(f"\033[1;32m{os_name}\033[0m \033[1;37mv{os_version}\033[0m")
    print("-------------------")
    print(f"\033[1;37mHost:\033[0m {hostname}")
    print(f"\033[1;37mKernel:\033[0m {kernel_version}")
    print(f"\033[1;37mCPU:\033[0m {cpu_info}")
    print(f"\033[1;37mMemory:\033[0m {memory}")

def main():
    """Main CLI loop."""
    clear_screen()
    current_directory = "D:/kerEL"

    while True:
        user_input = input(f"{current_directory}> ").strip()

        # Exit mechanism
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting kerEL...")
            break

        # Handle neofetch command
        if user_input == "neofetch":
            display_neofetch()

        # Handle md (make directory) command
        elif user_input.startswith("md "):
            folder_name = user_input[3:].strip()  # Extract folder name from command
            if folder_name:
                folders.append(folder_name)
                print(" ")
            else:
                print("Error: Folder name cannot be empty.")

        # Handle cd (change directory) command
        elif user_input.startswith("cd"):
            folder_name = user_input[3:].strip()  # Extract folder name from command
            if folder_name == "..":
                # Navigate back to the parent directory
                if current_directory != "D:/kerEL":
                    current_directory = "D:/kerEL"
                else:
                    print("Already in the root directory.")
            elif folder_name in folders:
                current_directory = f"D:/kerEL/{folder_name}"
                print(" ")
            else:
                print(f"Error: Folder '{folder_name}' not found.")

        elif user_input == "help":
            print("""dir -> show all directory's
                    echo 'message' -> show you entered message
                  ping 'website.domain' -> ping site
                 cls -> clear cmd
                cd 'folder_name' -> swiching you to folder
               md 'folder_name' -> creating folder with you name
              help -> show all commands""")

        # Handle other allowed commands
        else:
            allowed_commands = ["dir", "echo", "ping", "cls", "clear", "cd", "md", "help"]
            if user_input.split()[0] in allowed_commands:
                os.system(user_input)
            else:
                print(f"Error: Command '{user_input}' is not recognized or allowed.")
                print("Allowed commands: dir, echo, ping, cls, clear, md, cd, neofetch")

if __name__ == "__main__":
    main_loader()
