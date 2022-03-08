import scanner as scan

def parser(tokens):
    tokens = scan.scanner("f b i a a = 5 b = a + 3.2 p b")
    i = 0
    prog(tokens)

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
        raise ("Index out of range error Error")

def stmts(tokens):
    try:
        if tokens[i].type == "id" or tokens[i].type == "p" :
            stmt(tokens)
            stmts(tokens)
        else:
            if not(tokens[i].type == "$"):
                return -1
    except IndexError:
        raise ("Index out of range error Error")

def stmt(tokens):
    try:
        if tokens[i].type == "id":
            id = match(tokens[i], "id")
            assign = match(tokens[i+1], "assign")
            val(tokens[i+2])
            if id and assign and val:
                global i
                i+=1
            exp(tokens[i+3])
            
    except IndexError:
        raise ("Index out of range error Error")
        
def val(token):
    if token.type == "inum" or token.type == "fnum":
       return True
    else:
        return False

def exp(tokens[i]):
    
    
def match(token, type):
    if token.type == type:
        return True
    else:
        return False

