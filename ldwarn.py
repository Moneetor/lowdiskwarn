# import os
import shutil
import argparse
from math import log
from math import floor
DefaultLowSpaceSize = 400*1024**2


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
    prefixes = prefixes[-1::-1]
    if size < 1024:
        prefix = prefixes[0]
        dss = size
        return '{0:d} {1}'.format(dss, prefix)
    pps = int(floor(log(size, 1024)))
    dss = size / 1024**pps
    prefix = prefixes[pps]
    return '{0:0.2f} {1}'.format(dss, prefix)


def print_lowdisk_status(verbose=False, minimal=DefaultLowSpaceSize):
    ds = shutil.disk_usage('/')
    dsf = diskspace(ds.free)
    if verbose is True or minimal > ds.free:
        print('Free space on disk is {0}'.format(dsf))


if __name__ == '__main__':
    description = 'Low disk space alerting service for MOTD'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        '-v', dest='verbose', default=False, action='store_true', help='Verbose true'
    )
    parser.add_argument(
        '-m', dest='size',
        type=int,
        help='Minimum space for alert',
        nargs=1,
        default=DefaultLowSpaceSize
    )
    args = parser.parse_args()
    verboseout = args.verbose
    print_lowdisk_status(verboseout, args.size[0])
