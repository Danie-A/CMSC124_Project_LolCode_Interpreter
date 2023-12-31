import regex as re
import sys
import math
import tkinter as tk
from tkinter import font
from tkinter import ttk
from tkinter import filedialog
import subprocess as sub

"""
────────────────────────────────────────────────────────────────────────────────────
─██████─────────██████████████─████████──████████─██████████████─████████████████───
─██░░██─────────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───
─██░░██─────────██░░██████████─████░░██──██░░████─██░░██████████─██░░████████░░██───
─██░░██─────────██░░██───────────██░░░░██░░░░██───██░░██─────────██░░██────██░░██───
─██░░██─────────██░░██████████───████░░░░░░████───██░░██████████─██░░████████░░██───
─██░░██─────────██░░░░░░░░░░██─────██░░░░░░██─────██░░░░░░░░░░██─██░░░░░░░░░░░░██───
─██░░██─────────██░░██████████───████░░░░░░████───██░░██████████─██░░██████░░████───
─██░░██─────────██░░██───────────██░░░░██░░░░██───██░░██─────────██░░██──██░░██─────
─██░░██████████─██░░██████████─████░░██──██░░████─██░░██████████─██░░██──██░░██████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─
─██████████████─██████████████─████████──████████─██████████████─██████──██████████─
────────────────────────────────────────────────────────────────────────────────────
"""
class Token:
    def __init__(self, tokentype, tokenvalue, valuetype_ = None):
        self.tokentype = tokentype
        self.tokenvalue = tokenvalue
        self.valuetype = valuetype_

    def __repr__(self) -> str:
        return f"({self.tokentype}, \"{self.tokenvalue}\")"

def find_tldr(i,line):
    # Regular expression pattern
    pattern = r'(\bTLDR\b)\s*$'

    # Find a match using the pattern
    match = re.search(pattern, line)

    if match:
        return True
    else:
        # Check if TLDR is not found
        if re.search(r'\bTLDR\b', line):
            print("\nCommentError: Words exist after TLDR.")
            print(f"\n\tLine {i+1}: {line}\n")
            sys.exit()        
        else:
            return False

