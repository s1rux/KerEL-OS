import os
import platform
import time

def starter():
    os.system("cls")
    asm_start_check = input("")
    if asm_start_check == 'boot.asm.start':
        print("boot: started")
        time.sleep(2)
        print("boot: intilizated")
        time.sleep(2)
        main()

def display_neofetch():
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
    # Clear the screen (cross-platform)
    os.system("cls" if os.name == "nt" else "clear")

    while True:
        user_input = input("D:/kerEL> ").strip()

        # Exit mechanism
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting kerEL...")
            break

        # Handle neofetch command
        if user_input == "neofetch":
            display_neofetch()
        else:
            # Safe command execution (example: only allow specific commands)
            allowed_commands = ["dir", "echo", "ping", "cls", "clear"]
            if user_input.split()[0] in allowed_commands:
                os.system(user_input)
            else:
                print(f"Error: Command '{user_input}' is not allowed.")

if __name__ == "__main__":
    starter()