import os
import requests
import glob
import subprocess
import time


def next_step(folder):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n--- FairBlox Optimizer Installer ---")
        print("Developed by: Zeroo\n")

        print("Choose an option:")
        print("1. Install FairBlox Optimizer")
        print("2. Uninstall FairBlox Optimizer")
        print("3. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            install(folder)
        elif choice == "2":
            uninstall(folder)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid number.")

def main():
    print("\n--- FairBlox Optimizer Installer ---")
    print("Developed by: Zeroo\n")

    print("Initializing FairBlox Optimizer installation...\n")

    folder = find_roblox_folder("%localappdata%\\Roblox\\Versions\\*")
    if not folder:
        folder = find_roblox_folder("%ProgramFiles(x86)%\\Roblox\\Versions\\*")
    if not folder:
        folder = find_roblox_folder("%ProgramFiles%\\Roblox\\Versions\\*")

    if not folder:
        print("ERROR: Roblox installation not found.")
        return

    next_step(folder)

def find_roblox_folder(pattern):
    for folder in glob.glob(os.path.expandvars(pattern)):
        roblox_exe_path = os.path.join(folder, "RobloxPlayerBeta.exe")
        if os.path.exists(roblox_exe_path):
            return folder
    return None

def install(folder):
    client_settings_folder = os.path.join(folder, "ClientSettings")
    if not os.path.exists(client_settings_folder):
        os.makedirs(client_settings_folder)

    print("Downloading the essential configuration file...\n")

    config_file_url = "https://raw.githubusercontent.com/zerootoad/F.Optimizer/main/modifications/ClientSettings/ClientAppSettings.json"
    config_file_path = os.path.join(client_settings_folder, "ClientAppSettings.json")
    try:
        response = requests.get(config_file_url)
        with open(config_file_path, 'wb') as file:
            file.write(response.content)
        print("Configuration file downloaded successfully!\n")
    except Exception as e:
        print("Unable to download the configuration file.\n")
    
    change_cursors_urls = (
    "https://raw.githubusercontent.com/zerootoad/F.Optimizer/main/modifications/content/textures/Cursors/KeyboardMouse/ArrowCursor.png",
    "https://raw.githubusercontent.com/zerootoad/F.Optimizer/main/modifications/content/textures/Cursors/KeyboardMouse/ArrowFarCursor.png"
    )

    change_sounds_urls = (
        "https://github.com/zerootoad/F.Optimizer/blob/main/modifications/content/sounds/action_falling.mp3",
        "https://github.com/zerootoad/F.Optimizer/blob/main/modifications/content/sounds/action_footsteps_plastic.mp3",
        "https://github.com/zerootoad/F.Optimizer/blob/main/modifications/content/sounds/action_get_up.mp3",
        "https://github.com/zerootoad/F.Optimizer/blob/main/modifications/content/sounds/action_jump.mp3",
        "https://github.com/zerootoad/F.Optimizer/blob/main/modifications/content/sounds/action_jump_land.mp3",
        "https://github.com/zerootoad/F.Optimizer/blob/main/modifications/content/sounds/action_swim.mp3",
        "https://github.com/zerootoad/F.Optimizer/blob/main/modifications/content/sounds/impact_explosion_03.mp3",
        "https://github.com/zerootoad/F.Optimizer/blob/main/modifications/content/sounds/impact_water.mp3",
        "https://github.com/zerootoad/F.Optimizer/blob/main/modifications/content/sounds/ouch.ogg"
    )

    content_folder = os.path.join(folder, "content")
    textures_folder = os.path.join(content_folder, "textures")
    cursors_folder = os.path.join(textures_folder, "Cursors")
    cursor_folder = os.path.join(cursors_folder, "KeyboardMouse")
    for texture in os.listdir(cursor_folder):
        if texture != "IBeamCursor.png":
            print(f"Replacing: {texture}")
            os.remove(os.path.join(cursor_folder, texture))


    for file_url in change_cursors_urls:
        response = requests.get(file_url)
        if response.status_code == 200:
            filename = os.path.basename(file_url)
            with open(os.path.join(cursor_folder, filename), "wb") as f:
                f.write(response.content)

    sounds_folder = os.path.join(content_folder, "sounds")
    for sound in os.listdir(sounds_folder):
        if sound != "volume_slider.ogg":
            print(f"Replacing: {sound}")
            os.remove(os.path.join(sounds_folder, sound))

    for file_url in change_sounds_urls:
        response = requests.get(file_url)
        if response.status_code == 200:
            filename = os.path.basename(file_url)
            with open(os.path.join(sounds_folder, filename), "wb") as f:
                f.write(response.content)
    
    print("Installation successful: FairBlox Optimizer has been added to your Roblox.\n")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

def uninstall(folder):
    installer_path = os.path.join(folder, "RobloxPlayerInstaller.exe")
    config_file_path = os.path.join(folder, "ClientSettings", "ClientAppSettings.json")
    if os.path.exists(config_file_path):
        os.remove(config_file_path)
        print("Configuration file removed successfully!\n")

    if os.path.exists(installer_path):
        print("Running RobloxInstaller.exe...")
        subprocess.run([installer_path])
        found = True
    else:
        print("RobloxInstaller.exe not found. Please run it manually.")
        subprocess.run(["explorer", folder], shell=True)
        found = False
        
    if found:
        print("Uninstallation successful: FairBlox Optimizer has been removed from your Roblox.\n")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')