#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import argparse
import argcomplete
import xmltodict
import os
from collections import defaultdict

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-b", "--base",
                        dest="base_smdb",
                        required=True,
                        help="Smokemonster SMDB")

    parser.add_argument("-s", "--sub",
                        dest="subtract_dats",
                        nargs='+',
                        required=True,
                        help="DAT to subtract")

    parser.add_argument("-o", "--out",
                        dest="output_folder",
                        required=True,
                        help="Desired output folder")

    parser.add_argument("-m", "--min",
                        dest="min_smdb",
                        required=True,
                        help="Smokemonster minus No-Intro")

    argcomplete.autocomplete(parser)
    ARGS = parser.parse_args()

def parse_smdb(target_smdb):
    db = {}
    number_of_entries = 0
    with open(target_smdb, "r") as target_smdb:
        for line in target_smdb:
            sha256, filename, sha1, md5, crc32 = line.strip().split("\t", 4)
            number_of_entries += 1
            db[sha1] = {}
            db[sha1]['sha256'] = sha256
            db[sha1]['md5'] = md5
            db[sha1]['crc32'] = crc32
            db[sha1]['filename'] = ARGS.output_folder+"/"+os.path.basename(filename.rstrip(os.sep))
    return db

def parse_dat(target_dat):
    with open(target_dat, "r") as fd:
        doc = xmltodict.parse(fd.read())

    db = {}
    for game in doc['datafile']['game']:
        sha1 = (game['rom']['@sha1']).lower()
        md5 = (game['rom']['@md5']).lower()
        crc = (game['rom']['@crc']).lower()
        filename = game['rom']['@name']
        db[sha1] = {}
        db[sha1]['md5'] = md5
        db[sha1]['crc'] = crc
        db[sha1]['filename'] = filename
    return db

def generate_min_db(smdb, subtract_dats):
    parsed = {}
    for dat in subtract_dats:
        if dat.endswith(".dat"):
            parsed = parse_dat(dat)
        elif dat.endswith(".txt"):
            parsed = parse_smdb(dat)
        for key in parsed.keys():
            if key in smdb:
                smdb.pop(key)
    return smdb

if __name__ == '__main__':
    smdb = parse_smdb(ARGS.base_smdb)
    min_db = generate_min_db(smdb, ARGS.subtract_dats)

    f = open(ARGS.min_smdb, "w+")
    for m in min_db:
        sha1 = m
        sha256 = min_db[m]['sha256']
        filename = min_db[m]['filename']
        md5 = min_db[m]['md5']
        crc32 = min_db[m]['crc32']
        f.write("%s\t%s\t%s\t%s\t%s\n" % (sha256, filename, sha1, md5, crc32))
