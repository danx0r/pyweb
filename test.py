from pyweb import *
from pprint import pprint

pg=[
    {html: [
        "hello",
        {div: [
            {a: "link", 'href': "http://www.busyboxes.org", 'style': "font-family: sans; background-color: pink"}
        ]},
        {span: "goodbye"},
        {"button": "OK", "onclick": "alert('okay')"}                                    #regular string is fine too
    ]}
]

print(parse(pg))
