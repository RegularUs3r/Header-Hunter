#!/usr/bin/env python3 

from helpers.header_stuff import *
from colorama import Fore

def out(wordlist, output):
    if wordlist is not None:
        if output:
            f = open("output-headers.txt", "a")
            f.write("                              " + "\n")
            f.write(Fore.RED+"[Missing Security Headers]"+Fore.RESET+ "\n")
            f.close()
            for i_miss_you in missing:
                missing_headers = (Fore.RED+"[x]"+Fore.RESET+Fore.WHITE+f" - {i_miss_you}"+Fore.RESET)
                f = open("output-headers.txt", "a")
                f.write(missing_headers + "\n")
            f.write("                              " + "\n")
            f.close()
            missing.clear()

    elif wordlist is None:
        print("")
        print(Fore.RED+"[Missing Security Headers]"+Fore.RESET)
        for i_miss_you in missing:
            print(Fore.RED+"[x]"+Fore.RESET+f" - {Fore.WHITE+i_miss_you+Fore.RESET}")
        missing.clear()
