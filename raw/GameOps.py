import os
import shutil
import requests
import subprocess

def check_dependencies():
    for tool in ["wget", "tar"]:
        if not shutil.which(tool):
            print(f"Error: {tool} is not installed or not in PATH.")
            return False
    return True

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
    vulkan_choice = get_valid_choice("Enter your choice: ", ["1", "2", "3"])
    
    if vulkan_choice == "1":
        print("1. DirectX 9")
        print("2. DirectX 10")
        print("3. DirectX 11")
        directx_choice = get_valid_choice("Enter your choice: ", ["1", "2", "3"])
        
        if directx_choice == "1":
            install_directx9_32()
        elif directx_choice == "2":
            install_directx10_32()
        elif directx_choice == "3":
            install_directx11_32()
    elif vulkan_choice == "2":
        print("1. DirectX 9")
        print("2. DirectX 10")
        print("3. DirectX 11")
        directx_choice = get_valid_choice("Enter your choice: ", ["1", "2", "3"])
        
        if directx_choice == "1":
            install_directx9_64()
        elif directx_choice == "2":
            install_directx10_64()
        elif directx_choice == "3":
            install_directx11_64()
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
            

def download_files(target_directory, files):
    if not os.path.exists(target_directory):
        print("Target directory does not exist. Creating...")
        os.makedirs(target_directory)

    for file_name, url in files.items():
        print(f"Downloading {file_name}")
        response = requests.get(url)
        with open(os.path.join(target_directory, file_name), 'wb') as file:
            file.write(response.content)

def copy_dxvk_files_dx932(target_directory, architecture):
    """
    Copy only d3d9.dll and dxgi.dll files for DirectX 9
    """
    source_dir = f"dxvk-2.6.1/x{architecture}"
    required_files = ['d3d9.dll', 'dxgi.dll']
    try:
        for file in required_files:
            source_file = os.path.join(source_dir, file)
            dest_file = os.path.join(target_directory, file)
            if os.path.exists(source_file):
                shutil.copy2(source_file, dest_file)
                print(f"Copied {file} to {target_directory}")
            else:
                print(f"Warning: {file} not found in source directory")
    except Exception as e:
        print(f"Error copying DXVK files: {e}")
def copy_dxvk_files_dx1032(target_directory, architecture):
    """
    Copy only d3d10core.dll and dxgi.dll files for DirectX 10
    """
    source_dir = f"dxvk-2.6.1/x{architecture}"
    required_files = ['d3d10core.dll', 'dxgi.dll']
    try:
        for file in required_files:
            source_file = os.path.join(source_dir, file)
            dest_file = os.path.join(target_directory, file)
            if os.path.exists(source_file):
                shutil.copy2(source_file, dest_file)
                print(f"Copied {file} to {target_directory}")
            else:
                print(f"Warning: {file} not found in source directory")
    except Exception as e:
        print(f"Error copying DXVK files: {e}")

def copy_dxvk_files_dx1132(target_directory, architecture):
    """
    Copy only d3d11.dll and dxgi.dll files for DirectX 11
    """
    source_dir = f"dxvk-2.6.1/x{architecture}"
    required_files = ['d3d11.dll', 'dxgi.dll']
    try:
        for file in required_files:
            source_file = os.path.join(source_dir, file)
            dest_file = os.path.join(target_directory, file)
            if os.path.exists(source_file):
                shutil.copy2(source_file, dest_file)
                print(f"Copied {file} to {target_directory}")
            else:
                print(f"Warning: {file} not found in source directory")
    except Exception as e:
        print(f"Error copying DXVK files: {e}")

def copy_dxvk_files_dx964(target_directory, architecture):
    """
    Copy only d3d9.dll and dxgi.dll files for DirectX 9
    """
    source_dir = f"dxvk-2.6.1/x{architecture}"
    required_files = ['d3d9.dll', 'dxgi.dll']
    try:
        for file in required_files:
            source_file = os.path.join(source_dir, file)
            dest_file = os.path.join(target_directory, file)
            if os.path.exists(source_file):
                shutil.copy2(source_file, dest_file)
                print(f"Copied {file} to {target_directory}")
            else:
                print(f"Warning: {file} not found in source directory")
    except Exception as e:
        print(f"Error copying DXVK files: {e}")

