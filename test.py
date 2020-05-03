from pyweb import *
from pprint import pprint

pg=[
    {html: [
        "hello",
        {div: [
            {a: "link", 'href': "http://www.busyboxes.org", 'style': "font-family: sans; background-color: pink"}
        ]},
        {span: "goodbye", 'style': "font-size: 200%"},
        {"button": "OK", "onclick": "alert('okay')"}                                    #regular string is fine too
    ]}
]

print(parse(pg))
