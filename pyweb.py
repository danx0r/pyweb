#rsi protection:
import html_tags
html_tags = [x for x in dir(html_tags) if x[0] != '_']
from html_tags import *                     #for PyCharm


def get_tag(e):
    for k in e.keys():
        if k in html_tags:
            return k


def parse(pyml):
    html=""
    for el in pyml:
        if hasattr(el, 'lower'):            #text element
            html += el
        else:
            tag=get_tag(el)                 #tag element
            body = el[tag]
            html += "<{0}".format(tag)
            for att, val in el.items():
                if att != tag:
                    html += ' {0}="{1}"'.format(att, val)
            html += ">{0}</{1}>".format(parse(body), tag)
    return html