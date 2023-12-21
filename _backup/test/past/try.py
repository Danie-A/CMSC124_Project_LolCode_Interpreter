
def lex_num(line):
    num= ""
    for c in line:
        if not c.isdigit():
            break
    return 'num', int(num), len(num)
    
def lex_str(line):
    delimiter = line[0]
    string = ""
    for c in line:
         if c==delimiter:
             break
         string += c
    return 'str', string, len(string)

def lex_id(line):
    keys = ['print', 'var', 'while', 'if', 'elif', 'else']
    id = ""
    for c in line:
        if not c.isdigit() and not c.isalpha and c != "_":
            break
        id += c
    if id in keys:
        return "key", id, len(id)
    else:
        return "ID", id, len(id)

def lex(line):
    lexeme_count = 0
    while lexeme_count < len(line):
        lexeme = line[lexeme_count]
        if lexeme.isdigit():
            typ, tok, consumed = lex_num(line[lexeme_count:])
            lexeme_count += consumed
        elif lexeme == "\"" or lexeme == "\"":
            typ, tok, consumed = lex_str(line[lexeme_count:])
            lexeme_count += consumed
        elif lexeme.isalpha():
            typ, tok, consumed = lex_id(line[lexeme_count])
            lexeme_count += consumed
        else:
            lexeme_count += 1
code = input()
lex(code)