def lexical_analyzer(contents):
    lines = contents.split('\n') # split contents (per line through newline) to the 'lines' list
    print("lines are:", lines)
    lexeme = ""
    items = []
    obtwFound = False
    for i, line in enumerate(lines):
        print(f"i and line is {i+1}: {line}")

        # For Multi-Line Comments 
        
        # Check if OBTW is found
        if obtwFound:
            # Check if TLDR is found
            if find_tldr(i,line):
                obtwFound = False
                # change line to empty string
                lines[i] = ""
                continue
            else:
                # change line to empty string
                lines[i] = ""
                continue
        
        # OBTW
        pattern = r'^\s*(.*?)\bOBTW\b'
        match = re.match(pattern, line)
        if match:
            words_before_obtw = match.group(1).split() # get first OBTW and split to find words before OBTW
            
            # Check if there are words before "OBTW"
            if words_before_obtw:
                
                print("\nCommentError: Words exist before OBTW:", words_before_obtw)
                print(f"\n\tLine {i+1}: {line}\n")
                sys.exit()
            else:
                obtwFound = True
                # change line to empty string
                lines[i] = ""
                continue
        
        
        if line.strip() == "": # if line is empty
            # add an item which is an empty space
            items.append(Token("empty_line", line))
            continue # skip to next line
                
        chars = list(line) # split line to each character in the line to the 'chars' list
        tokens = [] # initialize empty tokens list
        in_quotes = False # initialize in_quotes to false
        
        for char in chars:
            if char == '"':
                if in_quotes: # if in_quotes is true (already second quote)
                    
                    tokens.append(lexeme)  # append the string inside quotes as string literal token
                    lexeme = '' # set lexeme to empty again
                tokens.append(char)  # append the quote '"' itself as a lexeme
                in_quotes = not in_quotes  # if in_quotes is true, set to false, if false, set to true
            elif char == " " and not in_quotes: # in_quotes is false
                # print("lexeme is ", lexeme)
                if lexeme=="I":
                    # [] Keywords with Spaces
                    lexeme += char # append char to lexeme
                elif lexeme=="I HAS":
                    lexeme += char # append char to lexeme
                elif lexeme=="I IZ":
                    tokens.append(lexeme)
                    lexeme = ''
                elif lexeme=="I HAS A":
                    tokens.append(lexeme) # append 'I HAS A' lexeme to tokens list
                    lexeme = '' # set lexeme to empty again 
                elif lexeme=="SUM":
                    lexeme += char
                elif lexeme=="SUM OF":
                    tokens.append(lexeme)
                    lexeme = ''
                elif lexeme=="DIFF":
                    lexeme += char
                elif lexeme == "DIFF OF":
                    tokens.append(lexeme)
                    lexeme = ''
                elif lexeme == "PRODUKT":
                    lexeme += char
                elif lexeme == "PRODUKT OF":
                    tokens.append(lexeme)
                    lexeme = ''
                elif lexeme == "QUOSHUNT":
                    lexeme += char
                elif lexeme == "QUOSHUNT OF":
                    tokens.append(lexeme)
                    lexeme = ''
                elif lexeme == "MOD":
                    lexeme += char
                elif lexeme == "MOD OF":
                    tokens.append(lexeme)
                    lexeme = ''
                elif lexeme == "BIGGR":
                    lexeme += char
                elif lexeme == "BIGGR OF":
                    tokens.append(lexeme)
                    lexeme = ''
                elif lexeme == "SMALLR":
                    lexeme += char
                elif lexeme == "SMALLR OF":
                    tokens.append(lexeme)
                    lexeme = ''
                elif lexeme == "BOTH":
                    lexeme += char
                elif lexeme == "BOTH OF":
                    tokens.append(lexeme)
                    lexeme = ''
                elif lexeme == "EITHER":
                    lexeme += char
                elif lexeme == "EITHER OF":
                    tokens.append(lexeme)
                    lexeme = ''
                elif lexeme == "WON":
                    lexeme += char
                elif lexeme == "WON OF":
                    tokens.append(lexeme)
                    lexeme = ''
                elif lexeme == "ANY":
                    lexeme += char
                elif lexeme == "ANY OF":
                    tokens.append(lexeme) 
                    lexeme = ''
                elif lexeme == "ALL":
                    lexeme += char
                elif lexeme == "ALL OF":
                    tokens.append(lexeme) 
                    lexeme = ''
                elif lexeme == "BOTH":
                    lexeme += char
                elif lexeme == "BOTH SAEM":
                    tokens.append(lexeme) 
                    lexeme = ''
                elif lexeme == "IS":
                    lexeme += char
                elif lexeme == "IS NOW":
                    lexeme += char
                elif lexeme == "IS NOW A":
                    tokens.append(lexeme) 
                    lexeme = ''
                elif lexeme == "O":
                    lexeme += char
                elif lexeme == "O RLY?":
                    tokens.append(lexeme)
                    lexeme = ''
                elif lexeme == "YA":
                    lexeme += char
                elif lexeme == "YA RLY":
                    tokens.append(lexeme)
                    lexeme = ''
                elif lexeme == "NO":
                    lexeme += char
                elif lexeme == "NO WAI":
                    tokens.append(lexeme)
                    lexeme = ''
                elif lexeme == "IM":
                    lexeme += char
                elif lexeme == "IM IN":
                    lexeme += char
                elif lexeme == "IM IN YR":
                    tokens.append(lexeme)
                    lexeme = ''
                elif lexeme == "IM OUTTA":
                    lexeme += char
                elif lexeme == "IM OUTTA YR":
                    tokens.append(lexeme)
                    lexeme = ''
                elif lexeme == "HOW":
                    lexeme += char
                elif lexeme == "HOW IZ":
                    lexeme += char
                elif lexeme == "HOW IZ I":   
                    tokens.append(lexeme)
                    lexeme = ''
                elif lexeme == "IF":
                    lexeme += char  
                elif lexeme == "IF U":
                    lexeme += char
                elif lexeme == "IF U SAY" :
                     lexeme += char    
                elif lexeme == "IF U SAY SO":
                    tokens.append(lexeme)
                    lexeme = ''
                elif lexeme == "FOUND":
                     lexeme += char
                elif lexeme == "FOUND YR":
                    tokens.append(lexeme)
                    lexeme = ''                                  
                else: # if lexeme is not empty
                    #print("ELSE RUNS")
                    if lexeme:
                        tokens.append(lexeme)
                        lexeme = '' # set lexeme to empty again
            else:
                lexeme += char # append char to lexeme
        
        
        if lexeme:
            tokens.append(lexeme)  # append any remaining lexeme as a lexeme
            lexeme = '' # set lexeme to empty again
            
        # add linebreak
        tokens.append("\n")
        
        num_quote = 0
        for j,token in enumerate(tokens):
            if token == '"':
                num_quote += 1
                if num_quote == 2:
                    num_quote = 0
                items.append(Token("string_delimiter", token))
            elif j > 0 and j < len(tokens)-1 and tokens[j+1] == '"' and tokens[j-1] == '"':
                if num_quote == 1:
                    items.append(Token("string_literal", token))
            
            # Comments
            # If comment are seen, show error because it must already be deleted from the start of the program
            elif re.fullmatch(r"BTW", token):
                # items.append(Token("line_comment_delimiter", token))
                # show error message and end program
                print(f"\nCommentError: Wrong BTW Comment Format Detected.\n\tLine {i+1}: {line}\n")
                # end program
                sys.exit()

            elif re.fullmatch(r"OBTW", token):
                # items.append(Token("start_block_comment", token))
                # show error message and end program
                print(f"\nCommentError: Wrong OBTW TLDR Comment Format Detected.\n\tLine {i+1}: {line}\n")
                # end program
                sys.exit()
                
            elif re.fullmatch(r"TLDR", token):
                # items.append(Token("end_block_comment", token))
                # show error message and end program
                print(f"\nCommentError: Wrong OBTW TLDR Comment Format Detected.\n\tLine {i+1}: {line}\n")
                # end program
                sys.exit()
            
            elif re.fullmatch(r"WIN|FAIL", token):
                items.append(Token("troof_literal", token))
            elif re.fullmatch(r"NOOB|NUMBR|NUMBAR|YARN|TROOF", token):
                items.append(Token("type_literal", token))
            elif re.fullmatch(r"HAI", token):
                items.append(Token("start_code_delimiter", token))
            elif re.fullmatch(r"KTHXBYE", token):
                items.append(Token("end_code_delimiter", token))
            
            # Variable Declaration
            elif re.fullmatch(r"WAZZUP", token):
                items.append(Token("start_var_declaration_delimiter", token))
            elif re.fullmatch(r"BUHBYE", token):
                items.append(Token("end_var_declaration_delimiter", token))
            
            elif re.fullmatch(r"I HAS A", token):
                items.append(Token("variable_declaration", token))
            
            elif re.fullmatch(r"ITZ", token):
                items.append(Token("variable_assignment", token))
            
            elif re.fullmatch(r"R", token):
                items.append(Token("variable_value_reassignment", token))
                        
            #Arithmetic/Mathematical Operations
            elif re.fullmatch(r"AN", token):
                items.append(Token("and_keyword", token))
            elif re.fullmatch(r"SUM OF", token):
                items.append(Token("add_keyword", token))
            elif re.fullmatch(r"DIFF OF", token):
                items.append(Token("subtract_keyword", token))
            elif re.fullmatch(r"PRODUKT OF", token):
                items.append(Token("multiply_keyword",token))
            elif re.fullmatch(r"QUOSHUNT OF", token):
                items.append(Token("divide_keyword",token))
            elif re.fullmatch(r"MOD OF", token):
                items.append(Token("modulo_keyword",token))
            elif re.fullmatch(r"BIGGR OF", token):
                items.append(Token("return_larger_number_keyword",token))
            elif re.fullmatch(r"SMALLR OF", token):
                items.append(Token("return_smaller_number_keyword",token))
            #Boolean Operations
            elif re.fullmatch(r"BOTH OF", token):
                items.append(Token("both_true_check_keyword",token))
            elif re.fullmatch(r"EITHER OF", token):
                items.append(Token("both_false_check_keyword",token))
            elif re.fullmatch(r"WON OF", token):
                items.append(Token("exactly_one_is_true_check_keyword",token))
            elif re.fullmatch(r"NOT", token):
                items.append(Token("negate_keyword", token))
            elif re.fullmatch(r"ANY OF", token):
                items.append(Token("atleast_one_true_check_keyword", token))
            elif re.fullmatch(r"ALL OF", token):
                items.append(Token("all_true_check_keyword", token))
            #Comparison Operation Keywords
            elif re.fullmatch(r"BOTH SAEM", token):
                items.append(Token("both_argument_equal_check_keyword", token))
            elif re.fullmatch(r"DIFFRINT", token):
                items.append(Token("both_argument_not_equal_check_keyword", token))
            
            elif re.fullmatch(r"SMOOSH", token):
                items.append(Token("concatenation_keyword", token))
            elif re.fullmatch(r"MAEK", token):
                items.append(Token("typecast_keyword", token))
            elif re.fullmatch(r"A", token):
                items.append(Token("typecast_prefix", token))
            elif re.fullmatch(r"IS NOW A", token): 
                items.append(Token("full_typecast_keyword", token))
            #Input/Output Keyword
            elif re.fullmatch(r"VISIBLE", token):
                items.append(Token("print_keyword", token))
            elif re.fullmatch(r"GIMMEH", token):
                items.append(Token("input_keyword", token))
            #Flow-control Keywords
            elif re.fullmatch(r"O RLY\?", token):
                items.append(Token("if_keyword", token))
            elif re.fullmatch(r"YA RLY", token):
                items.append(Token("if_true_keyword", token))
            elif re.fullmatch(r"MEBBE", token):
                items.append(Token("else_if_keyword", token))
            elif re.fullmatch(r"NO WAI", token):
                items.append(Token("else_keyword", token))
            elif re.fullmatch(r"OIC", token):
            #Switch-case keywods
                items.append(Token("end_of_if_block_keyword", token))    
            elif re.fullmatch(r"WTF\?", token):
                items.append(Token("switch_keyword", token))     
            elif re.fullmatch(r"OMG", token):
                items.append(Token("switch_case_keyword", token))   
            elif re.fullmatch(r"OMGWTF", token):
                items.append(Token("switch_default_keyword", token))
            #Loop related keywords/ Inc and Dec
            elif re.fullmatch(r"IM IN YR", token):
                items.append(Token("explicit_start_loop_keyword", token))
            elif re.fullmatch(r"UPPIN", token):
                items.append(Token("increment_keyword",token)) 
            elif re.fullmatch(r"NERFIN", token):
                items.append(Token("decrement_keyword", token))   
            elif re.fullmatch(r"YR", token):
                items.append(Token("concise_start_loop_keyword", token))   
            elif re.fullmatch(r"TIL", token):
                items.append(Token("until_indicated_end_of_loop_keyword", token))
            elif re.fullmatch(r"WILE", token):
                items.append(Token("while_indicated_end_of_loop_keyword", token))   
            elif re.fullmatch(r"IM OUTTA YR", token):
                items.append(Token("break_loop_keyword", token))
            #Function/Assignment keywords
            elif re.fullmatch(r"HOW IZ I", token):
                items.append(Token("define_function_keyword", token))
            elif re.fullmatch(r"IF U SAY SO", token):
                items.append(Token("end_of_function_keyword", token))
            elif re.fullmatch(r"GTFO", token):
                items.append(Token("general_purpose_break_keyword", token))
            elif re.fullmatch(r"FOUND YR", token):
                items.append(Token("return_keyword", token))
            elif re.fullmatch(r"I IZ", token):
                items.append(Token("function_call", token))
            elif re.fullmatch(r"MKAY", token):
                items.append(Token("end_of_assignment_keyword", token))

            # VARIABLE IDENTIFIERS
            elif re.fullmatch(r"[a-zA-Z][a-zA-Z0-9_]*", token):
                items.append(Token("variable_identifier", token))
            # NUMBR LITERAL
            elif re.fullmatch(r"-?([1-9][0-9]*|0)", token):
                items.append(Token("numbr_literal", int(token)))
            # NUMBAR LITERAL
            elif re.fullmatch(r"-?(0|[1-9][0-9]*)(\.[0-9]+)?", token):
                items.append(Token("numbar_literal", float(token)))
            
            # ADDED LEXEMES FROM GRAMMAR
            elif re.fullmatch(r"\n", token):
                items.append(Token("linebreak", "\\n"))
            elif re.fullmatch(r"", token):
                items.append(Token("epsilon", token))
            elif re.fullmatch(r".*", token):
                items.append(Token("any", token))
            else:
                print(f"InvalidTokenError: Invalid Token Detected.\n\tLine {i+1}: {line}\n\tToken: {token}")
                sys.exit()    

    # print items separated by newline
    for item in items:
        print(item)
                    
    return items

