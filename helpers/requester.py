#!/usr/bin/env python3

from helpers.header_stuff import *
from colorama import Fore
from helpers.court import judger
import requests, httpx, asyncio, sys, os
from urllib3 import disable_warnings
disable_warnings()


async def requester(targett,  header, proxy, raw, path_list, security_headers, banner):
    url = targett
    if header is not None:
        for items in header:
            param_name, param_value = items.split(": ")
            custom_headers[param_name] = param_value
    if proxy:
        proxy1, proxy2 = {"https://": proxy}, {"https": proxy}
    else:
        proxy1, proxy2 = None, None
    
    client = httpx.AsyncClient(http2=True, verify=False, proxies=proxy)
    if security_headers:
        if path_list: 
            print(f"[•] IN SCOPE ASSET - [{targett}]")
            f = open(path_list, "r")
            for paths in f:
                path = paths.strip()    
                try:
                    r = await client.get(url+path, headers=custom_headers, follow_redirects=True, timeout=10)
                    print(f"[+] REQUESTED PATH - [{r.url}]")
                    headers = r.headers
                    for head, value in zip(headers, headers.values()):
                        all_headers[head] = value
                except httpx.RemoteProtocolError:
                    try:
                        r = requests.get(url+path, proxies=proxy2, headers=custom_headers,  verify=False, allow_redirects=True, timeout=10)
                        print(f"[+] REQUESTED PATH - [{r.url}]")
                        headers = r.headers
                        for head, value in zip(headers, headers.values()):
                            all_headers[head] = value
                    except requests.exceptions.ConnectionError as errc:
                        print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
                        print(Fore.RED+f"[-] ERROR [{errc}]"+Fore.RESET)
                        print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        print(exc_type, fname, exc_tb.tb_lineno)
                except httpx.ConnectError:
                    r = await client.get(url+path, headers=custom_headers, follow_redirects=True, timeout=10)
                    headers = r.headers
                    for head, value in zip(headers, headers.values()):
                        all_headers[head] = value
                except requests.exceptions.ConnectionError as e:
                    print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
                    print(Fore.RED+f"[-] ERROR {e}"+Fore.RESET)
                    print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
                except httpx.ConnectTimeout as e:
                    print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
                    print(Fore.RED+f"[-] ERROR {e}"+Fore.RESET)
                    print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
                except httpx.ReadTimeout as e:
                    print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
                    print(Fore.RED+f"[-] ERROR {e}"+Fore.RESET)
                    print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
            print("")
            print(f"[▼] IN USE HEADERS - [{targett}]")
            
            for header, value in zip(all_headers.keys(), all_headers.values()):
                print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")

            for header_html in mind_headers_html:
                if header_html not in all_headers:
                    missing.append(header_html)
            if missing:
                print("")
                print(Fore.RED+"[Missing Security Headers]"+Fore.RESET)
            
            for miss in missing:
                print(Fore.RED+"[x]"+Fore.RESET+f" - {Fore.WHITE+miss+Fore.RESET}")
        
        else:
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
                    
                    if raw is True:
                        print(f"[▼] RAW CONTENT - [{r.url}]")
                        print(Fore.WHITE+f"HTTP/{r.raw.version / 10} {r.reason} {r.status_code}")
                        for header, value in zip(headers, headers.values()):
                            print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
                        print("")
                except requests.exceptions.ConnectionError as errc:
                    print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
                    print(Fore.RED+f"[-] ERROR [{errc}]"+Fore.RESET)
                    print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
            except httpx.ConnectError:
                r = await client.get(url, headers=custom_headers, follow_redirects=True, timeout=10)
                headers = r.headers
                if r.url != targett:
                    print(f"[»] REDIRECTION - [{r.url}]")
                else:
                    print(f"[-] NO REDIRECT - [{r.url}]")
                if raw is True:
                    print("")
                    print(f"[▼] RAW CONTENT - [{r.url}]")
                    print(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+Fore.RESET)
                    for header, value in zip(headers, headers.values()):
                        print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
                    print("")
            except requests.exceptions.ConnectionError as e:
                print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
                print(Fore.RED+f"[-] ERROR {e}"+Fore.RESET)
                print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
            except httpx.ConnectTimeout as e:
                print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
                print(Fore.RED+f"[-] ERROR {e}"+Fore.RESET)
                print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
            
            for header_html in mind_headers_html:
                if header_html.lower() not in headers:
                    missing.append(header_html)
            if missing:
                print("")
                print(Fore.RED+"[Missing Security Headers]"+Fore.RESET)
            
            for miss in missing:
                print(Fore.RED+"[x]"+Fore.RESET+f" - {Fore.WHITE+miss+Fore.RESET}")
    elif banner:
        if path_list:
            print(f"[•] IN SCOPE ASSET - [{targett}]")
            f = open(path_list, "r")
            for paths in f:
                path = paths.strip()    
                client = httpx.AsyncClient(http2=True, verify=False, proxies=proxy)
                try:
                    r = await client.get(url+path, headers=custom_headers, follow_redirects=True, timeout=10)
                    print(f"[+] REQUESTED PATH - [{r.url}]")
                    headers = r.headers
                    for head, value in zip(headers, headers.values()):
                        all_headers[head] = value
                except httpx.RemoteProtocolError:
                    try:
                        r = requests.get(url+path, proxies=proxy2, headers=custom_headers,  verify=False, allow_redirects=True, timeout=10)
                        print(f"[+] REQUESTED PATH - [{r.url}]")
                        headers = r.headers
                        for head, value in zip(headers, headers.values()):
                            all_headers[head] = value
                    except requests.exceptions.ConnectionError as errc:
                        print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
                        print(Fore.RED+f"[-] ERROR [{errc}]"+Fore.RESET)
                        print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        print(exc_type, fname, exc_tb.tb_lineno)
                except httpx.ConnectError:
                    r = await client.get(url+path, headers=custom_headers, follow_redirects=True, timeout=10)
                    headers = r.headers
                    for head, value in zip(headers, headers.values()):
                        all_headers[head] = value
                except requests.exceptions.ConnectionError as e:
                    print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
                    print(Fore.RED+f"[-] ERROR {e}"+Fore.RESET)
                    print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
                except httpx.ConnectTimeout as e:
                    print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
                    print(Fore.RED+f"[-] ERROR {e}"+Fore.RESET)
                    print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
                except httpx.ReadTimeout as e:
                    print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
                    print(Fore.RED+f"[-] ERROR {e}"+Fore.RESET)
                    print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
            
                for header, value in zip(all_headers.keys(), all_headers.values()):
                    print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
        else:
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
                    
                    if raw is True:
                        print(f"[▼] RAW CONTENT - [{r.url}]")
                        print(Fore.WHITE+f"HTTP/{r.raw.version / 10} {r.reason} {r.status_code}")
                        for header, value in zip(headers, headers.values()):
                            print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
                        print("")
                except requests.exceptions.ConnectionError as errc:
                    print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
                    print(Fore.RED+f"[-] ERROR [{errc}]"+Fore.RESET)
                    print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
            except httpx.ConnectError:
                r = await client.get(url, headers=custom_headers, follow_redirects=True, timeout=10)
                headers = r.headers
                if r.url != targett:
                    print(f"[»] REDIRECTION - [{r.url}]")
                else:
                    print(f"[-] NO REDIRECT - [{r.url}]")
                if raw is True:
                    print("")
                    print(f"[▼] RAW CONTENT - [{r.url}]")
                    print(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+Fore.RESET)
                    for header, value in zip(headers, headers.values()):
                        print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
                    print("")
            except requests.exceptions.ConnectionError as e:
                print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
                print(Fore.RED+f"[-] ERROR {e}"+Fore.RESET)
                print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
            except httpx.ConnectTimeout as e:
                print(Fore.RED+f"[-] Host [{targett}] errored out"+ Fore.RESET)
                print(Fore.RED+f"[-] ERROR {e}"+Fore.RESET)
                print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
            
        
            print("")
            print(Fore.YELLOW+"[Banner Disclosure]"+Fore.RESET)
            for information in disclosure:
                for header in headers:
                    if header.lower() == information.lower():
                        if headers[f"{header}"]:
                            result = header+": "+headers[f"{header}"]
                            print(Fore.YELLOW+"[!]"+Fore.RESET+f" - {Fore.WHITE+header+Fore.RESET}:",Fore.YELLOW+headers[f"{header}"]+Fore.RESET)
                    # else:
                    #     print(header)
    
    # client = httpx.AsyncClient(http2=True, verify=False, proxies=proxy)
    #     print("")
    #     print(f"[•] BASE TARGET - [{targett}]")
    #     try:
    #         r = await client.get(url, headers=custom_headers, follow_redirects=True, timeout=10)
    #         headers = r.headers
    #         if r.url != targett:
    #             print(f"[»] REDIRECTION - [{r.url}]")
    #         else:
    #             print(f"[-] NO REDIRECT - [{r.url}]")
    #         headers = r.headers
    #         if raw is True:
    #             print("")
    #             print(f"[▼] RAW CONTENT - [{r.url}]")
    #             print(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+Fore.RESET)
    #             for header, value in zip(headers, headers.values()):
    #                 print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
    #             print("")
    #         judger(headers, api, wordlist, output)
    #     except httpx.RemoteProtocolError:
    #         try:
    #             r = requests.get(url, proxies=proxy2, headers=custom_headers,  verify=False, allow_redirects=True, timeout=10)
    #             headers = r.headers
    #             if r.url != targett:
    #                 print(f"[»] REDIRECTION - [{r.url}]")
    #             else:
    #                 print(f"[-] NO REDIRECT - [{r.url}]")
    #             headers = r.headers
                
    #             if raw is True:
    #                 print(f"[▼] RAW CONTENT - [{r.url}]")
    #                 print(Fore.WHITE+f"HTTP/{r.raw.version / 10} {r.reason} {r.status_code}")
    #                 for header, value in zip(headers, headers.values()):
    #                     print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
    #                 print("")
    #             judger(headers, api, wordlist, output)
    #         except requests.exceptions.ConnectionError as errc:
    #             print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
    #             print(Fore.RED+f"[-] ERROR [{errc}]"+Fore.RESET)
    #             print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
    #             exc_type, exc_obj, exc_tb = sys.exc_info()
    #             fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #             print(exc_type, fname, exc_tb.tb_lineno)
    #     except httpx.ConnectError:
    #         r = await client.get(url, headers=custom_headers, follow_redirects=True, timeout=10)
    #         headers = r.headers
    #         if r.url != targett:
    #             print(f"[»] REDIRECTION - [{r.url}]")
    #         else:
    #             print(f"[-] NO REDIRECT - [{r.url}]")
    #         if raw is True:
    #             print("")
    #             print(f"[▼] RAW CONTENT - [{r.url}]")
    #             print(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+Fore.RESET)
    #             for header, value in zip(headers, headers.values()):
    #                 print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
    #             print("")
    #         judger(headers, api, wordlist, output)
    #     except requests.exceptions.ConnectionError as e:
    #         print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
    #         print(Fore.RED+f"[-] ERROR {e}"+Fore.RESET)
    #         print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
    #         exc_type, exc_obj, exc_tb = sys.exc_info()
    #         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #         print(exc_type, fname, exc_tb.tb_lineno)
    #     except httpx.ConnectTimeout as e:
    #         print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
    #         print(Fore.RED+f"[-] ERROR {e}"+Fore.RESET)
    #         print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
    #         exc_type, exc_obj, exc_tb = sys.exc_info()
    #         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #         print(exc_type, fname, exc_tb.tb_lineno)
    #     if proxy:
    #         proxy1, proxy2 = {"https://": proxy}, {"https": proxy}
    #     else:
    #         proxy1, proxy2 = None, None
    
    
    
    #         print("AQUI AQUI AQUI AQUI")        
    #         try:
    #             if proxy:
    #                 proxy1, proxy2 = {"https://": proxy}, {"https": proxy}
    #             else:
    #                 proxy1, proxy2 = None, None
    #             client = httpx.AsyncClient(http2=True, verify=False, proxies=proxy1)
    #             print("")
    #             print(f"[•] BASE TARGET - [{targett}]")
    #             try:
    #                 r = await client.get(url, headers=custom_headers, follow_redirects=True, timeout=10)
    #                 headers = r.headers
    #                 if r.url != targett:
    #                     print(f"[»] REDIRECTION - [{r.url}]")
    #                 else:
    #                     print(f"[-] NO REDIRECT - [{r.url}]")
    #                 if raw is True:
    #                     print("")
    #                     print(f"[▼] RAW CONTENT - [{r.url}]")
    #                     print(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+Fore.RESET)
    #                     for header, value in zip(headers, headers.values()):
    #                         print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
    #                     print("")
    #                 judger(headers, api, wordlist, output)
    #             except httpx.RemoteProtocolError:
    #                 try:
    #                     r = requests.get(url, proxies=proxy2, headers=custom_headers,  verify=False, allow_redirects=True, timeout=10)
    #                     headers = r.headers
    #                     if r.url != targett:
    #                         print(f"[»] REDIRECTION - [{r.url}]")
    #                     else:
    #                         print(f"[-] NO REDIRECT - [{r.url}]")
    #                     headers = r.headers
                        
    #                     if raw is True:
    #                         print(f"[▼] RAW CONTENT - [{r.url}]")
    #                         print(Fore.WHITE+f"HTTP/{r.raw.version / 10} {r.reason} {r.status_code}")
    #                         for header, value in zip(headers, headers.values()):
    #                             print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
    #                         print("")
    #                     judger(headers, api, wordlist, output)
    #                 except requests.exceptions.ConnectionError as errc:
    #                     print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
    #                     print(Fore.RED+f"[-] ERROR [{errc}]"+Fore.RESET)
    #                     print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
    #                     exc_type, exc_obj, exc_tb = sys.exc_info()
    #                     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #                     print(exc_type, fname, exc_tb.tb_lineno)
    #             except httpx.ConnectError:
    #                 r = await client.get(url, headers=custom_headers, follow_redirects=True, timeout=10)
    #                 headers = r.headers
    #                 if r.url != targett:
    #                     print(f"[»] REDIRECTION - [{r.url}]")
    #                 else:
    #                     print(f"[-] NO REDIRECT - [{r.url}]")
    #                 if raw is True:
    #                     print("")
    #                     print(f"[▼] RAW CONTENT - [{r.url}]")
    #                     print(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+Fore.RESET)
    #                     for header, value in zip(headers, headers.values()):
    #                         print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
    #                     print("")
    #                 judger(headers, api, wordlist, output)
    #             except requests.exceptions.ConnectionError as e:
    #                 print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
    #                 print(Fore.RED+f"[-] ERROR {e}"+Fore.RESET)
    #                 print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
    #                 exc_type, exc_obj, exc_tb = sys.exc_info()
    #                 fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #                 print(exc_type, fname, exc_tb.tb_lineno)
    #             except httpx.ConnectTimeout as e:
    #                 print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
    #                 print(Fore.RED+f"[-] ERROR {e}"+Fore.RESET)
    #                 print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
    #                 exc_type, exc_obj, exc_tb = sys.exc_info()
    #                 fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #                 print(exc_type, fname, exc_tb.tb_lineno)
    #         except UnboundLocalError:
    #             r = await client.get(url, headers=custom_headers, follow_redirects=True, timeout=10)
    #             headers = r.headers
    #             if r.url != targett:
    #                 print(f"[»] REDIRECTION - [{r.url}]")
    #             else:
    #                 print(f"[-] NO REDIRECT - [{r.url}]")
    #             if raw is True:
    #                 print("")
    #                 print(f"[▼] RAW CONTENT - [{r.url}]")
    #                 print(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+Fore.RESET)
    #                 for header, value in zip(headers, headers.values()):
    #                     print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
    #                 print("")
    #             judger(headers, api, wordlist, output)
    #         except httpx.RemoteProtocolError:
    #             try:
    #                 r = requests.get(url, proxies=proxy2, headers=custom_headers,  verify=False, allow_redirects=True, timeout=10)
    #                 headers = r.headers
    #                 if r.url != targett:
    #                     print(f"[»] REDIRECTION - [{r.url}]")
    #                 else:
    #                     print(f"[-] NO REDIRECT - [{r.url}]")
                    
    #                 if raw is True:
    #                     print(f"[▼] RAW CONTENT - [{r.url}]")
    #                     print(Fore.WHITE+f"HTTP/{r.raw.version / 10} {r.reason} {r.status_code}")
    #                     for header, value in zip(headers, headers.values()):
    #                         print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
    #                     print("")
    #                 judger(headers, api, wordlist, output)
    #             except requests.exceptions.ConnectionError as errc:
    #                 print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
    #                 print(Fore.RED+f"[-] ERROR {e}"+Fore.RESET)
    #                 print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
    #                 exc_type, exc_obj, exc_tb = sys.exc_info()
    #                 fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #                 print(exc_type, fname, exc_tb.tb_lineno)
    #         except httpx.ConnectError:
    #             r = await client.get(url, headers=custom_headers, follow_redirects=True, timeout=10)
    #             headers = r.headers
    #             if r.url != targett:
    #                 print(f"[»] REDIRECTION - [{r.url}]")
    #             else:
    #                 print(f"[-] NO REDIRECT - [{r.url}]")
    #             if raw is True:
    #                 print("")
    #                 print(f"[▼] RAW CONTENT - [{r.url}]")
    #                 print(Fore.WHITE+f"{r.http_version} {r.reason_phrase} {r.status_code}"+Fore.RESET)
    #                 for header, value in zip(headers, headers.values()):
    #                     print(f"{Fore.WHITE+header+Fore.RESET}: {Fore.GREEN+value+Fore.RESET}")
    #                 print("")
    #             judger(headers, api, wordlist, output)
    #         except requests.exceptions.ConnectionError:
    #             print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
    #             print(Fore.RED+f"[-] ERROR {e}"+Fore.RESET)
    #             print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
    #             exc_type, exc_obj, exc_tb = sys.exc_info()
    #             fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #             print(exc_type, fname, exc_tb.tb_lineno)
    #         except httpx.ConnectTimeout:
    #             print(Fore.RED+f"[-] Host [{targett}] errored out"+Fore.RESET)
    #             print(Fore.RED+f"[-] ERROR {e}"+Fore.RESET)
    #             print(Fore.GREEN+"[*] Consider proxing it!"+Fore.RESET)
    #             exc_type, exc_obj, exc_tb = sys.exc_info()
    #             fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #             print(exc_type, fname, exc_tb.tb_lineno)
