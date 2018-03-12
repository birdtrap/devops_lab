#!/usr/bin/env python
"""python info"""
# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods
# pylint: disable=line-too-long
# pylint: disable=too-many-instance-attributes
import os
import json
import sys
import site
import pip
import yaml


def get_inst_pack():
    """inst_pack"""
    inst_pack_list = pip.get_installed_distributions()
    installed_packages = []
    for i in range(len(inst_pack_list)):
        installed_packages.append(str(inst_pack_list[i]))
    return installed_packages


def py_info_dict():
    """info dictionary"""
    info_dict = {'version': str(sys.version),
                 'name': str(os.path.basename(sys.exec_prefix)),
                 'python_executable_location': str(sys.executable),
                 'pip_location': str(pip.__path__),
                 'PYTHONPATH': str(sys.path),
                 'installed_packages': get_inst_pack(),
                 'site-packages_location': str(site.getsitepackages())}
    return info_dict


def wr_json():
    """write json"""
    FI = open("py_info.json", "w+")
    json.dump(py_info_dict(), FI, indent=2, ensure_ascii=False)
    FI.close()


def wr_yaml():
    """write yaml"""
    FI = open("py_info.yml", "w+")
    yaml.dump(py_info_dict(), FI, default_flow_style=False)
    FI.close()


wr_json()
wr_yaml()
