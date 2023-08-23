import os
import shutil
import requests
import subprocess

def copy_wget():
    source_file = "wget.exe"
    destination_file = r"C:\Windows\System32"
    
    try:
        shutil.copy(source_file, destination_file)
        print(f"'{source_file}' has been copied to '{destination_file}'")
    except Exception as e:
        print(f"An error occurred while copying '{source_file}': {e}")
        
        
def install_vulkan():
    print("1. Vulkan 32-bit")
    print("2. Vulkan 64-bit")
    print("3. Uninstall Vulkan")
    vulkan_choice = input("Enter your choice: ")
    
    if vulkan_choice == "1":
        print("1. DirectX 9")
        print("2. DirectX 10")
        print("3. DirectX 11")
        directx_choice = input("Enter your choice: ")
        
        if directx_choice == "1":
            install_directx9_32()
        elif directx_choice == "2":
            install_directx10_32()
        elif directx_choice == "3":
            install_directx11_32()
        else:
            print("Invalid choice. Please select a valid option.")
    elif vulkan_choice == "2":
        print("1. DirectX 9")
        print("2. DirectX 10")
        print("3. DirectX 11")
        directx_choice = input("Enter your choice: ")
        
        if directx_choice == "1":
            install_directx9_64()
        elif directx_choice == "2":
            install_directx10_64()
        elif directx_choice == "3":
            install_directx11_64()
        else:
            print("Invalid choice. Please select a valid option.")    
        pass
    elif vulkan_choice == "3":
        try:
            target_directory = input("Enter the Game.exe directory path: ")
            
            vulkan_files = [
                os.path.join(target_directory, "d3d10core.dll"),
                os.path.join(target_directory, "d3d9.dll"),
                os.path.join(target_directory, "d3d11.dll"),
                os.path.join(target_directory, "dxgi.dll")
                # Add more file paths as needed
            ]

            confirm = input("Are you sure you want to uninstall Vulkan? (y/n): ")
            if confirm.lower() == "y":
                for file_path in vulkan_files:
                    if os.path.exists(file_path):
                        os.remove(file_path)
                        print(f"File '{file_path}' has been deleted.")
                    else:
                        print(f"File '{file_path}' does not exist.")

                print("Vulkan has been uninstalled.")
            else:
                print("Vulkan uninstallation cancelled.")
        except Exception as e:
            print(f"An error occurred while uninstalling Vulkan: {e}")
            


def install_directx9_32():
    # Rest of your code for installing DirectX 9
    downloaddxgi = "https://github.com/Naufal453/Gameops/blob/main/dxvk-2.2.tar/dxvk-2.2/x32/dxgi.dll"
    downloadd3d9 = "https://github.com/Naufal453/Gameops/blob/main/dxvk-2.2.tar/dxvk-2.2/x32/d3d9.dll"
    
    target_directory = input("Enter the Game.exe directory path: ")
    
    if not os.path.exists(target_directory):
        print("Target directory does not exist. Creating...")
        os.makedirs(target_directory)
    
    print("Downloading dxgi.dll")
    response_dxgi = requests.get(downloaddxgi)
    with open(os.path.join(target_directory, "dxgi.dll"), 'wb') as file:
        file.write(response_dxgi.content)
    
    print("Downloading d3d9.dll")
    response_d3d9 = requests.get(downloadd3d9)
    with open(os.path.join(target_directory, "d3d9.dll"), 'wb') as file:
        file.write(response_d3d9.content)
    
    print("The requirements have been installed")
    pass

def install_directx10_32():
    # Rest of your code for installing DirectX 10
    downloaddxgi = "https://github.com/Naufal453/Gameops/blob/main/dxvk-2.2.tar/dxvk-2.2/x32/dxgi.dll"
    downloadd3d10 = "https://github.com/Naufal453/Gameops/blob/main/dxvk-2.2.tar/dxvk-2.2/x32/d3d10core.dll"
    
    target_directory = input("Enter the Game.exe directory path: ")
    
    if not os.path.exists(target_directory):
        print("Target directory does not exist. Creating...")
        os.makedirs(target_directory)
    
    print("Downloading dxgi.dll")
    response_dxgi = requests.get(downloaddxgi)
    with open(os.path.join(target_directory, "dxgi.dll"), 'wb') as file:
        file.write(response_dxgi.content)
    
    print("Downloading d3d10core.dll")
    response_d3d10core = requests.get(downloadd3d10)
    with open(os.path.join(target_directory, "d3d10core.dll"), 'wb') as file:
        file.write(response_d3d10core.content)
    
    print("The requirements have been installed")
    pass