def copy_dxvk_files_dx1064(target_directory, architecture):
    """
    Copy only d3d10core.dll and dxgi.dll files for DirectX 10
    """
    source_dir = f"dxvk-2.6.1/x{architecture}"
    required_files = ['d3d10core.dll', 'dxgi.dll']
    try:
        for file in required_files:
            source_file = os.path.join(source_dir, file)
            dest_file = os.path.join(target_directory, file)
            if os.path.exists(source_file):
                shutil.copy2(source_file, dest_file)
                print(f"Copied {file} to {target_directory}")
            else:
                print(f"Warning: {file} not found in source directory")
    except Exception as e:
        print(f"Error copying DXVK files: {e}")

def copy_dxvk_files_dx1164(target_directory, architecture):
    """
    Copy only d3d11.dll and dxgi.dll files for DirectX 11
    """
    source_dir = f"dxvk-2.6.1/x{architecture}"
    required_files = ['d3d11.dll', 'dxgi.dll']
    try:
        for file in required_files:
            source_file = os.path.join(source_dir, file)
            dest_file = os.path.join(target_directory, file)
            if os.path.exists(source_file):
                shutil.copy2(source_file, dest_file)
                print(f"Copied {file} to {target_directory}")
            else:
                print(f"Warning: {file} not found in source directory")
    except Exception as e:
        print(f"Error copying DXVK files: {e}")


def install_directx9_32():
    target_directory = input("Enter the Game.exe directory path: ")
    copy_dxvk_files_dx932(target_directory, "32")
    print("DirectX 9 32-bit requirements have been installed")

def install_directx10_32():
    target_directory = input("Enter the Game.exe directory path: ")
    copy_dxvk_files_dx1032(target_directory, "32")
    print("DirectX 10 32-bit requirements have been installed")

def install_directx11_32():
    target_directory = input("Enter the Game.exe directory path: ")
    copy_dxvk_files_dx1132(target_directory, "32")
    print("DirectX 11 32-bit requirements have been installed")

def install_directx9_64():
    target_directory = input("Enter the Game.exe directory path: ")
    copy_dxvk_files_dx964(target_directory, "64")
    print("DirectX 9 64-bit requirements have been installed")

def install_directx10_64():
    target_directory = input("Enter the Game.exe directory path: ")
    copy_dxvk_files_dx1064(target_directory, "64")
    print("DirectX 10 64-bit requirements have been installed")

def install_directx11_64():
    target_directory = input("Enter the Game.exe directory path: ")
    copy_dxvk_files_dx1164(target_directory, "64")
    print("DirectX 11 64-bit requirements have been installed")

def perform_optimization():
    print("1. Amd Ryzen Tdp Change (RyzenAdj)")
    print("2. Other Optimizations (Coming soon)")
    choice = get_valid_choice("Enter your choice: ", ["1", "2"])
    if choice =="1":
        ryzenadjusment()
    elif choice =="2":
        print("coming soon")

    pass
def ryzenadjusment():
    print("1. 15 watt")
    print("2. 25 watt")
    print("3. 30 watt")
    print("4. 45 watt")
    choice = get_valid_choice("Enter your choice: ", ["1", "2", "3", "4"])
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
        
    pass               
        
def get_valid_choice(prompt, choices):
    while True:
        choice = input(prompt)
        if choice in choices:
            return choice
        print("Invalid choice. Please try again.")

def download_dxvk():
    url = "https://github.com/doitsujin/dxvk/releases/download/v2.6.1/dxvk-2.6.1.tar.gz"
    output_file = "dxvk-2.6.1.tar.gz"

    try:
        # Execute wget command
        cmd_command = f"wget {url} -O {output_file}"
        result = subprocess.run(cmd_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            print("Error output:")
            print(result.stderr)
            print("Failed to download the file. Please ensure wget is installed and in PATH.")
            return False

        # Extract the tar.gz file
        print("Extracting DXVK files...")
        extract_cmd = f"tar -xzf {output_file}"
        extract_result = subprocess.run(extract_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if extract_result.returncode != 0:
            print("Error extracting files:")
            print(extract_result.stderr)
            return False

        print("DXVK files extracted successfully")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main():
    # Clear the console
    os.system("cls" if os.name == "nt" else "clear")
    print("Starting GameOps...")

    # Download the DXVK file
    download_dxvk()

    while True:
        print("GameOps By Test_bench")
        print("Main Menu")
        print("1. Install/Uninstall Vulkan")
        print("2. Optimization")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            install_vulkan()
        elif choice == "2":
            perform_optimization()
        elif choice == "3":
            print("Exiting GameOps. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