def parse(file):
    contents = open(file, 'r').read()
    print(repr(contents))
    contents = re.sub(r"(?<!O)BTW.*?(?=\n)", "", contents) # remove comments by deleting BTW and after it before \n
    
    #print("REVISED CONTENTS ARE:\n", result)
    tokens = lexical_analyzer(contents)
    return tokens

# ______________________________________________________________________________________________________________
# -------------------------------------------[  PARSER ]--------------------------------------------------------
"""
───────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─████████████████───██████████████─██████████████─████████████████───
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───
─██░░██████░░██─██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░████████░░██───
─██░░██──██░░██─██░░██──██░░██─██░░██────██░░██───██░░██─────────██░░██─────────██░░██────██░░██───
─██░░██████░░██─██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░████████░░██───
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───
─██░░██████████─██░░██████░░██─██░░██████░░████───██████████░░██─██░░██████████─██░░██████░░████───
─██░░██─────────██░░██──██░░██─██░░██──██░░██─────────────██░░██─██░░██─────────██░░██──██░░██─────
─██░░██─────────██░░██──██░░██─██░░██──██░░██████─██████████░░██─██░░██████████─██░░██──██░░██████─
─██░░██─────────██░░██──██░░██─██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─
─██████─────────██████──██████─██████──██████████─██████████████─██████████████─██████──██████████─
───────────────────────────────────────────────────────────────────────────────────────────────────
"""


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
errorMessage = ""
    
