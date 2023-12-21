from lexer import Token, parse
import sys
import regex as re
import math

expression_tokens = ["add_keyword", 
                    "subtract_keyword", 
                    "multiply_keyword", 
                    "divide_keyword", 
                    "modulo_keyword",
                    "return_larger_number_keyword", 
                    "return_smaller_number_keyword", 
                    "both_true_check_keyword", 
                    "both_false_check_keyword", 
                    "exactly_one_is_true_check_keyword", 
                    "negate_keyword", 
                    "atleast_one_true_check_keyword", 
                    "all_true_check_keyword",
                    "both_argument_equal_check_keyword", 
                    "both_argument_not_equal_check_keyword"]

arith_tokens = ["add_keyword", 
                "subtract_keyword", 
                "multiply_keyword", 
                "divide_keyword", 
                "modulo_keyword", 
                "return_larger_number_keyword", 
                "return_smaller_number_keyword"]

bool_tokens =  ["both_true_check_keyword", 
                "both_false_check_keyword", 
                "exactly_one_is_true_check_keyword", 
                "negate_keyword", 
                "atleast_one_true_check_keyword", 
                "all_true_check_keyword"]

comp_tokens =  ["both_argument_equal_check_keyword", 
                "both_argument_not_equal_check_keyword"]

class Variable:
    def __init__(self, name, value, valuetype_ = None):
        self.name = name
        self.value = value
        self.valuetype = valuetype_

    def __repr__(self) -> str:
        return f"({self.type}, \"{self.value}\", {self.valuetype})"

variables = {'IT': None}

tokens = []

token_idx = -1
current_token = None
current_line = 1
    
def advance():
    global token_idx, current_token
    if token_idx < len(tokens):
        token_idx += 1
        current_token = tokens[token_idx]

def error(msg, line):
    print("Error: {} : Line {}".format(msg,line))
    sys.exit()

def if_linebreak():
    global current_token, current_line
    if current_token.tokentype == "linebreak":
        current_line += 1
        advance()
    else:
        error("[SyntaxError] Linebreak expected after statement", current_line)
 
def program():
    global current_token, current_line
    nodes = []
    if current_token.tokentype == "start_code_delimiter":
        nodes.append(("START",current_token))
        advance()
        if_linebreak()
        # VARIABLE DECLARATION
        if current_token.tokentype == "start_var_declaration_delimiter": # WAZZUP
            advance() # pass wazzup
            if_linebreak()
            varDeclarationList = var_declaration_list()
            nodes.append(("VAR_DEC_LIST",varDeclarationList))
            if current_token.tokentype == "end_var_declaration_delimiter":
                advance() # pass BUHBYE
                if_linebreak()
            else:
                error("[SyntaxError] End variable declaration delimiter (BUHBYE) not found", current_line)
        else:
            error("[SyntaxError] Start variable declaration delimiter (WAZZUP) not found", current_line)
        
        # STATEMENTS_LIST
        statementList = statement_list()
        nodes.append(("STAT_LIST", statementList))
        if current_token.tokentype == "end_code_delimiter":
            nodes.append(("END",current_token))
            advance()
        else:
            error("[SyntaxError] End code delimiter (KTHXBYE) not found", current_line)
    else: 
        error("[SyntaxError] Start code delimiter (HAI) not found", current_line)

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
            error("[SyntaxError] Linebreak expected after variable declaration", current_line)
            break
    return nodes

