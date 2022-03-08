import parser

ast = parser.parser()


def consistent(c1, c2):
    m = generalize(c1.type, c2.type)
    convert(c1, m)
    convert(c2, m)
    return m


def generalize(t1, t2):
    type = ""
    if t1 == "float" or t2 == "floaa":
        type = "float"
    else:
        type = "integer"


def convert(n, t):
    if n.type == "float" and t == "integer":
        raise Exception("Ilegal type conversion")
    else:
        if n.type == "integer" and t == "float":
            n.type = "float"