def advance():
    global token_idx, current_token
    if token_idx < len(tokens):
        token_idx += 1
        current_token = tokens[token_idx]

class Error(Exception):
    def __init__(self, message=None):
        self.message = message
        super().__init__(message)
        
def error(msg, line):
    # use Error class
    errorMessage = "{} : Line {}".format(msg,line)
    raise Error(errorMessage)

def if_linebreak():
    global current_token, current_line
    if current_token.tokentype == "linebreak":
        current_line += 1
        advance()
        skip_empty_lines()
    else:
        error("[SyntaxError] Linebreak expected after statement", current_line)
        
def program():
    global current_token, current_line
    nodes = []
    if current_token.tokentype == "start_code_delimiter":
        nodes.append(("START",current_token))
        advance()
        if_linebreak()
        # [] functions
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

def skip_empty_lines():
    global current_token, current_line
    while current_token.tokentype == "empty_line":
        advance() # skip empty lines
        current_line += 1

def var_declaration_list(): 
    global current_token, current_line
    nodes = []
    while current_token.tokentype != "end_var_declaration_delimiter":
        node = var_declaration()
        if node is not None:
            nodes.append(node)
        if_linebreak()
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
        
        elif current_token.tokentype == "full_typecast_keyword": # changing the type of the variable
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
            if re.fullmatch(yarn_pattern, var_value):
                print("var_value:", var_value)
                var_value = re.sub(r'\.\d+', '', var_value)
                variables[var_name] = int(var_value)
            else:
                error(f"[RuntimeError] Invalid String. Cannot convert '{var_value}' to NUMBR", current_line)
        elif isinstance(var_value, float):
            variables[var_name] = int(var_value)
        elif isinstance(var_value, int):
            variables[var_name] = var_value
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
        elif isinstance(var_value, float):
            variables[var_name] = var_value
        elif isinstance(var_value, int):
            variables[var_name] = float(var_value)
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


