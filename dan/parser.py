from lexer import Token, parse
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

def if_linebreak():
    global current_token, current_line
    if current_token.tokentype == "linebreak":
        current_line += 1
        advance()
    else:
        print('SyntaxError: Linebreak expected after statement : Line {}'.format(current_line))
        return 

def error(msg, line):
    print("Error: {} at line {}".format(msg,line))
           
def program():
    global current_token, current_line
    nodes = []
    if current_token.tokentype == "start_code_delimiter":
        nodes.append(("START",current_token))
        advance()
        if_linebreak()
        
    return nodes


def var_declaration_list():
    global current_token, current_line
    nodes = []
    while current_token.tokentype != "end_var_declaration_delimiter":
        node = var_declaration()
        if node is not None:
            nodes.append(node)
        if current_token.tokentype == "linebreak":
            current_line += 1
            advance()
        else:
            print('SyntaxError: Linebreak expected after variable declaration : Line {}'.format(current_line))
            return 
    return nodes

def var_declaration():
    global current_token, current_line
    # print("current token type is:", current_token.tokentype)
    if current_token.tokentype == "variable_declaration": # I HAS A
        # print("current token type is:", current_token.tokentype)
        # print("current line is:", current_line)
        advance() # pass I HAS A
        if current_token.tokentype == "variable_identifier": # var
            varident = current_token.tokenvalue
            advance() # pass var
            if current_token.tokentype == "variable_assignment":
                advance() # pass ITZ
                literal_ = literal()
                return ("VARIABLE", varident, literal_)                
            elif current_token.tokentype == "variable_identifier":
                node = ("VARIABLE", varident, current_token)
                advance()
                return node
            elif current_token.tokentype == "linebreak": # I HAS A var (only, no ITZ) - untyped or uninitialized variable
                return ("VARIABLE", varident, "NOOB") # place untyped or uninitialized variable inside nodes list
            else:
                print('SyntaxError: Invalid variable assignment : Line {}'.format(current_line))
                return 
        else:
            print('SyntaxError: Invalid variable identifier : Line {}'.format(current_line))
            return 
    else:
        print('SyntaxError: Invalid variable declaration : Line {}'.format(current_line))
        return 

def varident():
    global current_token
    if current_token.tokentype == "variable_identifier": # check if variable identifier
        node = current_token
        advance()
        return node
    else:
        print('SyntaxError: Invalid variable identifier : Line {}'.format(current_line))
        return 

def statement():
    global current_token
    if current_token.tokentype == "print_keyword": # to add + in VISIBLE (concatenation)
        advance() # pass VISIBLE
        return ("PRINT", print_expression())  
    elif current_token.tokentype == "input_keyword":
        advance() # pass GIMMEH
        varident_ = varident()
        return ("INPUT", varident_)
    elif current_token.tokentype == "variable_identifier": #assignment statement
        varidentDest = current_token.tokenvalue
        advance() # pass varident
        if current_token.tokentype == "variable_value_reassignment":
            advance() # pass R
            if current_token.tokentype == "variable_identifier":
                varidentSrc = current_token
                advance() # pass varident
                return ("ASSIGN", varidentDest, varidentSrc)
            elif current_token.tokentype in ["numbr_literal", "numbar_literal", "troof_literal", "string_delimiter"]:
                literal_ = literal()
                return ("ASSIGN", varidentDest, literal_)
            # to add expression
            else:
                print('SyntaxError: Error in reassignment statement. Invalid variable identifier, literal, or expression : Line {}'.format(current_line))
                return 
        
        elif current_token.tokentype == "full_typecast_keyword": # changing the type of the varriable
            advance() # pass IS NOW A
            if current_token.tokentype == "type_literal":
                type_literal_ = current_token
                advance() # pass NUMBAR/NUMBR/TROOF/YARN
                return("FULL_TYPECAST", varidentDest, type_literal_)
            else:
                print('SyntaxError: Typecasting Error. Invalid type literal : Line {}'.format(current_line))
                return 
        else:
            print('SyntaxError: Variable value reassignment (R) not found : Line {}'.format(current_line))
            return 
    elif current_token.tokentype == "typecast_keyword":
        advance() # pass MAEK
        varident_ = varident() # var
        # may or may not include A typecast_prefix
        if current_token.tokentype == "typecast_prefix":
            advance() # pass A
        if current_token.tokentype == "type_literal":
            type_literal_ = current_token
            advance() # pass NUMBAR/NUMBR/TROOF/YARN
            return ("TYPECAST", varident_, type_literal_)
        else:
            print('SyntaxError: Invalid typecast literal: Line {}'.format(current_line))
            return         
    else:
        print('SyntaxError: Invalid statement : Line {}'.format(current_line))
        return 
    
# [] to-add expression() function 

def literal():
    if current_token.tokentype in ["numbr_literal", "numbar_literal", "troof_literal"]:
        node = current_token
        advance()
        return node
    elif current_token.tokentype == "string_delimiter": # string literal
        advance()
        if current_token.tokentype == "string_literal":
            node = current_token
            advance() #string delimiter
            if current_token.tokentype == "string_delimiter":
                advance() 
                return node
            else:
                print('SyntaxError: String delimiter expected : Line {}'.format(current_line))
                end_parse()
        else:
            print('SyntaxError: Invalid string literal : Line {}'.format(current_line))
            return 
    else:
        print('SyntaxError: Invalid literal : Line {}'.format(current_line))
        return 

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
            print('SyntaxError: Linebreak expected after statement : Line {}'.format(current_line))
            return 
    return nodes
    
def print_expression():
    global current_token

    if current_token.tokentype in ["numbr_literal", "numbar_literal", "troof_literal"]:
        node = current_token
        advance()
        return node
    elif current_token.tokentype == "string_delimiter": # string literal
        advance()
        if current_token.tokentype == "string_literal":
            node = current_token
            advance() #string delimiter
            if current_token.tokentype == "string_delimiter":
                advance() 
                return node
            else:
                print('SyntaxError: String delimiter expected : Line {}'.format(current_line))
                return 
        else:
            print('SyntaxError: Invalid string literal : Line {}'.format(current_line))
            return 
    elif current_token.tokentype == "variable_identifier": # check if variable identifier
        node = ("VARIDENT", current_token.tokentype, current_token.tokenvalue)
        advance()
        return node
    else:
        print('SyntaxError: Invalid print arguments : Line {}'.format(current_line))
        return 

def syntax_analyzer():
    global current_token,token_idx
    print("\nSYNTAX ANALYZER:")
    advance()
    return program()

def do_parse_tree(tokens_list):
    global tokens
    tokens = tokens_list
    parse_tree = syntax_analyzer()
    return parse_tree
        
if __name__ == '__main__':
    tokens = parse(sys.argv[1])
    print(tokens)
    parse_tree = syntax_analyzer()
    print(("PROGRAM",parse_tree))