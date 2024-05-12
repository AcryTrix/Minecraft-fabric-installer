"""Install Fabric for Minecraft.

This script takes the Minecraft directory and version from the user and uses the
minecraft_launcher_lib library to install Fabric for the specified version.

The script prompts the user for the Minecraft directory and version.

The script then installs Fabric using the minecraft_launcher_lib library.

Args:
    minecraft_directory (str): The directory where Minecraft is installed.
    minecraft_version (str): The Minecraft version to install Fabric for.

"""
import minecraft_launcher_lib as mll

# Prompt the user for the Minecraft directory and version
minecraft_directory = input("Minecraft directory: ")
minecraft_version = input("Version: ")

# Install Fabric using the minecraft_launcher_lib library
mll.fabric.install_fabric(minecraft_version, minecraft_directory)