def var_declaration():
    global current_token, current_line
    if current_token.tokentype == "variable_declaration": # I HAS A
        advance() # pass I HAS A
        if current_token.tokentype == "variable_identifier": # var
            varident = current_token.tokenvalue
            advance() # pass var
            if current_token.tokentype == "variable_assignment":
                advance() # pass ITZ
                if current_token.tokentype == "variable_identifier":
                    # if not yet in variables then throw error
                    if current_token.tokenvalue not in variables:
                        error("[SyntaxError] Variable not yet declared", current_line)
                    # else, get the value of the variable and assign it to the new variable
                    variables[varident] = variables[current_token.tokenvalue]
                    node = ("VARIABLE", varident, current_token)
                    advance()
                    return node
                else: 
                    literal_ = literal() 
                    # typecast string according to token type
                    var_value = literal_.tokenvalue
                    if literal_.tokentype == "numbr_literal":
                        var_value = int(literal_.tokenvalue)
                    elif literal_.tokentype == "numbar_literal":
                        var_value = float(literal_.tokenvalue)
                    elif literal_.tokentype == "troof_literal":
                        if literal_.tokenvalue == "WIN":
                            var_value = True
                        else:
                            var_value = False
                    variables[varident] = var_value
                    return ("VARIABLE", varident, literal_)                
            elif current_token.tokentype == "linebreak": # I HAS A var (only, no ITZ) - untyped or uninitialized variable
                variables[varident] = None # null value
                return ("VARIABLE", varident, "NOOB") # place untyped or uninitialized variable inside nodes list
            else:
                error("[SyntaxError] Invalid variable assignment", current_line)
        else:
            error("[SyntaxError] Invalid variable identifier", current_line)
    else:
        error("[SyntaxError] Invalid variable declaration", current_line)

def varident():
    global current_token
    if current_token.tokentype == "variable_identifier": # check if variable identifier
        if current_token.tokenvalue not in variables:
            error("[SyntaxError] Variable not yet declared", current_line)
        node = current_token
        advance() # pass varident to go to next token
        return node
    else:
        error("[SyntaxError] Invalid variable identifier", current_line)

def statement():
    global current_token
    if current_token.tokentype == "print_keyword": # to add + in VISIBLE (concatenation)
        advance() # pass VISIBLE
        return ("PRINT", print_expression())  
    elif current_token.tokentype == "input_keyword":
        advance() # pass GIMMEH
        varident_ = varident()
        variables[varident_.tokenvalue]= input("")
        print("variables is now:", variables)
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
            #TODO: add expression
            else:
                error("[SyntaxError] Invalid variable value reassignment", current_line)
        
        elif current_token.tokentype == "full_typecast_keyword": # changing the type of the varriable
            advance() # pass IS NOW A
            if current_token.tokentype == "type_literal":
                type_literal_ = current_token
                handle_full_typecast(varidentDest, type_literal_.tokenvalue, current_line)
                advance() # pass NUMBAR/NUMBR/TROOF/YARN
                return("FULL_TYPECAST", varidentDest, type_literal_)
            else:
                error("[SyntaxError] Invalid typecast literal", current_line)
        else:
            error("[SyntaxError] Invalid variable value reassignment. R not found. ", current_line)

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
             error("[SyntaxError: Invalid typecast literal: Line", current_line)
    
    # elif currenttoken.tokentype == "concatenation_keyword" #SMOOSH 
    
    # elif current_token.tokentype == "general_purpose_break_token": #GTFO

    # elif cuurent_token.tokentype == "return keyword": #FOUND YR    
    
    # else check if expression
    else:
        if current_token.tokentype in expression_tokens:
            expression_ = expression()
            return expression_

        else:
            error("[SyntaxError] Invalid statement", current_line)

def expression():
    global current_token, current_line
    if current_token.tokentype in arith_tokens:
        node = arithmetic_expression() 
    # elif current_token.tokentype in comp_tokens:
    #     node = compare_expression()
    # elif current_token.tokentype in bool_tokens:
    #     node = boolean_expression()
    return node

def typecast_string(string):
    numbr_pattern = r"-?([1-9][0-9]*|0)"
    numbar_pattern = r"-?(0|[1-9][0-9]*)(\.[0-9]+)?"
    # typecast string to numbr or numbar
    if string == "WIN":
        return 1
    elif string == "FAIL":
        return 0
    elif re.fullmatch(numbr_pattern, string):
        return int(string)
    elif re.fullmatch(numbar_pattern, string):
        return float(string)
    else:
        return None 

