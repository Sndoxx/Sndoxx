import os
import toml

class core:

    BOOT_CONFIGURATION = toml.load(os.getcwd() + "/src/boot.toml")
    INSTALLATION_PATH = BOOT_CONFIGURATION.get("DEFAULT").get("installation_path")

    def __init__(self):
        pass
