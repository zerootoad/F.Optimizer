import os
import requests
import subprocess
import time
import tkinter as tk
from tkinter import ttk
import glob
import threading
import sv_ttk

class FrancescoOptimizerInstaller(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x400")
        self.title("Francesco Optimizer Installer")
        self.resizable(width=False, height=False)

        self.folder = self.find_roblox_folder("%localappdata%\\Roblox\\Versions\\*")
        if not self.folder:
            self.folder = self.find_roblox_folder("%ProgramFiles(x86)%\\Roblox\\Versions\\*")
        if not self.folder:
            self.folder = self.find_roblox_folder("%ProgramFiles%\\Roblox\\Versions\\*")

        if not self.folder:
            self.log_message("ERROR: Roblox installation not found.")
            return

        self.label = ttk.Label(self, text="Francesco Optimizer", font=("Helvetica", 16))
        self.label.pack(padx=20, pady=10)

        self.button_frame = ttk.Frame(self)
        self.button_frame.pack()

        self.install_button = ttk.Button(self.button_frame, text="Install", command=self.install)
        self.install_button.pack(side="left", padx=10, pady=10)

        self.uninstall_button = ttk.Button(self.button_frame, text="Uninstall", command=self.uninstall)
        self.uninstall_button.pack(side="left", padx=10, pady=10)

        self.exit_button = ttk.Button(self.button_frame, text="Exit", command=self.exit_program)
        self.exit_button.pack(side="left", padx=10, pady=10)

        self.textbox = tk.Text(self, wrap="word", width=700, height=400)
        self.textbox.pack(padx=20, pady=10)


    def find_roblox_folder(self, pattern):
        for folder in glob.glob(os.path.expandvars(pattern)):
            roblox_exe_path = os.path.join(folder, "RobloxPlayerBeta.exe")
            if os.path.exists(roblox_exe_path):
                return folder
        return None

    def install(self):
        self.clear_textbox()
        threading.Thread(target=self.install_in_thread).start()

    def install_in_thread(self):
        client_settings_folder = os.path.join(self.folder, "ClientSettings")
        if not os.path.exists(client_settings_folder):
            os.makedirs(client_settings_folder)

        self.log_message("Downloading the essential configuration file...\n")

        config_file_url = "https://raw.githubusercontent.com/FrancescoTheToad/F.Optimizer/main/modifications/ClientSettings/ClientAppSettings.json"
        config_file_path = os.path.join(client_settings_folder, "ClientAppSettings.json")
        try:
            response = requests.get(config_file_url)
            with open(config_file_path, 'wb') as file:
                file.write(response.content)
            self.log_message("Configuration file downloaded successfully!\n")
            self.log_message("INSTALLATION SUCCESSFUL: Francesco Optimizer is ready to enhance your Roblox experience!\n")
        except Exception as e:
            self.log_message("Unable to download the configuration file.\n")
            self.log_message("INSTALLATION ERROR: Francesco Optimizer setup has encountered a problem.\n")
        
        change_cursors_urls = (
        "https://raw.githubusercontent.com/FrancescoTheToad/F.Optimizer/main/modifications/content/textures/Cursors/KeyboardMouse/ArrowCursor.png",
        "https://raw.githubusercontent.com/FrancescoTheToad/F.Optimizer/main/modifications/content/textures/Cursors/KeyboardMouse/ArrowFarCursor.png"
        )

        change_sounds_urls = (
            "https://github.com/FrancescoTheToad/F.Optimizer/blob/main/modifications/content/sounds/action_falling.mp3",
            "https://github.com/FrancescoTheToad/F.Optimizer/blob/main/modifications/content/sounds/action_footsteps_plastic.mp3",
            "https://github.com/FrancescoTheToad/F.Optimizer/blob/main/modifications/content/sounds/action_get_up.mp3",
            "https://github.com/FrancescoTheToad/F.Optimizer/blob/main/modifications/content/sounds/action_jump.mp3",
            "https://github.com/FrancescoTheToad/F.Optimizer/blob/main/modifications/content/sounds/action_jump_land.mp3",
            "https://github.com/FrancescoTheToad/F.Optimizer/blob/main/modifications/content/sounds/action_swim.mp3",
            "https://github.com/FrancescoTheToad/F.Optimizer/blob/main/modifications/content/sounds/impact_explosion_03.mp3",
            "https://github.com/FrancescoTheToad/F.Optimizer/blob/main/modifications/content/sounds/impact_water.mp3",
            "https://github.com/FrancescoTheToad/F.Optimizer/blob/main/modifications/content/sounds/ouch.ogg"
        )

        content_folder = os.path.join(self.folder, "content")
        textures_folder = os.path.join(content_folder, "textures")
        cursors_folder = os.path.join(textures_folder, "Cursors")
        cursor_folder = os.path.join(cursors_folder, "KeyboardMouse")
        for texture in os.listdir(cursor_folder):
            if texture != "IBeamCursor.png":
                self.log_message(f"Replacing: {texture}\n")
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
                self.log_message(f"Replacing: {sound}\n")
                os.remove(os.path.join(sounds_folder, sound))

        for file_url in change_sounds_urls:
            response = requests.get(file_url)
            if response.status_code == 200:
                filename = os.path.basename(file_url)
                with open(os.path.join(sounds_folder, filename), "wb") as f:
                    f.write(response.content)
        
        self.log_message("Installation successful: Francesco Optimizer has been added to your Roblox.\n")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

    def uninstall(self):
        self.clear_textbox()
        threading.Thread(target=self.uninstall_in_thread).start()

    def uninstall_in_thread(self):
        installer_path = os.path.join(self.folder, "RobloxPlayerInstaller.exe")
        config_file_path = os.path.join(self.folder, "ClientSettings", "ClientAppSettings.json")
        if os.path.exists(config_file_path):
            os.remove(config_file_path)
            self.log_message("Configuration file removed successfully!\n")

        if os.path.exists(installer_path):
            self.log_message("Running RobloxInstaller.exe...\n")
            subprocess.run([installer_path])
            found = True
        else:
            self.log_message("RobloxInstaller.exe not found. Please run it manually.\n")
            subprocess.run(["explorer", self.folder], shell=True)
            found = False
            
        if found:
            self.log_message("Uninstallation successful: Francesco Optimizer has been removed from your Roblox.\n")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

    def exit_program(self):
        self.destroy()

    def log_message(self, message):
        self.textbox.configure(state="normal")
        self.textbox.insert("end", message)
        self.textbox.see("end") 
        self.textbox.configure(state="disabled")

    def clear_textbox(self):
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", "end")
        self.textbox.configure(state="disabled")

if __name__ == "__main__":
    app = FrancescoOptimizerInstaller()
    sv_ttk.use_dark_theme(app)
    app.mainloop()
