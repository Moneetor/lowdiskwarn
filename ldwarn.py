# import os
import shutil
import argparse
from math import log
from math import floor
from math import ceil


def diskspace(size):
    prefixes = [
        'PiB',
        'EiB',
        'TiB',
        'GiB',
        'MiB',
        'kiB',
        'B',
    ]
    prefixes=prefixes[-1::-1]
    pps = int(floor(log(size, 1024)))
    dss = size / 1024**pps
    prefix = prefixes[pps]
    return '{0:0.2f} {1}'.format(dss, prefix)


def print_lowdisk_status(verbose=False, minimal=400*1024**2):
    # Use a breakpoint in the code line below to debug your script.
    ds = shutil.disk_usage('/')
    dsf = diskspace(ds.free)
    if verbose is True or minimal < ds.free:
        print('Free space on disk is {0}'.format(dsf))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    description = 'Low disk space alerting service for MOTD'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-v', dest='verbose', default=False, action='store_true', help='Verbose true')
    args = parser.parse_args()
    verbose = args.verbose
    print_lowdisk_status(verbose)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
