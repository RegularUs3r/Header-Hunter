#!/usr/bin/env python3

from helpers.header_stuff import *
from colorama import Fore
from helpers.court import judger
import requests, httpx, asyncio, sys, os
from urllib3 import disable_warnings



def handlerOne(targett, errc):
    print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
    print(Fore.RED+f"[-] ERROR [{errc}]"+Fore.RESET)
    print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)


def handlerTwo(targett, e):
    print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
    print(Fore.RED+f"[-] ERROR {e}"+Fore.RESET)
    print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)