from lexical import Token, parse
import sys

class Node:
    pass

tokens = []

token_idx = -1
current_token = None
current_line = 1

def advance():
    global token_idx, current_token
    if token_idx < len(tokens):
        token_idx += 1
        current_token = tokens[token_idx]
        

def program():
    global current_token, current_line
    nodes = []
    if current_token.tokentype == "start_code_delimiter":
        nodes.append(("START",current_token))
        advance()
        if current_token.tokentype == "linebreak":
            current_line +=1 
            advance()
            statementList = statement_list()
            nodes.append(statementList)
            if current_token.tokentype == "end_code_delimiter":
                nodes.append(("END",current_token))
                advance()
            else:
                raise SyntaxError('End code delimter not found : {}'.format(current_line))
        else:
            raise SyntaxError('linebreak expected after HAI : Line {}'.format(current_line))
    else: 
        
        raise SyntaxError('Start code delimiter not found : Line {}'.format(current_line))

    return nodes

def statement_list():
    global current_token, current_line
    nodes = []
    while current_token.tokentype != "end_code_delimiter":
        node = statement()
        if node is not None:
            nodes.append(node)
        if current_token.tokentype == "linebreak":
            current_line += 1
            advance()
        else:
            raise SyntaxError('Linebreak expected after statement : Line {}'.format(current_line))
    return nodes

def statement():
    global current_token
    if current_token.tokentype in ("print_keyword"):
        advance()
        return ("PRINT", expression())  
    else:
        raise SyntaxError('Invalid statement : Line {}'.format(current_line))
    
def expression():
    if current_token.tokentype in ["numbr_literal", "numbar_literal"]:
        node = ("NUMBER", current_token.tokentype, current_token.tokenvalue)
        advance()
        return node
    elif current_token.tokentype in ["troof_literal"]:
        node = ("BOOLEAN", current_token.tokentype, current_token.tokenvalue)
        advance()
        return node
    elif current_token.tokentype in ["string_delimiter"]:
        advance()
        if current_token.tokentype in ["string_literal"]:
            node = ("STRING", current_token.tokentype, current_token.tokenvalue)
            advance() #string delimiter
            if current_token.tokentype in ["string_delimiter"]:
                advance() 
                return node
            else:
                raise SyntaxError('String delimiter expected : Line {}'.format(current_line))
        else:
            raise SyntaxError('Invalid string literal on VISIBLE : Line {}'.format(current_line))
    # VARIABLES
    # elif current_token.isalpha():
    #     node = ('VARIABLE', current_token)
    #     advance()
    #     return node
    else:
        raise SyntaxError('Invalid expression on VISIBLE : Line {}'.format(current_line))

def syntax_analyzer():
    global current_token,token_idx
    print("\nSYNTAX ANALYZER:")
    advance()
    return program()
        
if __name__ == '__main__':
    tokens = parse(sys.argv[1])
    print(tokens)
    parse_tree = syntax_analyzer()
    print(parse_tree)