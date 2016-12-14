import json
import sys

import requests

API_BASE_URL = 'https://api.github.com/'

def get_file_contents(filename):
    with open(filename) as f:
        return f.read()

def get_filename_parameter():
    if len(sys.argv) > 1:
        return sys.argv[1]

def main():
    # Put your code logic here
    print('Replace me!')

if __name__ == '__main__':
    main()
