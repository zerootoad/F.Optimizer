import os
import requests
import glob

def main():
    print("\n--- Francesco Optimizer Installer ---")
    print("Developed by: Zeroo\n")

    print("Initializing Francesco Optimizer installation...\n")

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

def next_step(folder):
    client_settings_folder = os.path.join(folder, "ClientSettings")
    if not os.path.exists(client_settings_folder):
        os.makedirs(client_settings_folder)

    print("Downloading the essential configuration file...\n")

    config_file_url = "https://raw.githubusercontent.com/FrancescoTheToad/F.Optimizer/main/client settings/ClientAppSettings.json"
    config_file_path = os.path.join(client_settings_folder, "ClientAppSettings.json")
    try:
        response = requests.get(config_file_url)
        with open(config_file_path, 'wb') as file:
            file.write(response.content)
        print("Configuration file downloaded successfully!\n")
        print("INSTALLATION SUCCESSFUL: Francesco Optimizer is ready to enhance your Roblox experience!\n")
    except Exception as e:
        print("Unable to download the configuration file.\n")
        print("INSTALLATION ERROR: Francesco Optimizer setup has encountered a problem.\n")
    
    change_cursors_urls = (
    "https://raw.githubusercontent.com/FrancescoTheToad/F.Optimizer/main/modifications/content/textures/Cursors/KeyboardMouse/ArrowCursor.png",
    "https://raw.githubusercontent.com/FrancescoTheToad/F.Optimizer/blob/main/modifications/content/textures/Cursors/KeyboardMouse/ArrowFarCursor.png"
    )

    content_folder = os.path.join(folder, "content")
    for child in content_folder:
        textures_folder = os.path.join(child, "textures")
        sounds_folder = os.path.join(child, "sounds")
        


    input("Press Enter to exit...")

if __name__ == "__main__":
    main()