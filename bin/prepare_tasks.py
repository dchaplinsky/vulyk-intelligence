#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from unicodecsv import reader
import json
from codecs import open

if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit("Not enough arguments")

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    with open(in_file, "r") as f_in, open(out_file, "w", encoding="utf-8") as f_out:
        r = reader(f_in)
        r.next()

        for l in r:
            (region, lastname_uk, firstname_uk, patronymic_uk, lastname_ru,
                firstname_ru, patronymic_ru) = l

            rec = {
                "region": region,
                "lastname_uk": lastname_uk,
                "firstname_uk": firstname_uk,
                "patronymic_uk": patronymic_uk,
                "lastname_ru": lastname_ru,
                "firstname_ru": firstname_ru,
                "patronymic_ru": patronymic_ru
            }

            f_out.write(json.dumps(rec, ensure_ascii=False) + "\n")