# ______________________________________________________________________________________________________________
# -------------------------------------------[  GUI ]-----------------------------------------------------------
"""
──────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████──██████─██████████────██████████████─██████──██████─██████████─
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░██────██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░██─
─██░░██████████─██░░██──██░░██─████░░████────██░░██████████─██░░██──██░░██─████░░████─
─██░░██─────────██░░██──██░░██───██░░██──────██░░██─────────██░░██──██░░██───██░░██───
─██░░██─────────██░░██──██░░██───██░░██──────██░░██─────────██░░██──██░░██───██░░██───
─██░░██──██████─██░░██──██░░██───██░░██──────██░░██──██████─██░░██──██░░██───██░░██───
─██░░██──██░░██─██░░██──██░░██───██░░██──────██░░██──██░░██─██░░██──██░░██───██░░██───
─██░░██──██░░██─██░░██──██░░██───██░░██──────██░░██──██░░██─██░░██──██░░██───██░░██───
─██░░██████░░██─██░░██████░░██─████░░████────██░░██████░░██─██░░██████░░██─████░░████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░██────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░██─
─██████████████─██████████████─██████████────██████████████─██████████████─██████████─
──────────────────────────────────────────────────────────────────────────────────────
"""

# Global Vairables ===
fileLoaded = False
file_path = ""
tokens = []
# ====================

