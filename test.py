from pyweb import *
from pprint import pprint

pg=[
    {html: [
        {div: [
            {a: "link", href: "www.busyboxes.org", style: "font-color: purple"}
        ]},
        {span: "goodbye"},
        {"button": "OK", "onclick": "alert('okay')"}
    ]}
]

print(parse(pg))
