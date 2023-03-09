import argparse, dns.resolver


def lookup(name):
    # IPv4, CNAME, IPv6, DNS, MAIL
    for qtype in 'A', 'CNAME', 'AAAA', 'MX', 'NS':
        answer = dns.resolver.query(name, qtype, raise_on_no_answer=False)
        if answer.rrset is not None:
            print(answer.rrset)


if __name__ == '__main__':
    parse = argparse.ArgumentParser(description='Resolve a name using DNS')
    parse.add_argument('name', help='name that you want to look up in DNS')
    lookup(parse.parse_args().name)

    # pip3 install dnspython3
    # python3 dns_basic.py python.org