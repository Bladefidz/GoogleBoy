#! usr/bin/env python
# -*- coding: utf-8 -*-

# import libraries
import urllib2
import urllib
from bs4 import BeautifulSoup
import re
import sys
import argparse
import os

reload(sys)
sys.setdefaultencoding('utf8')

script_dir = os.path.dirname(__file__)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--keyword', help='Enter keyword')
    parser.add_argument('-R', '--recursive', help='Recursive query')
    return parser.parse_args()


def scrapping_site_google(keyword):
    keyword_ = urllib.quote(keyword)
    g_url = "http://www.google.com/search?q=%s&num=10&hl=en&start=0&nord=1" % (keyword_)
    request = urllib2.Request(g_url)
    request.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0')
    open_url = urllib2.urlopen(request)
    read_url = open_url.read()
    g_soup = BeautifulSoup(read_url)

    remove_tag = re.compile(r'<.*?>')

    # Hasil
    scrap_count = g_soup.find('div', attrs={'id': 'resultStats'})
    count = remove_tag.sub('', str(scrap_count)).replace('.', '')
    # only_count = count[0:-24]
    # prec_result = only_count
    # print 'prec_result=', only_count

    url = []
    content = []
    for li in g_soup.findAll('li', attrs={'class': 'g'}):
        links = li.find('a')
        link = links['href']
        url.append(link)
        scrap_content = li.find('span', attrs={'class': 'st'})
        contents = remove_tag.sub('', str(scrap_content)).replace('.', '')
        content.append(contents.encode("ascii", "xmlcharrefreplace"))

    i = 0
    while (i <= len(url)-1):
        print "\nurl: {}".format(str(url[i]))
        print "content: {}".format(str(content[i]))
        i += 1


def worker(k):
    print "Crawling google with keyword: {}".format(k)
    scrapping_site_google(k)


def main():
    args = parse_args()

    if not args.keyword:
        sys.exit("[!] Please enter url with option -k: -k ")
    else:
        if args.recursive:
            k = str(args.keyword).replace('\n', ' ')+str(args.recursive)
            worker(k)
        else:
            k = args.keyword
            worker(k)


if __name__ == '__main__':
    main()
