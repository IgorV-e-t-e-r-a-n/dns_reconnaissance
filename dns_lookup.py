from dnslib import DNSRecord, QTYPE
import socket  # For Reverse DNS lookups

# Dictionary to store discovered domains and their associated IPs
domains = {}

# File containing subdomains to search
subs = ["www", "mail", "ftp", "ns1", "ns2", "admin", "webmail", "smtp", "pop", "imap", 
    "secure", "server", "vpn", "blog", "cpanel", "whm", "autodiscover", "m", 
    "portal", "webdisk", "api", "status", "test", "dev", "staging", "shop", 
    "store", "forum", "support", "help", "docs", "wiki", "login", "db", "mysql", 
    "beta", "demo", "cdn", "download", "proxy", "vpn", "remote", "office", "erp", 
    "crm", "billing", "account", "exchange", "owa"
]

# Google's public DNS server
dns_server = "8.8.8.8"
dns_port = 53

# Domain to search for subdomains
domain = "google.com"
nums = True  # Enable numeric subdomain variations

def ReverseDNS(ip):
    """
    Performs a reverse DNS lookup to find the domain name associated with an IP address.
    """
    try:
        result = socket.gethostbyaddr(ip)
        return [result[0]] + result[1]  # Returns the hostname and alias list
    except socket.herror:
        return []  # Returns an empty list if no reverse lookup found

def DNSRequest(domain):
    """
    Sends a DNS A-record query to resolve a domain to IP addresses.
    Also performs reverse DNS lookup on each resolved IP.
    """
    ips = []  # List to store resolved IP addresses

    try:
        query = DNSRecord.question(domain, QTYPE.A)  # Create A record query
        response = query.send(dns_server, dns_port, timeout=2)  # Send query
        reply = DNSRecord.parse(response)  # Parse response

        addresses = [str(rr.rdata) for rr in reply.rr if rr.rtype == QTYPE.A]  # Extract IPs

        if addresses:
            # Store discovered IPs under the domain key
            domains[domain] = list(set(domains.get(domain, []) + addresses))

            # Perform reverse DNS lookup on each IP address
            for a in addresses:
                rd = ReverseDNS(a)
                for d in rd:
                    if d not in domains:
                        domains[d] = [a]
                        DNSRequest(d)  # Recursively resolve subdomains
                    else:
                        domains[d].append(a)

    except Exception as e:
        print(f"Failed to resolve {domain}: {e}")
        return []

    return ips

def HostSearch(domain, dictionary, nums):
    """
    Searches for subdomains using a given wordlist and optional numeric variations.
    """
    for word in dictionary:
        d = word + "." + domain  # Construct subdomain (e.g., "blog.example.com")
        DNSRequest(d)  # Perform DNS query on the subdomain

        if nums:
            for i in range(10):  # Add numeric variations (e.g., "test1.example.com")
                d = word + str(i) + "." + domain
                DNSRequest(d)

# Read subdomains from the file

# Perform subdomain enumeration
HostSearch(domain, subs, nums)

# Print discovered domains and their associated IP addresses
for domain in domains:
    print(f"{domain}: {domains[domain]}")
