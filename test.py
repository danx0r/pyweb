from pyweb import element
from pprint import pprint

pg=element("html")
pg.add(element('text', "Hello Earthlings!"))
e=element('div')
e.add(element('text', "please"))
pg.add(e)
pprint(pg)
