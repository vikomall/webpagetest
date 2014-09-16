import argparse
import re
import requests


def check_webpagetest(args):
    """Verify that WebPagetest is properly installed"""
    server_ip = getattr(args, 'server_ip')
    url = "http://" + server_ip
    try:
        r = requests.get(url)
        if re.search('Website Performance and Optimization Test', r.content):
            return True
        else:
            return False
    except:
        return False


parser = argparse.ArgumentParser()
parser.add_argument("server_ip", type=str, help="IP of the server to test")
args = parser.parse_args()

assert check_webpagetest(args), "WebPagetest is not properly installed"
