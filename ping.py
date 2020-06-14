import requests

filename = open('site-to-ping.txt', 'r')

site = filename.read()

requests.get(site)