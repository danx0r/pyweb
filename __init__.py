#rsi protection:
import html_tags
html_tags = [x for x in dir(html_tags) if x[0] != '_']
from html_tags import *                     #for PyCharm

INDENT=3

def get_tag(e):
    for k in e.keys():
        if k in html_tags:
            return k


def parse(pyml, indent=0):
    # print ("A", pyml)
    if hasattr(pyml, 'lower'):  # raw text element
        return "{0}{1}\n".format(" "*indent, pyml)
    html=""
    for el in pyml:
        if hasattr(el, 'lower'):  # embedded text element
            html += "{0}{1}\n".format(" "*indent, el)
            continue
        tag=get_tag(el)                 #tag element
        body = el[tag]
        html += "{0}<{1}".format(" "*indent, tag)
        for att, val in el.items():
            if att != tag:
                html += ' {0}="{1}"'.format(att, val)
        html += ">\n{0}{1}</{2}>\n".format(parse(body, indent=indent+INDENT), " "*indent, tag)
    return html