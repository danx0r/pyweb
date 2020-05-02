from pyweb import element
from pprint import pprint

pg=element("html")
pg.add(element('text', "Hello Earthlings!"))
e=element('div')
e.add(element('text', "please"))
pg.add(e)
pprint(pg)

def span():
    pass

html=div=text=a=href=span

if html():
    if div():
        text("hello")
    if span():
        text("goodbye")

pg=[
    {"tag": "html", "children": [
        {"tag": "div", "children": [
            "hello"
        ]},
        {"tag": "span", "children": [
            "goodbye"
        ]}
    ]}
]

pg=[
    ["html", [
        ["div", "hello"],
        ["span", "goodbye"]
    ]]
]

pg=[
    {"html": [
        {"div": "hello"},
        {"span": "goodbye"},
    ]}
]

pg=[
    {html: [
        {div: [
            {a: "link", href: "www.busyboxes.org"}
        ]},
        {span: "goodbye"},
    ]}
]
