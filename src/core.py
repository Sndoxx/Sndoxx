import os
import toml

class core:

    BOOT_CONFIGURATION = toml.load(os.getcwd() + "/src/boot.toml")
    SYSTEM_PATH = BOOT_CONFIGURATION.get("DEFAULT").get("installation_path")
    DATA_PATH = None
    STORAGE_PATH = None

    def __init__(self):
        pass

    def createSystem(self):
        if os.path.exists(self.SYSTEM_PATH + "/system/"):
            print("system path exists!")
        else:
            os.mkdir(self.SYSTEM_PATH + "/system/")