def install_directx11_32():
    # Rest of your code for installing DirectX 11
    downloaddxgi = "https://github.com/Naufal453/Gameops/blob/main/dxvk-2.2.tar/dxvk-2.2/x32/dxgi.dll"
    downloadd3d11 = "https://github.com/Naufal453/Gameops/blob/main/dxvk-2.2.tar/dxvk-2.2/x32/d3d11.dll"
    
    target_directory = input("Enter the Game.exe directory path: ")
    
    if not os.path.exists(target_directory):
        print("Target directory does not exist. Creating...")
        os.makedirs(target_directory)
    
    print("Downloading dxgi.dll")
    response_dxgi = requests.get(downloaddxgi)
    with open(os.path.join(target_directory, "dxgi.dll"), 'wb') as file:
        file.write(response_dxgi.content)
    
    print("Downloading d3d11.dll")
    response_d3d11 = requests.get(downloadd3d11)
    with open(os.path.join(target_directory, "d3d11.dll"), 'wb') as file:
        file.write(response_d3d11.content)
    
    print("The requirements have been installed")
    pass

def install_directx9_64():
    downloaddxgi = "https://github.com/Naufal453/Gameops/blob/main/dxvk-2.2.tar/dxvk-2.2/x64/dxgi.dll"
    downloadd3d9 = "https://github.com/Naufal453/Gameops/blob/main/dxvk-2.2.tar/dxvk-2.2/x64/d3d9.dll"
    
    target_directory = input("Enter the Game.exe directory path: ")
    
    if not os.path.exists(target_directory):
        print("Target directory does not exist. Creating...")
        os.makedirs(target_directory)
    
    print("Downloading dxgi.dll")
    response_dxgi = requests.get(downloaddxgi)
    with open(os.path.join(target_directory, "dxgi.dll"), 'wb') as file:
        file.write(response_dxgi.content)
    
    print("Downloading d3d9.dll")
    response_d3d9 = requests.get(downloadd3d9)
    with open(os.path.join(target_directory, "d3d9.dll"), 'wb') as file:
        file.write(response_d3d9.content)
    
    print("The requirements have been installed")
    pass

def install_directx10_64():
    downloaddxgi = "https://github.com/Naufal453/Gameops/blob/main/dxvk-2.2.tar/dxvk-2.2/x64/dxgi.dll"
    downloadd3d10 = "https://github.com/Naufal453/Gameops/blob/main/dxvk-2.2.tar/dxvk-2.2/x64/d3d10core.dll"
    
    target_directory = input("Enter the Game.exe directory path: ")
    
    if not os.path.exists(target_directory):
        print("Target directory does not exist. Creating...")
        os.makedirs(target_directory)
    
    print("Downloading dxgi.dll")
    response_dxgi = requests.get(downloaddxgi)
    with open(os.path.join(target_directory, "dxgi.dll"), 'wb') as file:
        file.write(response_dxgi.content)
    
    print("Downloading d3d10core.dll")
    response_d3d10core = requests.get(downloadd3d10)
    with open(os.path.join(target_directory, "d3d10core.dll"), 'wb') as file:
        file.write(response_d3d10core.content)
    
    print("The requirements have been installed")
    pass

def install_directx11_64():
    downloaddxgi = "https://github.com/Naufal453/Gameops/blob/main/dxvk-2.2.tar/dxvk-2.2/x64/dxgi.dll"
    downloadd3d11 = "https://github.com/Naufal453/Gameops/blob/main/dxvk-2.2.tar/dxvk-2.2/x64/d3d11.dll"
    
    target_directory = input("Enter the Game.exe directory path: ")
    
    if not os.path.exists(target_directory):
        print("Target directory does not exist. Creating...")
        os.makedirs(target_directory)
    
    print("Downloading dxgi.dll")
    response_dxgi = requests.get(downloaddxgi)
    with open(os.path.join(target_directory, "dxgi.dll"), 'wb') as file:
        file.write(response_dxgi.content)
    
    print("Downloading d3d11.dll")
    response_d3d11 = requests.get(downloadd3d11)
    with open(os.path.join(target_directory, "d3d11.dll"), 'wb') as file:
        file.write(response_d3d11.content)
    
    print("The requirements have been installed")
    pass

