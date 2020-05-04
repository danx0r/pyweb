#rsi protection:
try:
    import html_tags
    from html_tags import *
except:
    from . import html_tags
    from .html_tags import *

html_tags = [x for x in dir(html_tags) if x[0] != '_']

INDENT=3

def get_tag(e):
    for k in e.keys():
        if k in html_tags:
            return k

def get_childs(e):
    t = get_tag(e)
    v = e[t]
    if hasattr(v, 'lower'):
        return []
    return v


def get_by_id(p, i):                                #FIXME: create map of id's, this is N*N slow
    for e in p:
        if hasattr(e, 'lower'):
            continue
        if 'id' in e and e['id']==i:
            return e
        for c in get_childs(e):
            ii = get_by_id(e, i)
            if ii:
                return ii
    return None


def get_childs_by_id(e, i):
    return get_childs(get_by_id(e, i))


def parse(pyml, indent=0):
    # print ("A", pyml)
    if hasattr(pyml, 'lower'):  # raw text element
        if len(pyml):
            return "{0}{1}\n".format(" "*indent, pyml)
        else:
            return ''
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


if __name__=="__main__":
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