import argparse
from dictionary import latin_script


def permutate(domain, tld):
    res = []
    for i,char in enumerate(domain):
        prefix = domain[:i]
        suffix = domain[i+1:]
        for perchar in latin_script[char]:
            res.append(prefix + perchar + suffix + tld)
    return ','.join(res)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('domain')
    parser.add_argument('tld')
    args = parser.parse_args()
    print(permutate(args.domain, args.tld))


if __name__ == '__main__':
    main()
