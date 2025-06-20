#!/usr/bin/env python3

from helpers.header_stuff import *
from colorama import Fore
from helpers.court import judger
import requests, httpx, asyncio, sys, os
from urllib3 import disable_warnings
from errorhandler import *
disable_warnings()


async def requester(targett,  header, proxy, security_headers, banner):
    url = targett
    if header is not None:
        for items in header:
            param_name, param_value = items.split(": ")
            custom_headers[param_name] = param_value
    if proxy:
        proxy1, proxy2 = {"https://": proxy}, {"https": proxy}
    else:
        proxy1, proxy2 = None, None
    
    client = httpx.AsyncClient(http2=True, verify=False, proxy=proxy)
    if security_headers:
        ###Security Header down bellow
        print(f"[•] BASE TARGET - [{targett}]")
        try:
            r = await client.get(url, headers=custom_headers, follow_redirects=True, timeout=10)
            headers = r.headers
            if r.url != targett:
                print(f"[»] REDIRECTION - [{r.url}]")
            else:
                print(f"[-] NO REDIRECT - [{r.url}]")
            headers = r.headers
            print("")
            print(f"[▼] RAW CONTENT - [{r.url}]")
            print(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+Fore.RESET)
            for header, value in zip(headers, headers.values()):
                print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
            
        except httpx.RemoteProtocolError:
            try:
                r = requests.get(url, proxies=proxy2, headers=custom_headers,  verify=False, allow_redirects=True, timeout=10)
                headers = r.headers
                if r.url != targett:
                    print(f"[»] REDIRECTION - [{r.url}]")
                else:
                    print(f"[-] NO REDIRECT - [{r.url}]")
                headers = r.headers
                
                print(f"[▼] RAW CONTENT - [{r.url}]")
                print(Fore.WHITE+f"HTTP/{r.raw.version / 10} {r.reason} {r.status_code}")
                for header, value in zip(headers, headers.values()):
                    print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
                print("")
            except requests.exceptions.ConnectionError as errc:
                handlerOne(targett, errc)
        except httpx.ConnectError:
            r = await client.get(url, headers=custom_headers, follow_redirects=True, timeout=10)
            headers = r.headers
            if r.url != targett:
                print(f"[»] REDIRECTION - [{r.url}]")
            else:
                print(f"[-] NO REDIRECT - [{r.url}]")
            print("")
            print(f"[▼] RAW CONTENT - [{r.url}]")
            print(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+Fore.RESET)
            for header, value in zip(headers, headers.values()):
                print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
            print("")
        except requests.exceptions.ConnectionError as e:
            handlerTwo(targett, e)
        except httpx.ConnectTimeout as e:
            handlerTwo(targett, e)        
        for header_html in mind_headers_html:
            if header_html.lower() not in headers:
                missing.append(header_html)
        if missing:
            print("")
            print(Fore.RED+"[Missing Security Headers]"+Fore.RESET)
        
        for miss in missing:
            print(Fore.RED+"[x]"+Fore.RESET+f" - {Fore.WHITE+miss+Fore.RESET}")
    elif banner:
        print(f"[•] BASE TARGET - [{targett}]")
        try:
            r = await client.get(url, headers=custom_headers, follow_redirects=True, timeout=10)
            headers = r.headers
            if r.url != targett:
                print(f"[»] REDIRECTION - [{r.url}]")
            else:
                print(f"[-] NO REDIRECT - [{r.url}]")
            headers = r.headers
            
            print("")
            print(f"[▼] RAW CONTENT - [{r.url}]")
            print(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+Fore.RESET)
            for header, value in zip(headers, headers.values()):
                print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
            
        except httpx.RemoteProtocolError:
            try:
                r = requests.get(url, proxies=proxy2, headers=custom_headers,  verify=False, allow_redirects=True, timeout=10)
                headers = r.headers
                if r.url != targett:
                    print(f"[»] REDIRECTION - [{r.url}]")
                else:
                    print(f"[-] NO REDIRECT - [{r.url}]")
                headers = r.headers
                print(f"[▼] RAW CONTENT - [{r.url}]")
                print(Fore.WHITE+f"HTTP/{r.raw.version / 10} {r.reason} {r.status_code}")
                for header, value in zip(headers, headers.values()):
                    print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
                print("")
            except requests.exceptions.ConnectionError as errc:
                handlerOne(targett, errc)
        except httpx.ConnectError:
            r = await client.get(url, headers=custom_headers, follow_redirects=True, timeout=10)
            headers = r.headers
            if r.url != targett:
                print(f"[»] REDIRECTION - [{r.url}]")
            else:
                print(f"[-] NO REDIRECT - [{r.url}]")
            print("")
            print(f"[▼] RAW CONTENT - [{r.url}]")
            print(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+Fore.RESET)
            for header, value in zip(headers, headers.values()):
                print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
            print("")
                
        except requests.exceptions.ConnectionError as e:
            handlerTwo(targett, e)
        except httpx.ConnectTimeout as e:
            handlerTwo(targett, e)            
            # try:
            print("")
            print(Fore.YELLOW+"[Banner Disclosure]"+Fore.RESET)
            for information in disclosure:
                for header in headers:
                    if header.lower() == information.lower():
                        if headers[f"{header}"]:
                            result = header+": "+headers[f"{header}"]
                            print(Fore.YELLOW+"[!]"+Fore.RESET+f" - {Fore.WHITE+header+Fore.RESET}:",Fore.YELLOW+headers[f"{header}"]+Fore.RESET)