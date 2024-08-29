#!/usr/bin/env python3


from helpers.header_stuff import *
from helpers.out import *
from colorama import Fore



def judger(headers, api, wordlist, output):
    if wordlist is not None:
        for information in disclosure:
            for header in headers:
                if headers[f"{header}"]:
                    if header.lower() == information.lower():
                        not_empty.append(header)
        
        if output:
            if not_empty:
                f = open("output-headers.txt", "a")
                f.write("                              " + "\n")
                info_disclosure = (Fore.YELLOW+"[Banner Disclosure]"+Fore.RESET)
                f.write(info_disclosure + "\n")
                f.close()
                not_empty.clear()
            
            for information in disclosure:
                for header in headers:
                    if header.lower() == information.lower():
                        if headers[f"{header}"]:
                            if headers[f"{header}"]:
                                f = open("output-headers.txt", "a")
                                banner_disc = (Fore.YELLOW+"[!]"+Fore.RESET+f" - {Fore.WHITE+header+Fore.RESET}:",Fore.YELLOW+headers[f"{header}"]+Fore.RESET)                 
                                banner_disclosure = (''.join(banner_disc))
                                f.write(banner_disclosure + "\n")
                                f.close()
            if api is not None:
                for must_have in mind_headers_api:
                    if must_have not in headers:
                        missing.append(must_have)
                    else:
                        pass
                out(wordlist, output)
            else:
                for must_have in mind_headers_html:
                    if must_have not in headers:
                        missing.append(must_have)
                    else:
                        pass
                out(wordlist)
        else:
            if not_empty:
                print("")
                print(Fore.YELLOW+"[Banner Disclosure]"+Fore.RESET)
                not_empty.clear()
            
            for information in disclosure:
                for header in headers:
                    if header.lower() == information.lower():
                        if headers[f"{header}"]:
                            if headers[f"{header}"]:
                                print(Fore.YELLOW+"[!]"+Fore.RESET+f" - {Fore.WHITE+header+Fore.RESET}:",Fore.YELLOW+headers[f"{header}"]+Fore.RESET)                 
            if api is not None:
                for must_have in mind_headers_api:
                    if must_have not in headers:
                        missing.append(must_have)
                    else:
                        pass
                out(wordlist, output)
            else:
                for must_have in mind_headers_html:
                    if must_have not in headers:
                        missing.append(must_have)
                    else:
                        pass
                out(wordlist)
    elif wordlist is None:
        print("")        
        for information in disclosure:
            for header in headers:
                if headers[f"{header}"]:
                    if header.lower() == information.lower():
                        not_empty.append(header)
        if not_empty:
            print("")
            print(Fore.YELLOW+"[Banner Disclosure]"+Fore.RESET)
            not_empty.clear()

        for information in disclosure:
            for header in headers:
                if header.lower() == information.lower():
                    if headers[f"{header}"]:
                        print(Fore.YELLOW+"[!]"+Fore.RESET+f" - {Fore.WHITE+header+Fore.RESET}:",Fore.YELLOW+headers[f"{header}"]+Fore.RESET)    
        if api == True:
            for must_have in mind_headers_api:
                if must_have not in headers:
                    missing.append(must_have)
                else:
                    pass
            out(wordlist, output)
        elif api is False:
            for must_have in mind_headers_html:
                if must_have not in headers:
                    missing.append(must_have)
                else:
                    pass
            out(wordlist, output)
