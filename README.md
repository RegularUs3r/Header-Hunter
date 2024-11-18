# CURRENTLY OUTDATED!!

![Python minimum version](https://img.shields.io/badge/Python-3.10%2B-brightgreen)
# DESCRIPTION
Header hunter is a python script aimed for headers evaluation, whether a certain target has or not all valid security headers

## Features
+ API - You can set it to search for headers an API should have [this option was created based solely on owasp]
+ WORDLIST - Now you can provide a list of targets
+ OUTPUT - You can save the output results to a file
+ RAW - You're able to display the response just like you would get in burp
+ PROXY - Hardly ever you need this, but if you need just proxy it

### :gear: Instalation
      pip3 install virtualenv
      python3 -m venv <your-virtual-env-name>
      cd into it
      clone the repo and...
      pip3 install -r requirements.txt


### :man_technologist: Usage
      usage: HeaderHunter.py [-h] [-H] [-o] [-x] [-api] [-r] (-t  | -w ) [ ...]

      positional arguments:
      
      
      options:
        -h, --help        show this help message and exit
        -H , --header     This is self explaining
        -o, --output      Output results to file
        -x , --proxy      Proxy - http://IP:PORT
        -api, --api       Set it for api
        -r, --raw         Display raw response
        -t , --target
        -w , --wordlist   Provide list of targets      
