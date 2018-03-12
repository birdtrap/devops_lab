#!/usr/bin/env python
"""SYSTEM MONITOR"""
# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods
# pylint: disable=line-too-long
# pylint: disable=too-many-instance-attributes
from datetime import datetime
import json
import time
import psutil
import conf


class SNAPSHOT:
    """ class snapshot """
    SNAP_COUNT = 1

    def __init__(self):
        """init"""
        self.NUMBER = None
        self.TIME = None
        self.CPU_USE = None
        self.MEM_USE = None
        self.VMEM_USE = None
        self.DISKR_USE = None
        self.DISKW_USE = None
        self.NET_USE = None

    def renew(self):
        """renew"""
        self.NUMBER = SNAPSHOT.SNAP_COUNT
        self.TIME = str(datetime.now())
        self.CPU_USE = str(psutil.cpu_percent())
        self.MEM_USE = str(psutil.swap_memory().used)
        self.VMEM_USE = str(psutil.virtual_memory().used)
        self.DISKR_USE = str(psutil.disk_io_counters().read_count)
        self.DISKW_USE = str(psutil.disk_io_counters().write_count)
        self.NET_USE = str(psutil.net_io_counters().bytes_sent)
        SNAPSHOT.SNAP_COUNT += 1


SNAP = SNAPSHOT()


def SNAP_STRING_TRANSFORM(MY_SNAP):
    """string transform"""
    OUT_STR = str('SNAPSHOT {:>2}: {} :{:>15}{:>15}{:>15}{:>15}{:>15}{:>15}'.format(MY_SNAP.NUMBER, MY_SNAP.TIME[:19], MY_SNAP.CPU_USE, MY_SNAP.MEM_USE, MY_SNAP.VMEM_USE, MY_SNAP.DISKR_USE, MY_SNAP.DISKW_USE, MY_SNAP.NET_USE))
    return OUT_STR


def FILE_TXT(MY_SNAP):
    """file txt"""
    FI = open("output.txt", "a+")
    FI.write(SNAP_STRING_TRANSFORM(MY_SNAP))
    FI.write('\n')
    FI.close()


def SNAP_DICTIONARY_TRANSFORM(MY_SNAP):
    """dict transform"""
    SNAP_DICTIONARY = {'Number': str(MY_SNAP.NUMBER),
                       'Timestamp': str(MY_SNAP.TIME),
                       'CPU_usage': str(MY_SNAP.CPU_USE),
                       'Mem_usage': str(MY_SNAP.MEM_USE),
                       'Virt_mem_usage': str(MY_SNAP.VMEM_USE),
                       'Disk_read': str(MY_SNAP.DISKR_USE),
                       'Disk_write': str(MY_SNAP.DISKW_USE),
                       'Net_usage': str(MY_SNAP.NET_USE)}
    return SNAP_DICTIONARY


def FILE_JSON(MY_SNAP):
    """file json"""
    FI = open("output.json", "a+")
    json.dump(SNAP_DICTIONARY_TRANSFORM(MY_SNAP), FI, indent=2, ensure_ascii=False)
    FI.close()


FI = open("output.txt", "w+")
FI.write('NUMBER       |TIMESTAMP              |CPU_LOAD_IN_%	   |MEM_USAGE  |VMEM_USAGE        |IO_READ        |IO_WRITE    |NET_USE             \n')
FI.close()

FI = open("output.json", "w+")
FI.close()


for i in range(conf.itteration_number):
    SNAP.renew()
    if conf.out_type == "txt":
        FILE_TXT(SNAP)
    elif conf.out_type == "json":
        FILE_JSON(SNAP)
    else:
        break
    time.sleep(conf.interval)
