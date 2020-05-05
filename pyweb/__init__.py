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


def parse_pyml(pyml, indent=0):
    # print ("A", pyml)
    if pyml == None:
        return ""
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
        html += ">\n{0}{1}</{2}>\n".format(parse_pyml(body, indent=indent+INDENT), " "*indent, tag)
    return html


if __name__=="__main__":
    butstyl = "color: black; margin: 10px; padding: 2px; border: solid thin; text-decoration: none"
    
    list1 = []
    
    bod=[
        {form: [
            {input: '', 'type': "text", 'name': "param1"},
            {input: '', 'type': "submit", 'value': "Go for it"}
        ],
        'action': "act/update.html"
        },
    
        {ul:list1, 'style': "padding-left: 0; margin-left: -10px; list-style: none;"}
    ]
    
    pyml=[
        {html:[
            {head: []},
            {body: bod, 'style': "font-family: sans"}
        ]}
    ]
    
    for x in ('cat', 'dog', 'bird'):
        el={li: [
            {a: "edit", 'href': "act/update.html?edit=%s" % x, 'style': butstyl},
            x
        ], 'style': "margin-top: 10px; list-style-type: none"}
        list1.append(el)
    
    print(parse_pyml(pyml))