def typecast_troof(troof):
    # typecast troof to numbr or numbar
    if troof == "WIN":
        return 1
    else:
        return 0
    
def arithmetic_expression():
    global current_token, current_line
    if current_token.tokentype == "add_keyword":
        advance() # pass SUM OF
        # left operand # operand can be a variable, numbar, numbr, string, troof  
        if current_token.tokentype in expression_tokens:
            left = expression()
        elif current_token.tokentype in ["numbr_literal","numbar_literal"]:
            left = current_token.tokenvalue
        elif current_token.tokentype == "string_delimiter":
            advance() # pass starting "
            if current_token.tokentype == "string_literal":
                left = typecast_string(current_token.tokenvalue)
                advance() # pass string literal
                if current_token.tokentype != "string_delimiter":
                    error("[Syntax Error] String delimiter expected", current_line)
            else:
                error("[Syntax Error] Invalid string literal", current_line)
        elif current_token.tokentype == "troof_literal":
            left = typecast_troof(current_token.tokenvalue)
        elif current_token.tokentype == "variable_identifier":
            if current_token.tokenvalue in variables.keys() and variables[current_token.tokenvalue] is not None:
                left = variables[current_token.tokenvalue]
            else:
                error("[Logic Error] Variable not found", current_line)
        else:
            error("[Syntax Error] Invalid operand", current_line)

        advance() # pass LEFT OPERAND
        
        if current_token.tokentype == "and_keyword":
            advance() # pass AN
            #right operand
            if current_token.tokentype in expression_tokens:
                right = expression()
            elif current_token.tokentype in ["numbr_literal","numbar_literal"]:
                right = current_token.tokenvalue
            elif current_token.tokentype == "string_delimiter":
                advance() # pass starting "
                if current_token.tokentype == "string_literal":
                    right = typecast_string(current_token.tokenvalue)
                    advance() # pass string literal
                    if current_token.tokentype != "string_delimiter":
                        error("[Syntax Error] String delimiter expected", current_line)
                else:
                    error("[Syntax Error] Invalid string literal", current_line)
            elif current_token.tokentype == "troof_literal":
                right = typecast_troof(current_token.tokenvalue)
            elif current_token.tokentype == "variable_identifier":
                if variables[current_token.tokenvalue] is not None:
                    right = variables[current_token.tokenvalue]
                else:
                    error("[Logic Error] Variable not found", current_line)
            else:
                error("[Syntax Error] Invalid operand", current_line)            
            #add
            advance()
            result = left + right
            return ('EXPRESSION', result)
        else:
            error("[Syntax Error] AN keyword not found", current_line)
    # SUBTRACTION 
    # MULTIPLICATION
    else:
        error("[Syntax Error] Incorrect Arithmetic Expression", current_line)
    

