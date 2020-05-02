import pyweb

pg=pyweb.html()
pg.div("Hello Earthlings!")
s=pg.generate()
print(s)
f=open("test.html", 'w')
f.write(s)
f.close()
