#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import os
import os.path
import json
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

import codecs
import re


def fetch_url(url):
    print(url)
    return "Zaloopah"


def grab_urls(text):
    urls = '(?: %s)' % '|'.join("""http telnet gopher file wais
    ftp""".split())
    ltrs = r'\w'
    gunk = r'/#~:.?+=&%@!\-'
    punc = r'.:?\-'
    any = "%(ltrs)s%(gunk)s%(punc)s" % {'ltrs': ltrs,
                                        'gunk': gunk,
                                        'punc': punc}

    url = r"""
        \b                            # start at word boundary
            %(urls)s    :             # need resource and a colon
            [%(any)s]  +?             # followed by one or more
                                      #  of any valid character, but
                                      #  be conservative and take only
                                      #  what you need to....
        (?=                           # look-ahead non-consumptive assertion
                [%(punc)s]*           # either 0 or more punctuation
                (?:   [^%(any)s]      #  followed by a non-url char
                    |                 #   or end of the string
                      $
                )
        )
        """ % {'urls': urls,
               'any': any,
               'punc': punc}

    url_re = re.compile(url, re.VERBOSE | re.MULTILINE)
    """Given a text string, returns all the urls we can find in it."""
    return url_re.sub(text, fetch_url)

def resolve_links(value):
    print(grab_urls(value))
    return value


sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

ENV = Environment(loader=FileSystemLoader("templates"))
ENV.filters['resolve_links'] = resolve_links
TEMPLATE = ENV.get_template('dossier.html')


def export_answers(answers, out_dir):
    rendered = TEMPLATE.render(answers=answers)
    if "lastname_uk" in answers[0]["task"]["data"]:
        reg_dir = os.path.join(out_dir, answers[0]["task"]["data"]["region"])

        if not os.path.exists(reg_dir):
            os.makedirs(reg_dir)

        fname = "%s/%s %s %s.pdf" % (
            answers[0]["task"]["data"]["region"],
            answers[0]["task"]["data"]["lastname_uk"],
            answers[0]["task"]["data"]["firstname_uk"],
            answers[0]["task"]["data"]["patronymic_uk"])
    else:
        fname = "%s.pdf" % answers[0]["task"]["id"]

    # print(rendered)
    print(fname)
    HTML(string=rendered).write_pdf(os.path.join(out_dir, fname))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit("Not enough arguments")

    in_file = sys.argv[1]
    out_dir = sys.argv[2]

    with open(in_file, "r") as fp_in:
        for i, l in enumerate(fp_in):
            answers = json.loads(l)

            if answers:
                export_answers(answers, out_dir)
                # break
