#!/usr/bin/env python
"""Getting GitHub info"""
# pylint: disable=invalid-name
# pylint: disable=line-too-long

import argparse
import getpass
import requests


def print_info(out_info):
    """print git statistics"""
    U_NAME = str(input("Please enter Git user name: "))
    F_NAME = str(input("Please enter Git repository: "))
    Y_NAME = str(input("Please enter your Git name: "))
    PASS = getpass.getpass(prompt="And your Git password: ")
# U_NAME = str('alenaPy')
# F_NAME= str('devops_lab')

    ADDR_PARTS = ['https://api.github.com/repos', '', '', '']
    ADDR_PARTS[1] = U_NAME
    ADDR_PARTS[2] = F_NAME
    ADDR_PARTS[3] = str('pulls')
    GIT_ADDR = '/'

# GIT_ADDR = str('https://api.github.com/repos/alenaPy/devops_lab/pulls')
    GIT_PULL = requests.get(GIT_ADDR.join(ADDR_PARTS), auth=(Y_NAME, PASS))
# print(json.dumps(GIT_PULL.json(), sort_keys = True, indent = 4, ensure_ascii = False))

    GIT_DICT = GIT_PULL.json()

    if out_info == 'forks':
        print(GIT_DICT[0].get("base").get("repo").get("forks_count"))
    elif out_info == 'name':
        for i in range(15):
            print(GIT_DICT[i].get("head").get("repo").get("full_name"))
    elif out_info == 'usr':
        for i in range(15):
            print(GIT_DICT[i].get("head").get("user").get("login"))
    elif out_info == 'date':
        print(GIT_DICT[0].get("base").get("repo").get("created_at"))
    else:
        print("Sorry, this parametr doesn't exist. Please read --help")


def print_vers():
    """print version"""
    print('GitHubInformer 1.0')


parser = argparse.ArgumentParser()
parser.add_argument("-g", type=print_info, action="store", help="Back Git info. \n Use '-g forks' for getting numder of forks. \n Use '-g usr' for getting last 15 names in pull. \n Use '-g date' for getting creation date. \n Use '-g name' for getting full names last 15 users")
parser.add_argument("-v", action="store_true", help="Info about version")
args = parser.parse_args()
if args.v:
    print_vers()
