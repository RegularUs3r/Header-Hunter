#!/usr/bin/env python3

from helpers.requester import requester
import asyncio
from colorama import Fore

def http_builder(targett,  header, proxy, raw, path_list, security_headers, banner):
    if targett:
        if not targett.startswith("http"):
            print(Fore.RED + "[!] Target string missing protocol -1 " + Fore.RESET)
        else:
            asyncio.run(requester(targett,  header, proxy, raw, path_list, security_headers, banner))
    else:
        print(Fore.RED + "[!] Missing target string" - Fore.RESET)
