from libkl import *
from time import sleep
import os
import platform
import psutil
import re
import dotenv



dotenv.load_dotenv()

FILE_PATH = "KerEL Beta Interface.py"
TARGET_VALUE = "50"
REPLACEMENT_VALUE = "100"

def modify_file():
    if not os.path.exists(FILE_PATH):
        print("Файл 'StartXInterface' не найден.")
        return
    
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Замена скрытого счетчика
    modified_content = re.sub(r"(\bhidden_counter\s*=\s*)" + TARGET_VALUE, r"\g<1>" + REPLACEMENT_VALUE, content)
    
    if modified_content != content:
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            file.write(modified_content)

kerel_logo = r""" __    __                      ________  __       
/  |  /  |                    /        |/  |      
$$ | /$$/   ______    ______  $$$$$$$$/ $$ |      
$$ |/$$/   /      \  /      \ $$ |__    $$ |      
$$  $$<   /$$$$$$  |/$$$$$$  |$$    |   $$ |      
$$$$$  \  $$    $$ |$$ |  $$/ $$$$$/    $$ |      
$$ |$$  \ $$$$$$$$/ $$ |      $$ |_____ $$ |_____ 
$$ | $$  |$$       |$$ |      $$       |$$       |
$$/   $$/  $$$$$$$/ $$/       $$$$$$$$/ $$$$$$$$/"""

# Global variable to store folder names
folders = []

def main_loader():
    cls()
    # Simulate the bootloader process.
    print("Loader: Initializing KerEL...")
    sleep(2)
    print("Loader: Success")
    sleep(0.5)
    print("Loader: Loading essential modules...")
    sleep(2)
    print("Loader: Success")
    sleep(0.5)
    starter()

def starter():
    # Handle the boot process and user input.
    cls()
    while True:
        print(kerel_logo)
        #asm_start_check = input("") <- не имеет смысла (по моему мнению)
        #if asm_start_check == "bootloader.asm.start": <- это тоже
        if True:
            cls()
            print("boot: started")
            sleep(2)
            print("boot: initialized")
            sleep(2)
            main()
            break
        #else:
        #    print("Invalid input. Try again.")   # инвалид(
        #    ^^^ это тогда вообще выполнится не должно
        #    pass

def display_neofetch():
    # System information
    os_name = "KerEL"
    os_version = "1.1b"
    kernel_version = 1.0
    hostname = platform.node()
    cpu_info = platform.processor()
    memory = round(psutil.virtual_memory().total / (1024 ** 3), 2)

    # Display the neofetch output
    print("\033[1;34m" + kerel_logo + "\033[0m")  # Blue color for the logo
    print(f"\033[1;32m{os_name}\033[0m \033[1;37mv{os_version}\033[0m")
    print("-------------------")
    print(f"\033[1;37mHost:\033[0m {hostname}")
    print(f"\033[1;37mKernel:\033[0m {kernel_version}")
    print(f"\033[1;37mCPU:\033[0m {cpu_info}")
    print(f"\033[1;37mMemory:\033[0m {memory}")

def main():
    # Main CLI loop.
    cls()
    current_directory = "D:\\kerEL"

    while True:
        user_input = input(f"{current_directory}> ").strip()
        # Exit mechanism
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting kerEL...")
            break

        # Handle neofetch command
        match user_input.lower().split():
            case ["neofetch"]:
                display_neofetch()

        # Handle md (make directory) command
            case ["md", folder]:
                if folder:
                    folders.append(folder)
                    print(" ")
                else:
                    print("Error: Folder name cannot be empty.")
            
            case ["msg", mes]:
                os.system(f"msg * \"{mes}\"")

        # Handle cd (change directory) command
            case ["cd", folder]:
                if folder == "..":
                    # Navigate back to the parent directory
                    if current_directory != "D:\\kerEL":
                        current_directory = "D:\\kerEL"
                    else:
                        print("Already in the root directory.")
                elif folder in folders:
                    current_directory = f"D:\\kerEL\\{folder}"
                    print(" ")
                else:
                    print(f"Error: Folder '{folder}' not found.")

            case ["calc", num1, num2]:
                try:
                    num1 = int(num1)
                    num2 = int(num2)
                    print(f"Result: {num1 + num2}")
                except ValueError:
                    print("Error: Please enter valid numbers.")
            case ["calc"]:
                try:
                    in1 = int(input("Enter one value to add + > "))
                    in2 = int(input("Enter second value to add + > "))
                    print(f"Result: {in1 + in2}")
                except ValueError:
                    print("Error: Please enter valid numbers.")
            
            case ["calculator", exp]:
                print(eval(exp))
            case ["startx"]:
                os.system("python 'KerEL\\KerELBetaInterface.py'")
                modify_file()
            case ["calc", "2x0"]:
                print("else:unknown[0]:")
            
            case ["cls"]:
                cls()             

            case ["help"]:
                print("""dir -> show all directories\necho "message" -> show you entered message\nping "website.domain" -> ping site\ncls -> clear cmd\ncd "folder_name" -> swiching you to folder\nmd "folder_name" -> creating folder with you name\nhelp -> show all commands""")

            # Handle other allowed commands
            case _:
                allowed_commands = ["dir", "echo", "ping", "cls", "clear", "cd", "md", "help", "msg"]
                if user_input.lower().split()[0] in allowed_commands:
                    #os.system(user_input) <-- пашёл нахуй
                    pass
                else:
                    print(f"Error: Command '{user_input}' is not recognized or allowed.")
                    print("Allowed commands: dir, echo, ping, cls, clear, md, cd, neofetch")

if __name__ == "__main__":
    main_loader()