# Color ======
bgcolor1 = "#C9E4DE"
bgcolor2 = "#BDE0FE"
bgcolor3 = "#FFDAC1"
bgcolor4 = "#FFE1E9"
bgcolor5 = "#55CBCD"
# ============

# Font =======
defaultFont = ("Microsoft YaHei UI", 8, "normal")
labelFont = ("Microsoft YaHei UI", 8, "bold") 
texteditorFont = ("Courier New", 10, "normal") 
# ============

# GUI Functions ===============
# Events
def on_resize(event):
    width = root.winfo_width()
    height = root.winfo_height()
    topFrame.configure(width=width, height=height // 2)
    bottomFrame.configure(width=width, height=height // 2)

        
def insert_spaces(event):
    textEditor.insert(tk.INSERT, " " * 4)
    return 'break'

# Program Functions
def open_file():
    global fileLoaded, file_path
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Lolcode files", "*.lol"), ("All files", "*.*")])
    file = open(file_path, "r")
    if file_path != "":
        fileLoaded = True
        filepathText.config(state=tk.NORMAL)
        filepathText.delete("1.0","end")
        filepathText.insert(tk.END, file_path)
        filepathText.config(state=tk.DISABLED)
        textEditor.insert("1.0",file.read())
        textEditor.config(state=tk.DISABLED)
        file.close()
        read_file_lexical()
        read_file_parser()
        
def read_file_lexical(file_path):
    global tokens
    tokens = parse(file_path)
    print(tokens)
    for token in tokens:
        if token.tokentype != "linebreak" and token.tokentype != "empty_line":
            lexemeTable.insert("", "end", values=(token.tokenvalue, token.tokentype))

def read_file_parser():
    global tokens
    _, variableDictionary = do_parse_tree(tokens)
    # get the key and value from the dictionary
    print(variableDictionary)
    for key, value in variableDictionary.items():
        print(key, value)
        symbolTable.insert("", "end", values=(key, value))
    
def execute_code():
    pass
    # global tokens, file_path
    # if fileLoaded == True:
    #     print("filepath is ", file_path)
    #     filename_quoted = shlex.quote(file_path)
    #     command = f"python ./syntax.py {filename_quoted}"
    #     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    #     output, error = process.communicate()

    #     print(output.decode())
    #     print(error.decode())
    #     # parse_tree = do_parse_tree(tokens)

    #     # output = sys.stdout

    #     outputText.insert('1.0', output.decode())

    #     sys.stdout = output

# =============================

root = tk.Tk()
root.title("The Lords of the Strings LOLCODE Interpreter")
root.geometry('1300x700')
root.minsize(1300,700)

font.nametofont("TkDefaultFont").configure(family=defaultFont[0], size=defaultFont[1])

topFrame = tk.Frame(root, bg=bgcolor1)
bottomFrame = tk.Frame(root, bg=bgcolor4)

# Top Frame =====
# Text Editor
textEditorFrame = tk.Frame(topFrame, width=400,bg=bgcolor1)
openfileUI = tk.Frame(textEditorFrame)
filepathText = tk.Text(openfileUI, height = 1, width=54)
openfileButton = tk.Button(openfileUI, text="Open", command=open_file)
filepathText.configure(state=tk.DISABLED)

textEditFrame = tk.Frame(textEditorFrame)
textEditor = tk.Text(textEditFrame, height = 10, width = 60, wrap='none', font=texteditorFont)

textEditorvsb = ttk.Scrollbar(textEditFrame, orient="vertical", command=textEditor.yview)
textEditor.configure(yscrollcommand=textEditorvsb.set)
textEditorvsb.pack(side=tk.RIGHT, fill=tk.Y)

textEditorhsb = ttk.Scrollbar(textEditFrame, orient="horizontal", command=textEditor.xview)
textEditor.configure(xscrollcommand=textEditorhsb.set)
textEditorhsb.pack(side=tk.BOTTOM, fill=tk.X)

openfileButton.pack(side=tk.RIGHT, fill=tk.X, expand=False)
filepathText.pack(side=tk.RIGHT, fill=tk.X, expand=True)
openfileUI.pack(side=tk.TOP, fill=tk.X, expand=False)
textEditor.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

textEditFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
textEditorFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Lexemes Table
lexemeFrame = tk.Frame(topFrame, width=300, bg=bgcolor3)
lexemeTableLabel = tk.Label(lexemeFrame, text="Lexeme Table", bg=bgcolor3, font=labelFont)

lexemeTableFrame = tk.Frame(lexemeFrame, width=300, bg=bgcolor3)

lexemeTable = ttk.Treeview(lexemeTableFrame, columns=("lexeme", "classification"), show='headings')
lexemeTable.heading("lexeme", text="Lexeme")
lexemeTable.heading("classification", text="Classification")

lexemevsb = ttk.Scrollbar(lexemeTableFrame, orient="vertical", command=lexemeTable.yview)
lexemeTable.configure(yscrollcommand=lexemevsb.set)
lexemevsb.pack(side=tk.RIGHT, fill=tk.Y)

lexemeTableLabel.pack(side=tk.TOP)
lexemeTable.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
lexemeTableFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

lexemeFrame.pack(side=tk.LEFT, fill=tk.BOTH,expand=True)

# Symbol Table
symbolFrame = tk.Frame(topFrame, width=300, bg=bgcolor2)
symbolTableLabel = tk.Label(symbolFrame, text="Symbol Table", bg=bgcolor2, font=labelFont)

symbolTableFrame = tk.Frame(symbolFrame, width=300, bg=bgcolor2)

symbolTable = ttk.Treeview(symbolTableFrame, columns=("identifier", "value"), show='headings')
symbolTable.heading("identifier", text="Identifier")
symbolTable.heading("value", text="Value")

symbolvsb = ttk.Scrollbar(symbolTableFrame, orient="vertical", command=symbolTable.yview)
symbolTable.configure(yscrollcommand=symbolvsb.set)
symbolvsb.pack(side=tk.RIGHT, fill=tk.Y)

symbolTableLabel.pack(side=tk.TOP)
symbolTable.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
symbolTableFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

symbolFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
# ===============

# Bottom Frame ==
executeButton = tk.Button(bottomFrame, text="EXECUTE", font=labelFont, command=execute_code)
executeButton.pack(side=tk.TOP, fill=tk.X)

outputFrame = tk.Frame(bottomFrame, bg=bgcolor4)
outputText = tk.Text(outputFrame, height = 10, width = 60, wrap='none', font=texteditorFont)
outputTextvsb = ttk.Scrollbar(outputFrame, orient="vertical", command=outputText.yview)
outputText.configure(yscrollcommand=outputTextvsb.set)
outputTextvsb.pack(side=tk.RIGHT, fill=tk.Y)
outputTexthsb = ttk.Scrollbar(outputFrame, orient="horizontal", command=outputText.xview)
outputText.configure(xscrollcommand=outputTexthsb.set)
outputTexthsb.pack(side=tk.BOTTOM, fill=tk.X)
outputText.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
outputFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
outputText.configure(state=tk.DISABLED)

# Console Try
"""
>> Temporary Solution for Console Input
[] .configure when there is VISIBLE or Error()
[] Pop up and ask user input, when button is clicked, value is stored in variable
"""

# outputText = Console(outputFrame, height = 10, width = 60, wrap='none', font=texteditorFont)
# outputText.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# ===============

topFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
bottomFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Event Binds
textEditor.bind("<Tab>", insert_spaces)
# root.bind('<Configure>', on_resize) 

# print(font.families())
root.mainloop()

if __name__ == '__main__':
    tokens = parse(sys.argv[1])
    print(tokens)
    parse_tree = syntax_analyzer()
    print(variables)
    print(("PROGRAM",parse_tree))