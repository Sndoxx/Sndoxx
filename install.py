import toml
import os
import sys

if __name__ == "__main__":
    BOOT_CONFIG = toml.load(os.getcwd() + "/src/boot.toml")
    BOOT_CONFIG["DEFAULT"]["installation_path"] = sys.argv[1]