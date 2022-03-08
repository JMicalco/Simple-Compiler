import re
import Token as tk


def scanner(code):
    token = []
    is_num = False
    for i in range(len(code)):
        if re.search("[0-9]", code[i]):
            end = 0
            if is_num == True:
                continue
            for j in range(i, len(code)):
                if code[j] == " ":
                    end = j
                    break
            if "." in code[i:end]:
                temp_token = tk.Token("fnum")
                temp_token.set_value(code[i:end])
                token.append(temp_token)
            else:
                temp_token = tk.Token("inum")
                temp_token.set_value(code[i:end])
                token.append(temp_token)
            is_num = True
        else:
            is_num = False
            if re.search("[a-e]|[g-h]|[j-o]|[q-z]", code[i]):
                temp_token = tk.Token("id")
                temp_token.set_value(code[i])
                token.append(temp_token)
            elif re.search("f", code[i]):
                token.append(tk.Token("floatdcl"))
            elif re.search("i", code[i]):
                token.append(tk.Token("intdcl"))
            elif re.search("p", code[i]):
                token.append(tk.Token("print"))
            elif re.search("=", code[i]):
                token.append(tk.Token("assign"))
            elif re.search("-", code[i]):
                token.append(tk.Token("minus"))
            elif re.search("\+", code[i]):
                token.append(tk.Token("plus"))
    token.append(tk.Token("$"))
    return token
