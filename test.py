from pyweb import *
from pprint import pprint

bod=[
    {body: [
        "hello",
        {div: [
            {a: "link", 'href': "http://www.busyboxes.org", 'style': "font-family: sans; background-color: pink"}
        ]},
        {span: "goodbye", 'style': "font-size: 200%; margin: 30px"},
        {"button": "OK", "onclick": "alert('okay')"}                                    #regular string is fine too
    ]}
]

pyml=[
    {html:[
        {head: []},
        {body: bod}
    ]}
]

print(parse(pyml))
