import scanner as scan


def parser():
    tokens = scan.scanner("f b i a a = 5 b = a + 3.2 p b")
    i = 0
    prog(tokens)
    return tokens


def prog(tokens):
    dcls(tokens)
    stmts(tokens)
    # $


def dcls(tokens):
    dcl(tokens)
    dcls(tokens)
    # lambda


def dcl(tokens):
    try:
        if tokens[i].type == "floatdcl" or tokens[i].type == "intdcl":
            global i
            is_id = tokens[i+1].type == "id"
            if is_id:
                i += 1
            else:
                return -1
        else:
            return "lambda"
    except IndexError:
        raise Exception("Index out of range error Error")


def stmts(tokens):
    try:
        if tokens[i].type == "id" or tokens[i].type == "p":
            stmt(tokens)
            stmts(tokens)
        else:
            if not(tokens[i].type == "$"):
                return -1
    except IndexError:
        raise Exception("Index out of range error Error")


def stmt(tokens):
    try:
        if tokens[i].type == "id":
            id = match(tokens[i], "id")
            assign = match(tokens[i+1], "assign")
            val(tokens[i+2])
            if id and assign and val:
                global i
                i += 1
            exp(tokens)
        else:
            if tokens[i].type == "print":
                id = match(tokens[i], "id")
                assign = match(tokens[i+1], "assign")
                val(tokens[i+2])
                if id and assign and val:
                    global i
                    i += 1
                exp(tokens)
    except IndexError:
        raise Exception("Index out of range error Error")


def val(token):
    if token.type == "inum" or token.type == "fnum":
        return True
    else:
        return False


def exp(tokens):
    try:
        if tokens[i].type == "plus" or tokens[i].type == "minus":
            if val(tokens[i+1]):
                exp(tokens[i+2])
            else:
                raise Exception("Value Error")
        else:
            raise Exception("Expression Error")
    except IndexError:
        raise Exception("Index out of range error Error")


def match(token, type):
    if token.type == type:
        return True
    else:
        return False