def perform_optimization():
    print("1. Amd Ryzen Tdp Change (RyzenAdj)")
    print("2. Other Optimizations (Coming soon)")
    choice = input("Enter your choice: ")
    if choice =="1":
        ryzenadjusment()
    elif choice =="2":
        print("coming soon")
    else:
        print("Invalid choice")

    pass
def ryzenadjusment():
    print("1. 15 watt")
    print("2. 25 watt")
    print("3. 30 watt")
    print("4. 45 watt")
    choice = input("Enter your choice: ")
    if choice =="1":
        script_dir = os.path.dirname(os.path.abspath(__file__))
        subdirectory_name = "ryzenadj-win64"
        ryzenadj_path = os.path.join(script_dir, subdirectory_name, "ryzenadj.exe")

        cmd_command = rf'"{ryzenadj_path}" --stapm-limit=15000 --fast-limit=15000 --slow-limit=15000 --tctl-temp=80 --max-performance'

        try:
            result = subprocess.run(cmd_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            # Print the command's standard output
            print("Command output:")
            print(result.stdout)
    
            # Print the command's error output
            print("Error output:")
            print(result.stderr)    
        except subprocess.CalledProcessError as e:
            print("Error:", e)
    elif choice =="2":
        script_dir = os.path.dirname(os.path.abspath(__file__))
        subdirectory_name = "ryzenadj-win64"
        ryzenadj_path = os.path.join(script_dir, subdirectory_name, "ryzenadj.exe")

        cmd_command = rf'"{ryzenadj_path}" --stapm-limit=25000 --fast-limit=25000 --slow-limit=25000 --tctl-temp=90 --max-performance'

        try:
            result = subprocess.run(cmd_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            # Print the command's standard output
            print("Command output:")
            print(result.stdout)
    
            # Print the command's error output
            print("Error output:")
            print(result.stderr)            
        except subprocess.CalledProcessError as e:
            print("Error:", e)
    elif choice =="3":
        script_dir = os.path.dirname(os.path.abspath(__file__))
        subdirectory_name = "ryzenadj-win64"
        ryzenadj_path = os.path.join(script_dir, subdirectory_name, "ryzenadj.exe")

        cmd_command = rf'"{ryzenadj_path}" --stapm-limit=30000 --fast-limit=30000 --slow-limit=30000 --tctl-temp=90 --max-performance'

        try:
            result = subprocess.run(cmd_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            # Print the command's standard output
            print("Command output:")
            print(result.stdout)
    
            # Print the command's error output
            print("Error output:")
            print(result.stderr)             
        except subprocess.CalledProcessError as e:
            print("Error:", e)
    elif choice =="4":
        script_dir = os.path.dirname(os.path.abspath(__file__))
        subdirectory_name = "ryzenadj-win64"
        ryzenadj_path = os.path.join(script_dir, subdirectory_name, "ryzenadj.exe")

        cmd_command = rf'"{ryzenadj_path}" --stapm-limit=45000 --fast-limit=45000 --slow-limit=45000 --tctl-temp=95 --max-performance'

        try:
            result = subprocess.run(cmd_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            # Print the command's standard output
            print("Command output:")
            print(result.stdout)
    
            # Print the command's error output
            print("Error output:")
            print(result.stderr)             
        except subprocess.CalledProcessError as e:
            print("Error:", e)
    else:
        print("Invalid choice. Please select a valid option.")
        
    pass               
        
    
def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("GameOps By Test_bench")
        print("Main Menu")
        print("1. Install/Uninstall Vulkan")
        print("2. Optimization")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            copy_wget()  # Call the function to copy wget.exe
            install_vulkan()
        elif choice == "2":
            perform_optimization()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select a valid option.")
        
        input("Press Enter to continue...")
    
if __name__ == "__main__":
    main()
