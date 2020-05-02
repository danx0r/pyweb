#import stringio

class element:
    def __init__(self, tag, text=None):
        self.tag=tag
        if tag=='text':
            self.body=text
        else:
            self.children=[]

    def add(self, e):
        self.children.append(e)

    def __repr__(self):
        if self.tag=='text':
            return self.body
        else:
            kids=""
            for k in self.children:
                kids+=str(k)
            s="<{0}>{1}</{0}>".format(self.tag, kids)
            # print("S:",s)
            return s