def handle_full_typecast(var_name, target_type, current_line):
    global current_token
    yarn_pattern = r"^-?(0|[1-9][0-9]*)(\.[0-9]+)?$"
    
    #Get the value associated w/ variable identifier
    var_value = variables.get(var_name, "NOOB")

    #perfrom type conversion based on target type
    if target_type == "NUMBR":
        if var_value == "WIN":   #Note: consider string literals WIN and FAIL, not just troof
            new_value = 1
            variables[var_name] = new_value
        elif var_value == "FAIL":
            new_value = 0
            variables[var_name] = new_value
        elif isinstance(var_value, str):
            # test yarn_pattern
            print("stringgg")
            if re.fullmatch(yarn_pattern, var_value):
                print("var_value:", var_value)
                var_value = re.sub(r'\.\d+', '', var_value)
                variables[var_name] = int(var_value)
            else:
                error(f"[RuntimeError] Invalid String. Cannot convert '{var_value}' to NUMBR", current_line)
        else: # for None
            error(f"[RuntimeError] Cannot convert '{var_value}' to NUMBR", current_line)
    
    elif target_type == "NUMBAR":
        if var_value == True:   #Note: consider string literals WIN and FAIL, not just troof
            new_value = 1
            float(new_value)
            variables[var_name] = new_value
        elif var_value == False:
            new_value = 0
            float(new_value)
            variables[var_name] = new_value
        elif isinstance(var_value, str):
            if re.fullmatch(yarn_pattern, var_value):
                variables[var_name] = int(var_value)
            else:
              error(f"[RuntimeError] Invalid String. Cannot convert '{var_value}' to NUMBAR", current_line)  
        else: # for None
            error(f"[RuntimeError] Cannot convert '{var_value}' to NUMBAR", current_line)
    
    elif target_type == "TROOF":
            if var_value == "":
                new_value = False # will print FAIL in Symbol Table
            elif var_value == "WIN":
                new_value = True # equivalent to WIN troof_literal
            elif var_value == "FAIL":
                new_value = False # equivalent to FAIL troof_literal
            elif var_value == 0:
                new_value = False # equivalent to FAIL
            else:
                new_value = True # equivalent to WIN
        
            variables[var_name] = new_value
            
    elif target_type == "YARN":
        if variables[var_name] == True:
            variables[var_name] = "WIN"
        elif variables[var_name] == False:
            variables[var_name] = "FAIL"
        elif variables[var_name] == None:
            error(f"[RuntimeError] Cannot convert uninitialized value to YARN", current_line)
        variables[var_name] = str(variables[var_name])
    elif target_type == "NOOB": # var IS NOW A NOOB # typecase a variable to NOOB
        variables[var_name] = None
    
    else:
        error(f"[RuntimeError] Failed to convert '{var_value}'", current_line)

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
                error("[SyntaxError] String delimiter expected", current_line)
        else:
            error("[SyntaxError] Invalid string literal", current_line)
    else:
        error("[SyntaxError] Invalid literal", current_line)


def statement_list():
    global current_token, current_line
    nodes = []
    while current_token.tokentype != "end_code_delimiter":
        node = statement()
        if node is not None:
            nodes.append(node)
        if_linebreak()

    return nodes


def print_expression():
    global current_token

    if current_token.tokentype in ["numbr_literal", "numbar_literal", "troof_literal"]:
        node = current_token
        advance() # pass literal
        # print the value of the literal
        # print(node.tokenvalue, end=" ")
        #extract/print value of literal 
        literal_value = node.tokenvalue
        print(literal_value)
        return node
    elif current_token.tokentype == "string_delimiter": # string literal
        advance()
        if current_token.tokentype == "string_literal":
            node = current_token
            advance() #string delimiter
            if current_token.tokentype == "string_delimiter":
                advance() 
                #extract/print value of string literal 
                string_value = node.tokenvalue
                print(string_value)
                return node
            else:
                error("[SyntaxError] String delimiter expected", current_line)
        else:
            error("[SyntaxError] Invalid string literal", current_line)
    elif current_token.tokentype == "variable_identifier": # check if variable identifier
        node = ("VARIDENT", current_token.tokentype, current_token.tokenvalue)
        if current_token.tokenvalue not in variables:
            error("[SyntaxError] Variable not yet declared", current_line)
        #extract/print value of var identifier
        variable_value = variables[current_token.tokenvalue]
        print(variable_value)
        advance() # pass varident
        return node
    elif current_token.tokentype in expression_tokens:
        node = expression()
        print(node[1])
        return node
    else:
        error("[SyntaxError] Invalid print arguments", current_line)

def syntax_analyzer():
    global current_token,token_idx
    print("\nSYNTAX ANALYZER:")
    advance()
    return program()

def do_parse_tree(tokens_list):
    global tokens
    tokens = tokens_list
    parse_tree = syntax_analyzer()
    return parse_tree, variables
        
if __name__ == '__main__':
    tokens = parse(sys.argv[1])
    print(tokens)
    parse_tree = syntax_analyzer()
    print(variables)
    print(("PROGRAM",parse_tree))