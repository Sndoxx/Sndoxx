import toml
import os
import sys
from src.core import core

if __name__ == "__main__":
    BOOT_CONFIG = toml.load(os.getcwd() + "/src/boot.toml")
    OS_DIR = BOOT_CONFIG.get("DEFAULT").get("installation_path")
    system = core()
    system.createSystem()
