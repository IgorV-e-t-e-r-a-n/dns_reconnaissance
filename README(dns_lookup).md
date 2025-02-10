# DNS lookup

## Overview
This script performs DNS enumeration by resolving subdomains and performing reverse DNS lookups to discover associated IP addresses. It utilizes the `dnslib` library for querying DNS records.

## Features
- **Subdomain Enumeration**: Checks for common subdomains from a predefined list.
- **Reverse DNS Lookup**: Resolves IP addresses back to hostnames.
- **Custom DNS Server**: Queries a specified DNS resolver (default: Google 8.8.8.8).
- **Wildcard Support**: Appends numbers to subdomains for exhaustive searches.

## Requirements
- Python 3.x
- `dnslib` library

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/IgorV-e-t-e-r-a-n/dns_reconnaissance.git
   cd dns_reconnaissance

  Install dependencies:

    pip install dnslib

  Ensure "subs" list contains a list of common subdomains.

## Usage

Run the script with:

python dns_enum.py

Configuration
    - **Modify the "subs" list to include additional subdomains.**
    - **Change the resolver setting to query a different DNS server.**

Example Output

www.example.com: 192.168.1.1
mail.example.com: 192.168.1.2
ftp.example.com: 192.168.1.3

Roadmap
    - **Add multi-threading for faster resolution.**
    - **Support for additional DNS record types (MX, TXT, etc.).**
    - **Integration with OSINT tools.**
