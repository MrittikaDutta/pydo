"""
Example: List all Droplets and their IPv4 addresses
Requires: DIGITALOCEAN_TOKEN environment variable
"""

import os
from pydo import Client

client = Client(token=os.getenv("DIGITALOCEAN_TOKEN"))

droplets = client.droplets.list()["droplets"]

for d in droplets:
    ip_info = d["networks"]["v4"][0]["ip_address"]
    print(f"{d['name']} → {ip_info}")
