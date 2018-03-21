import argparse
from dictionary import latin_script


def permutate(domain, tld, punycode=False):
    res = []
    for i,char in enumerate(domain):
        prefix = domain[:i]
        suffix = domain[i+1:]
        if char in latin_script:
            for perchar in latin_script[char]:
                new_domain_name = prefix + perchar + suffix + tld
                if punycode:
                    new_domain_name = str(new_domain_name.encode('idna'), 'utf-8')
                res.append(new_domain_name)

    return ','.join(res)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('domain')
    parser.add_argument('tld')
    parser.add_argument('--punycode', default=False, action='store_true')
    args = parser.parse_args()
    print(permutate(args.domain, args.tld, punycode=args.punycode))


if __name__ == '__main__':
    main()
