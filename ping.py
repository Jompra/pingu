import requests

filename = open('site-to-ping.txt', 'r')

sites = filename.read().split('\n')[:-1]
sites.remove('')

for site in sites:
  requests.get(site)
