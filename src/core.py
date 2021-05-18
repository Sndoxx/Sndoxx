import os
import toml

class core:

    BOOT_CONFIGURATION = toml.load(os.getcwd() + "/src/boot.toml")
    OS_PATH = BOOT_CONFIGURATION.get("DEFAULT").get("installation_path")
    DATA_PATH: str = None
    STORAGE_PATH: str = None
    SYSTEM_PATH: str = None


    def __init__(self):
        pass

    def createSystem(self):
        if os.path.exists(self.OS_PATH + "/system/"):
            print("Already installed in the location")
            self.SYSTEM_PATH = self.OS_PATH + "/system/"
            self._lockSystem()
        else:
            os.mkdir(self.OS_PATH + "/system/")
            self.SYSTEM_PATH = self.OS_PATH + "/system/"

    def _lockSystem(self):
        lockfile = open(self.SYSTEM_PATH + "lock", "w")
        lockfile.write("0")
