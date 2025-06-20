#!/usr/bin/env python3



import argparse
from progress.bar import Bar
from helpers.requester import requester
from helpers.http_builder import http_builder
from helpers.header_stuff import on_the_fly
from colorama import Fore

blah = {}
parser = argparse.ArgumentParser()

parser.add_argument("-H", "--header", metavar="", action="append", help="Add custom header")
parser.add_argument("-x", "--proxy", metavar="", help="Proxy - http://IP:PORT")
parser.add_argument("-sh", "--security-headers", dest="security_headers", action="store_true")
parser.add_argument("-b", "--banner", action="store_true")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-t", "--target", metavar="")
parser.add_argument(" ", nargs="*")
args = parser.parse_args()
target = args.target
header = args.header
proxy = args.proxy
security_headers = args.security_headers
banner = args.banner


def start():
    ORANGE = '\33[33m'
    NC = '\033[0m'
    # print(Fore.BLUE +"Created By: " + Fore.RESET + ORANGE + "RegularUs3r | https://github.com/regularus3r" + NC)
    targett = target
    http_builder(targett,  header, proxy, security_headers, banner)

start()
