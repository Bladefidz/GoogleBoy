#! usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='File contains keywords')
    parser.add_argument('-R', '--recursive', help='Recursive query')
    return parser.parse_args()


def b(text):
    for ch in ['\n', '\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '>',
               '#', '+', '-', '.', '!', '$', '\'']:
        if ch in text:
            text = text.replace(ch, "_")
    return text


def recursivly(args):
    fl = args.file
    recv = args.recursive
    str_fl = str(fl)
    str_recv = str(recv)
    with open(str_fl, "r") as keywordfiles:
        data = keywordfiles.readlines()
        i = 0
        while (i <= len(data)-1):
            normalized = b(str(data[i])+str(str_recv))
            filename = str(normalized)+".txt"
            subprocess.Popen(['python', 'doitgoogle.py', '-k', data[i],
                             '-R', str_recv], stdout=open(filename, 'w'))
            i += 1


if __name__ == "__main__":
    args = parse_args()

    if not args.file:
        sys.exit("[!] Please enter url with option -u: -u ")
    else:
        if args.recursive:
            recursivly(args)
        else:
            fl = args.file
            str_fl = str(fl)
            with open(str_fl, "r") as keywordfiles:
                data = keywordfiles.readlines()
                i = 0
                while (i <= len(data)-1):
                    normalized = b(str(data[i]))
                    filename = str(normalized)+".txt"
                    subprocess.Popen(['python', 'doitgoogle.py', '-k',
                                     data[i]], stdout=open(filename, 'w'))
                    i += 1
