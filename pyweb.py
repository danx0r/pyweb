#rsi protection:
html_tags=[
"html",
"div",
"span",
"a",
"href",
"span",
"style"]

for t in html_tags:
    globals()[t]=t

def get_tag(e):
    for k in e.keys():
        if k in html_tags:
            return k

def parse(py):
    s=""
    for e in py:
        tag=get_tag(e)
        body = e[tag]
        if type(body)
    return s