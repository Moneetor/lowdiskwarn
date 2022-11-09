import os
import shutil
import json


class Config:
    def __int__(self, configfile):
        self.ConfigFile = configfile
        self.Options = dict()
        self.load()

    def load(self):
        try:
            with open(self.ConfigFile) as ofile:
                config = json.load(ofile)
            self.Options = config['Options']
        except FileNotFoundError:
            self.dump()

    def dump(self):
        pass


def print_lowdisk_status():
    # Use a breakpoint in the code line below to debug your script.
    ds = shutil.disk_usage('/')
    # dsf =
    print(format(ds.free, 'Free space on disk is {1}'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ConfigDir = os.path.join(os.environ['HOME'], '.lowdiskwarn')
    ConfigFile = os.path.join(ConfigDir, 'config.json')
    Config = Config(ConfigFile)
    print_lowdisk_status()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
