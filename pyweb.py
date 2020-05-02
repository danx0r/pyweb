#import stringio

class html:
    def __init__(self):
        self.doc=["<html>\n"]

    def div(self, s):
        self.doc.append("<div>{0}</div>\n".format(s))

    def generate(self):
        self.doc.append("</html>\n")
        s=""
        for el in self.doc:
            s+=el
        return s
