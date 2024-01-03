from typing import Concatenate
import regex as re
import sys
import math
import tkinter as tk
from tkinter import font, ttk, filedialog, simpledialog
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
            error(f"[CommentError] Wrong OBTW TLDR Comment Format Detected. {line}", i+1)    
        else:
            return False

def lexical_analyzer(contents):
    lines = contents.split('\n') # split contents (per line through newline) to the 'lines' list
    # print("lines are:", lines)
    lexeme = ""
    items = []
    obtwFound = False
    for i, line in enumerate(lines):
        # print(f"i and line is {i+1}: {line}")

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
                
                error(f"[CommentError] Wrong OBTW TLDR Comment Format Detected. {line}", i+1)
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
        
        print(tokens)
        # add linebreak
        tokens.append("\n")
        
        num_quote = 0
        for j,token in enumerate(tokens):
            if token == '"':
                num_quote += 1
                if num_quote == 2:
                    num_quote = 0
                items.append(Token("string_delimiter", token))
            elif j > 0 and j < len(tokens)-1 and num_quote == 1 and tokens[j+1] == '"' and tokens[j-1] == '"':
                items.append(Token("string_literal", token))
            
            # Comments
            # If comment are seen, show error because it must already be deleted from the start of the program
            elif re.fullmatch(r"BTW", token):
                # items.append(Token("line_comment_delimiter", token))
                # show error message and end program
                error(f"[CommentError] Wrong OBTW TLDR Comment Format Detected. {line}", i+1)

            elif re.fullmatch(r"OBTW", token):
                # items.append(Token("start_block_comment", token))
                # show error message and end program
                error(f"[CommentError] Wrong OBTW TLDR Comment Format Detected. {line}", i+1)  
            elif re.fullmatch(r"TLDR", token):
                # items.append(Token("end_block_comment", token))
                # show error message and end program
                error(f"[CommentError] Wrong OBTW TLDR Comment Format Detected. {line}", i+1)            
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
                error(f"[LexerError] Invalid Token Detected. {line}", i+1)

    # print items separated by newline
    for item in items:
        print(item)
                    
    return items

# parse function for terminal-based
def parse_terminal(file):
    # reset variables
    
    contents = open(file, 'r').read()
    # print(repr(contents)) # printable representation of contents
    contents = re.sub(r"(?<!O)BTW.*?(?=\n)", "", contents) # remove comments by deleting BTW and after it before \n
    
    #print("REVISED CONTENTS ARE:\n", result)
    tokens = lexical_analyzer(contents)
    return tokens

# parse function for GUI-based
def parse_tkinter(code):
    print(repr(code)) # printable representation of contents
    code = re.sub(r"(?<!O)BTW.*?(?=\n)", "", code) # remove comments by deleting BTW and after it before \n
    
    #print("REVISED CONTENTS ARE:\n", result)
    tokens = lexical_analyzer(code)
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
                    "typecast_keyword",
                    "return_larger_number_keyword", 
                    "return_smaller_number_keyword", 
                    "both_true_check_keyword", 
                    "both_false_check_keyword", 
                    "exactly_one_is_true_check_keyword", 
                    "negate_keyword", 
                    "atleast_one_true_check_keyword", 
                    "all_true_check_keyword",
                    "both_argument_equal_check_keyword", 
                    "both_argument_not_equal_check_keyword",
                    "concatenation_keyword"
                    ]

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

flow_control_tokens = ["explicit_start_loop_keyword",
                       "if_keyword",
                       "switch_keyword"]

class Variable:
    def __init__(self, name, value, valuetype_ = None):
        self.name = name
        self.value = value
        self.valuetype = valuetype_

    def __repr__(self) -> str:
        return f"({self.type}, \"{self.value}\", {self.valuetype})"

variables = {'IT': None}
var_assign_ongoing = False # checker for expressions if to be placed in IT

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
        print(current_token)

class Error(Exception):
    def __init__(self, message=None):
        self.message = message
        super().__init__(message)
        
def error(msg, line):
    # use Error class
    errorMessage = "{} : Line {}".format(msg,line)
    insert_output(errorMessage)
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
    skip_empty_lines()
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
        update_symbol_table() # update symbol table
        if node is not None:
            nodes.append(node)
        if_linebreak()
    return nodes

def var_declaration():
    global current_token, current_line, var_assign_ongoing
    var_assign_ongoing = True # assignment ongoing
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
                    var_assign_ongoing = False # set back to false
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
                    var_assign_ongoing = False # set back to false
                    return ("VARIABLE", varident, literal_)      
            # [] to add expressions (arith)   
            elif current_token.tokentype == "linebreak": # I HAS A var (only, no ITZ) - untyped or uninitialized variable
                variables[varident] = None # null value
                var_assign_ongoing = False # set back to false
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

# tkinter pop up gui for user input (GIMMEH)
def popup_input(varident_):
    global variables
    user_input = simpledialog.askstring("Input", f"GIMMEH {varident_.tokenvalue}:")
    if user_input is None:
        variables[varident_.tokenvalue] = ""
    else:
        variables[varident_.tokenvalue] = user_input
    update_symbol_table()
    print("User input:", user_input)


# only the syntax --- to edit
def function_call():
    global current_token
    if current_token.tokentype == "define_function_keyword":
        advance() # pass HOW IZ I
        if current_token.tokentype == "variable_identifier":
            advance() # pass function name
            statementList = statement_list()
            if current_token.tokentype == "end_of_function_keyword":
                advance() # pass IF U SAY SO     
                return ("FUNCTION", statementList)
            else:
                error("[SyntaxError] Invalid end of function (IF U SAY SO)", current_line)
        else:
            error("[SyntaxError] Invalid function name", current_line)
    else:
        error("[SyntaxError] Invalid function call (HOW IZ I)", current_line)

def place_in_IT(value):
    global variables
    variables["IT"] = value
    update_symbol_table()
    
def semi_typecast_expression():
    new_value = None
    advance() # pass MAEK
    var_token = varident() # var
    # may or may not include A typecast_prefix
    if current_token.tokentype != "typecast_prefix" and current_token.tokentype != "type_literal":
        error("[SyntaxError: Invalid typecast: Line", current_line)
    else:
        if current_token.tokentype == "typecast_prefix":
            advance() # pass A
        new_value = handle_semi_typecast(var_token.tokenvalue, current_token.tokenvalue, current_line)
        advance() # pass NUMBAR/NUMBR/TROOF/YARN              
    return new_value  # to not print parse tree in var R MAEK var TYPE

def statement():
    global current_token, var_assign_ongoing
    if current_token.tokentype == "print_keyword": # to add + in VISIBLE (concatenation)
        advance() # pass VISIBLE
        expr_ = print_expression()
        return ("PRINT", expr_)  
    elif current_token.tokentype == "input_keyword":
        advance() # pass GIMMEH
        varident_ = varident()
        # pop up tkinter input box
        popup_input(varident_)
        print("variables is now:", variables)

        return ("INPUT", varident_)
    elif current_token.tokentype == "variable_identifier": #assignment statement
        var_assign_ongoing = True # variable assignment ongoing
        var_dest_token = varident()
        if current_token.tokentype == "variable_value_reassignment":
            advance() # pass R
            if current_token.tokentype == "variable_identifier": # var = var
                var_src_token = varident()
                variables[var_dest_token.tokenvalue] = variables[var_src_token.tokenvalue]
                update_symbol_table()
                var_assign_ongoing = False # set back to false, variable reassignment done
                return ("ASSIGN", var_dest_token, var_src_token)
            elif current_token.tokentype in ["numbr_literal", "numbar_literal", "troof_literal", "string_delimiter"]: # var = literal
                lit_src_token = literal()
                variables[var_dest_token.tokenvalue] = lit_src_token.tokenvalue
                update_symbol_table()
                var_assign_ongoing = False # set back to false, variable reassignment done
                return ("ASSIGN", var_dest_token, lit_src_token)
            elif current_token.tokentype in expression_tokens: # var = expression
                expr_val = expression()
                variables[var_dest_token.tokenvalue] = expr_val
                update_symbol_table()
                var_assign_ongoing = False # set back to false, variable reassignment done
                return ("ASSIGN", var_dest_token, expr_val)
            else:
                error("[SyntaxError] Invalid variable value reassignment", current_line)
        elif current_token.tokentype == "full_typecast_keyword": # changing the type of the variable
            advance() # pass IS NOW A
            if current_token.tokentype == "type_literal":
                type_literal_ = current_token
                handle_full_typecast(varidentDest, type_literal_.tokenvalue, current_line)
                advance() # pass NUMBAR/NUMBR/TROOF/YARN
                update_symbol_table()
                var_assign_ongoing = False # set back to false, variable reassignment done
                return("FULL_TYPECAST", varidentDest, type_literal_)
            else:
                error("[SyntaxError] Invalid typecast literal", current_line)
        else:
            error("[SyntaxError] Invalid variable value reassignment. R not found. ", current_line)

    
    elif current_token.tokentype in flow_control_tokens:  #FLOW CONTROL
        if current_token.tokentype == "explicit_start_loop_keyword": #IM IN YR
            node = loop()
        elif current_token.tokentype == "if_keyword":
            if_else_statement()
    # elif current_token.tokentype == "general_purpose_break_token": #GTFO

    # elif cuurent_token.tokentype == "return keyword": #FOUND YR    
    
    # else check if expression (can also be a statement)
    else:
        if current_token.tokentype in expression_tokens:
            expression_ = expression()
            return expression_

        else:
            error("[SyntaxError] Invalid statement", current_line)

def expression():
    global current_token, current_line, var_assign_ongoing
    ans = None
    if current_token.tokentype in arith_tokens:
        ans = arithmetic_expression() 
    elif current_token.tokentype == "typecast_keyword":
        ans = semi_typecast_expression()
    elif current_token.tokentype in comp_tokens:
        ans = compare_expression()
    elif current_token.tokentype in bool_tokens:
        ans = boolean_expression()
    # smoosh also an expr (x R SMOOSH x AN y; var = expr)
    elif current_token.tokentype == "concatenation_keyword": #SMOOSH
        advance()
        if current_token.tokentype in ["numbr_literal", "numbar_literal", "troof_literal", "string_delimiter"]:
            ans = ""
            while current_token.tokentype != "linebreak":
                lit_token = literal()
                ans = ans + lit_token.tokenvalue
                if current_token.tokentype == "and_keyword":
                    advance()
                elif current_token.tokentype == "linebreak":
                    break
                else:
                    error("[SyntaxError] : no AN keyword detected", current_line)
            print(ans)
        else:
            error("[SyntaxError] Invalid literal: Line", current_line)
    print("var_assign_ongoing is:", var_assign_ongoing)
    if var_assign_ongoing == False: # place in IT variable if not a variable assignment statement
        print("THIS IS RUNNNNNNNNNNNINGGGGGGGGGGGGGG")
        place_in_IT(ans)
    return ans

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
    if current_token.tokentype in ["add_keyword","subtract_keyword","multiply_keyword","divide_keyword","modulo_keyword", "return_larger_number_keyword", "return_smaller_number_keyword"]:
        operationType = current_token.tokentype # save operation type
        advance() # pass SUM OF
        
        # left operand # operand can be a variable, numbar, numbr, string, troof  
        if current_token.tokentype in expression_tokens:
            left = expression()
        elif current_token.tokentype in ["numbr_literal","numbar_literal"]:
            left = current_token.tokenvalue
            advance() # pass LEFT OPERAND
        elif current_token.tokentype == "string_delimiter":
            advance() # pass starting "
            if current_token.tokentype == "string_literal":
                left = typecast_string(current_token.tokenvalue)
                advance() # pass string literal
                if current_token.tokentype != "string_delimiter":
                    error("[Syntax Error] String delimiter expected", current_line)
                advance() # pass closing "
            else:
                error("[Syntax Error] Invalid string literal", current_line)
        elif current_token.tokentype == "troof_literal":
            left = typecast_troof(current_token.tokenvalue)
            advance() # pass LEFT OPERAND
        elif current_token.tokentype == "variable_identifier":
            if current_token.tokenvalue in variables.keys() and variables[current_token.tokenvalue] is not None:
                if isinstance(variables[current_token.tokenvalue], str): # check if string
                    left = typecast_string(variables[current_token.tokenvalue])
                left = variables[current_token.tokenvalue]
                advance() # pass LEFT OPERAND
            else:
                error("[Logic Error] Variable not found", current_line)
        else:
            error("[Syntax Error] Invalid operand", current_line)
        
        if current_token.tokentype == "and_keyword":
            advance() # pass AN
            #right operand
            if current_token.tokentype in expression_tokens:
                right = expression()
            elif current_token.tokentype in ["numbr_literal","numbar_literal"]:
                right = current_token.tokenvalue
                advance()
            elif current_token.tokentype == "string_delimiter":
                advance() # pass starting "
                if current_token.tokentype == "string_literal":
                    right = typecast_string(current_token.tokenvalue)
                    advance() # pass string literal
                    if current_token.tokentype != "string_delimiter":
                        error("[Syntax Error] String delimiter expected", current_line)
                    advance()
                else:
                    error("[Syntax Error] Invalid string literal", current_line)
            elif current_token.tokentype == "troof_literal":
                right = typecast_troof(current_token.tokenvalue)
                advance()
            elif current_token.tokentype == "variable_identifier":
                if current_token.tokenvalue in variables.keys() and variables[current_token.tokenvalue] is not None:
                    if isinstance(variables[current_token.tokenvalue], str):
                        right = typecast_string(variables[current_token.tokenvalue])
                    right = variables[current_token.tokenvalue]
                    advance()
                else:
                    error("[Logic Error] Variable value not found", current_line)
            else:
                error("[Syntax Error] Invalid operand", current_line)            
           
            if left is None or right is None: # OPERAND NOT TYPECAST-ABLE
                error("[Runtime Error] Cannot perform operation. Invalid operand.", current_line)
            elif operationType == "add_keyword": # ADD OPERATION
                result = left + right
                print(result)
                # advance() # pass RIGHT OPERAND (?)
                return result
            elif operationType == "subtract_keyword":
                result = left - right
                print(result)
                # advance() # pass RIGHT OPERAND (?)
                return result
            elif operationType == "multiply_keyword":
                result = left * right
                print(result)
                # advance() # pass RIGHT OPERAND (?)
                return result
            elif operationType == "divide_keyword":
                if right != 0:
                    result = left / right
                else:
                    error("[Arithmetic Error] Cannot divide by zero", current_line)
                print(result)
                # advance() # pass RIGHT OPERAND (?)
                return result
            elif operationType == "modulo_keyword":
                result = left % right
                print(result)
                return result
            elif operationType == "return_larger_number_keyword":
                if left > right:
                    result = left
                elif left < right:
                    result = right
                else:
                    result = left
                print(result)
                return result 
            elif operationType == "return_smaller_number_keyword":
                if left > right:
                    result = right
                elif left < right:
                    result = left
                else:
                    result = left
                print(result)
                return result 
            else:
                error("[Syntax Error] Invalid arithmetic operation", current_line)
        else:
            error("[Syntax Error] AN keyword not found", current_line)
    else:
        error("[Syntax Error] Incorrect Arithmetic Expression", current_line)
    
def compare_expression():
    global current_token, current_line
    if current_token.tokentype in ["both_argument_equal_check_keyword", "both_argument_not_equal_check_keyword"]: 
        comparisonType = current_token.tokentype #save comparison type
        advance() # pass BOTH SAEM/DIFFRINT

        # left operand # operand can be a variable, numbar, numbr, string, troof  
        if current_token.tokentype in expression_tokens:
            left = expression()
        elif current_token.tokentype in ["numbr_literal","numbar_literal"]:
            left = current_token.tokenvalue
            advance()
        elif current_token.tokentype == "string_delimiter":
            advance() # pass starting "
            if current_token.tokentype == "string_literal":
                left = current_token.tokenvalue
                advance() # pass string literal
                if current_token.tokentype != "string_delimiter":
                    error("[Syntax Error] String delimiter expected", current_line)
                advance() # pass closing "
            else:
                error("[Syntax Error] Invalid string literal", current_line)
        elif current_token.tokentype == "troof_literal":
            left = current_token.tokenvalue
            advance() # pass LEFT OPERAND
        elif current_token.tokentype == "variable_identifier":
            if current_token.tokenvalue in variables.keys() and variables[current_token.tokenvalue] is not None:
                left = variables[current_token.tokenvalue]
                advance() # pass LEFT OPERAND
            else:
                error("[Logic Error] Variable not found", current_line)
        else:
            error("[Syntax Error] Invalid operand", current_line)

        if current_token.tokentype == "and_keyword":
            advance() # pass AN
            #right operand
            if current_token.tokentype in expression_tokens:
                right = expression()
            elif current_token.tokentype in ["numbr_literal","numbar_literal"]:
                right = current_token.tokenvalue
                advance()
            elif current_token.tokentype == "string_delimiter":
                advance() # pass starting "
                if current_token.tokentype == "string_literal":
                    right = current_token.tokenvalue
                    advance() # pass string literal
                    if current_token.tokentype != "string_delimiter":
                        error("[Syntax Error] String delimiter expected", current_line)
                    advance()
                else:
                    error("[Syntax Error] Invalid string literal", current_line)
            elif current_token.tokentype == "troof_literal":
                right = current_token.tokenvalue
                advance()
            elif current_token.tokentype == "variable_identifier":
                if current_token.tokenvalue in variables.keys() and variables[current_token.tokenvalue] is not None:
                    right = variables[current_token.tokenvalue]
                    advance()
                else:
                    error("[Logic Error] Variable not found", current_line)
            else:
                error("[Syntax Error] Invalid operand", current_line)            
           
            if left is None or right is None: # OPERAND NOT TYPECAST-ABLE
                error("[Runtime Error] Cannot perform operation. Invalid operand.", current_line)
              
            elif comparisonType == "both_argument_equal_check_keyword": # Equal to ==
                result = "WIN" if left == right and type(left) == type(right) else "FAIL"
                print("RESULT", result)
                return result
            elif comparisonType == "both_argument_not_equal_check_keyword": # Equal to !=
                result = "WIN" if left != right else "FAIL"
                print("RESULT", result)
                return result  
            else:
                error("[Syntax Error] Invalid Comparison operation", current_line)  
        else:
            error("[Syntax Error] AN keyword not found", current_line)


def boolean_expression():
    global current_token, current_line
    has_allOf_anyOf = 0
    infinite_arr = []

    if current_token.tokentype in ["both_true_check_keyword", "both_false_check_keyword", "exactly_one_is_true_check_keyword", "negate_keyword", "atleast_one_true_check_keyword", "all_true_check_keyword"]:
        operationType = current_token.tokentype #save boolean operation
        print("CHECK",current_token.tokentype)
        advance()

        #ALL OF and ANY OF existence check (since can't be nested into each other or themselves)
        if operationType in ["atleast_one_true_check_keyword", "all_true_check_keyword"]: 
            has_allOf_anyOf += 1

        #NOT
        if operationType in ["negate_keyword"]: 
            if current_token.tokentype in expression_tokens:
                op = expression()
            elif current_token.tokentype in ["numbr_literal","numbar_literal"]:
                op = current_token.tokenvalue
                if op == 0:
                    new_value = "FAIL"
                else:
                    new_value = "WIN"
                op = new_value
                advance()
            elif current_token.tokentype == "string_delimiter":
                advance()
                if current_token.tokentype == "string_literal":
                    op = current_token.tokenvalue
                    if op == "":
                        new_value = "FAIL"
                    else:
                        new_value = "WIN"
                    op = new_value
                    advance() #pass string literal
                    if current_token.tokentype != "string_delimiter":
                        error("[Syntax Error] String delimiter expected", current_line)
                    advance()
                else:
                    error("[Syntax Error] Invalid string literal", current_line)
            elif current_token.tokentype == "troof_literal":
                op = current_token.tokenvalue
                advance() # pass LEFT OPERAND
            elif current_token.tokentype == "variable_identifier":
                if current_token.tokenvalue in variables.keys() and variables[current_token.tokenvalue] is not None:
                    op = variables[current_token.tokenvalue]
                    if op == 0:
                        new_value = "FAIL"
                    elif op == "":
                        new_value = "FAIL"
                    else:
                        new_value = "WIN"
                    op = new_value
                    advance()
                else:
                    error("[Logic Error] Variable not found", current_line)
            else:
                error("[Syntax Error] Invalid operand", current_line)


            if op is None: # OPERAND NOT TYPECAST-ABLE
                error("[Runtime Error] Cannot perform operation. Invalid operand.", current_line)
            elif op == "WIN":
                result = "FAIL"
                return result
            elif op == "FAIL":
                result = "WIN"
                return result
            else:
                error("[Syntax Error] Invalid Boolean operation", current_line)  

        #BOTH OF, EITHER OF, WON OF
        elif operationType in ["both_true_check_keyword", "both_false_check_keyword", "exactly_one_is_true_check_keyword"]:
            if current_token.tokentype in expression_tokens:
                left = expression()
            elif current_token.tokentype in ["numbr_literal","numbar_literal"]:
                left = current_token.tokenvalue
                if left == 0:
                    new_value = "FAIL"
                else:
                    new_value = "WIN"
                left = new_value
                advance()
            elif current_token.tokentype == "string_delimiter":
                advance()
                if current_token.tokentype == "string_literal":
                    left = current_token.tokenvalue
                    if left == "":
                        new_value = "FAIL"
                    else:
                        new_value = "WIN"
                    left = new_value
                    advance() #pass string literal
                    if current_token.tokentype != "string_delimiter":
                        error("[Syntax Error] String delimiter expected", current_line)
                    advance()
                else:
                    error("[Syntax Error] Invalid string literal", current_line)
            elif current_token.tokentype == "troof_literal":
                left = current_token.tokenvalue
                advance() # pass LEFT OPERAND
            elif current_token.tokentype == "variable_identifier":
                if current_token.tokenvalue in variables.keys() and variables[current_token.tokenvalue] is not None:
                    left = variables[current_token.tokenvalue]
                    if left == 0:
                        new_value = "FAIL"
                    elif left == "":
                        new_value = "FAIL"
                    else:
                        new_value = "WIN"
                    left = new_value
                    advance()
                else:
                    error("[Logic Error] Variable not found", current_line)
            else:
                error("[Syntax Error] Invalid operand", current_line)
            
            if current_token.tokentype == "and_keyword":
                advance() # pass AN
                #right operand
                if current_token.tokentype in expression_tokens:
                    right = expression()
                elif current_token.tokentype in ["numbr_literal","numbar_literal"]:
                    right = current_token.tokenvalue
                    if right == 0:
                        new_value = "FAIL"
                    else:
                        new_value = "WIN"
                    right = new_value
                    advance()
                elif current_token.tokentype == "string_delimiter":
                    advance()
                    if current_token.tokentype == "string_literal":
                        right = current_token.tokenvalue
                        if right == "":
                            new_value = "FAIL"
                        else:
                            new_value = "WIN"
                        right = new_value
                        advance() #pass string literal
                        if current_token.tokentype != "string_delimiter":
                            error("[Syntax Error] String delimiter expected", current_line)
                        advance()
                    else:
                        error("[Syntax Error] Invalid string literal", current_line)
                elif current_token.tokentype == "troof_literal":
                    right = current_token.tokenvalue
                    advance() # pass LEFT OPERAND
                elif current_token.tokentype == "variable_identifier":
                    if current_token.tokenvalue in variables.keys() and variables[current_token.tokenvalue] is not None:
                        right = variables[current_token.tokenvalue]
                        if right == 0:
                            new_value = "FAIL"
                        elif right == "":
                            new_value = "FAIL"
                        else:
                            new_value = "WIN"
                        right = new_value
                        advance()
                    else:
                        error("[Logic Error] Variable not found", current_line)
                else:
                    error("[Syntax Error] Invalid operand", current_line)


                if right is None: # OPERAND NOT TYPECAST-ABLE
                    error("[Runtime Error] Cannot perform operation. Invalid operand.", current_line)
                elif operationType == "both_true_check_keyword": #BOTH OF (AND)
                    if left == right == "WIN":
                        result = "WIN"
                    else:
                        result = "FAIL"
                    return result
                elif operationType == "both_false_check_keyword": #EITHER OF (OR)
                    if left == "WIN" or right == "WIN":
                        result = "WIN"
                    else:
                        result = "FAIL"   
                    return result
                elif operationType == "exactly_one_is_true_check_keyword": #WON OF (XOR)
                    if (left == "WIN" and right == "FAIL") or (left == "FAIL" and right == "WIN"):
                        result = "WIN"
                    else:
                        result = "FAIL"
                    return result
                else:
                    error("[Syntax Error] Invalid Boolean operation", current_line)  
            else:
                 error("[Syntax Error] Invalid Boolean operation", current_line) 
        

        elif operationType in ["atleast_one_true_check_keyword", "all_true_check_keyword"]:
            if current_token.tokentype in ["all_true_check_keyword", "atleast_one_true_check_keyword"]: #checks if more than 1 ALL OF OR ANY OF
                has_allOf_anyOf += 1
                if has_allOf_anyOf > 1:
                    error("[Syntax Error] ALL OF or ANY OF cannot be nested into each other and themselves", current_line)

            while current_token.tokentype != "end_of_assignment_keyword":
                if current_token.tokentype in expression_tokens:
                    infinite_arr.append(expression())
                elif current_token.tokentype in ["numbr_literal","numbar_literal"]:
                    if current_token.tokenvalue == 0:
                        new_value = "FAIL"
                    else:
                        new_value = "WIN"
                    infinite_arr.append(new_value)
                    advance() # pass numbr, numbar
                elif current_token.tokentype == "string_delimiter":
                    advance() #pass string delim
                    if current_token.tokentype == "string_literal":
                        if current_token.tokenvalue == "":
                            new_value = "FAIL"
                        else:
                            new_value = "WIN"
                        infinite_arr.append(new_value)
                        advance() #pass string literal
                        if current_token.tokentype != "string_delimiter":
                            error("[Syntax Error] String delimiter expected", current_line)
                        advance() #pass string delim
                    else:
                        error("[Syntax Error] Invalid string literal", current_line)
                elif current_token.tokentype == "troof_literal":
                    infinite_arr.append(current_token.tokenvalue)
                    advance() # pass LEFT OPERAND
                elif current_token.tokentype == "variable_identifier":
                    if current_token.tokenvalue in variables.keys() and variables[current_token.tokenvalue] is not None:
                        output = variables[current_token.tokenvalue]
                        if output == 0:
                            new_value = "FAIL"
                        elif output == "":
                            new_value = "FAIL"
                        else:
                            new_value = "WIN"
                        output = new_value
                        infinite_arr.append(output)
                        print(infinite_arr.append)
                        advance() 
                    else:
                        error("[Logic Error] Variable not found", current_line)
                else:
                    error("[Syntax Error] Invalid operand", current_line)    

                if current_token.tokentype == "and_keyword":
                    advance() # pass AN
                elif current_token.tokentype == "end_of_assignment_keyword":
                    break
                else:
                    error("[Syntax Error] Missing AN or MKAY", current_line)
            advance()
            if operationType == "all_true_check_keyword": #infinite AND (ALL OF)
                if "FAIL" in infinite_arr:
                    result = "FAIL"
                else:
                    result = "WIN"
                return result
            elif operationType == "atleast_one_true_check_keyword": #infinite OR (ANY OF)
                if "WIN" in infinite_arr:
                    result = "WIN"
                else:
                    result = "FAIL"
                return result
            else:
                error("[Syntax Error] Invalid Boolean operation", current_line)  
        else:
            error("[Syntax Error] Invalid Boolean operation", current_line) 
    else: 
        error("[Syntax Error] Invalid Boolean operation", current_line) 

def loop():
    if current_token.tokentype == "explicit_start_loop_keyword":
        advance()
        if current_token.tokentype == "variable_identifier":
            loop_variable = current_token.tokenvalue
            # check if value can be incremented or decremented and if it exists
            if loop_variable in variables.keys():
                if not isinstance(variables[loop_variable],(int, float)): 
                    error("[Logic Error] Variable cannot be incremented or decremented", current_line)
            else:
                error("[Logic Error] Variable does not exist", current_line)
            advance()
            if current_token.tokentype == "increment_keyword": #UPPIN   
                op_type = "increment"
            elif current_token.tokentype == "decrement_keyword": #NERFIN
                op_type = "decrement"
            else:
                error("[Syntax Error] Loop operation not found", current_line)
            advance()
            # optional TIL and WILE
            if current_token.tokentype == "until_indicated_end_of_loop_keyword":
                end_cond_type = "until"
                advance()

            elif current_token.tokentype == "while_indicated_end_of_loop_keyword":
                end_cond_type = "while"
            elif current_token.tokentype == "linebreak": # infinite loop until GTFO
                end_cond_type = None
            else:
                error("[Syntax Error] Unknown loop condition type", current_line)
            # CODE BLOCK FOR LOOP
        else:
            error("[Syntax Error] Label for the loop not found", current_line)
    else:
        error("[Syntax Error] Invalid Loop operation", current_line)


def if_else_statement():
    global current_token
    if current_token.tokens_list == "if_keyword":
        advance()
        if variables["IT"] == "WIN":
            if current_token.tokens_list == "if_true_keyword":
                advance()
                statement()
            else:
                error("[Syntax Error] Missing YA RLY", current_line)  
        elif variables["IT"] == "FAIL":  
            if current_token.tokens_list == "else_keyword":
                advance()
                statement()
            else:
                error("[Syntax Error] Missing NO WAI", current_line) 
        advance()

        if current_token.tokens_list == "end_of_if_block_keyword":
            advance()
        else:
            error("[Syntax Error] Missing OIC", current_line)
    else:
        error("[Syntax Error] Missing O RLY?", current_line)



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

def handle_semi_typecast(var_name, target_type, current_line):
    global current_token
    yarn_pattern = r"^-?(0|[1-9][0-9]*)(\.[0-9]+)?$"
    
    #Get the value associated w/ variable identifier
    var_value = variables.get(var_name, "NOOB")
    
    #perfrom type conversion based on target type
    if target_type == "NUMBR":
        if var_value == "WIN" or (var_value == True and isinstance(var_value, bool)):   #Note: consider string literals WIN and FAIL, not just troof
            new_value = 1
        elif var_value == "FAIL" or (var_value == False and isinstance(var_value, bool)):
            new_value = 0
        elif isinstance(var_value, str):
            # test yarn_pattern
            if re.fullmatch(yarn_pattern, var_value): # check if string is a number
                print("var_value:", var_value)
                var_value = re.sub(r'\.\d+', '', var_value)
                new_value = int(var_value) # change to integer
            else:
                error(f"[RuntimeError] Invalid String. Cannot convert '{var_value}' to NUMBR", current_line)
        elif isinstance(var_value, float):
            new_value = int(var_value) # change float to integer
        elif isinstance(var_value, int):
            new_value = var_value # still same
        else: # for None
            error(f"[RuntimeError] Cannot convert '{var_value}' to NUMBR", current_line)

    elif target_type == "NUMBAR":
        if var_value == True:   #Note: consider string literals WIN and FAIL, not just troof
            new_value = 1.0
        elif var_value == False:
            new_value = 0.0
        elif isinstance(var_value, str):
            if re.fullmatch(yarn_pattern, var_value):
                new_value = int(var_value)
            else:
              error(f"[RuntimeError] Invalid String. Cannot convert '{var_value}' to NUMBAR", current_line)  
        elif isinstance(var_value, float):
            new_value = var_value
        elif isinstance(var_value, int):
            new_value = float(var_value)
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
                        
    elif target_type == "YARN":
        if variables[var_name] == True:
            new_value = "WIN"
        elif variables[var_name] == False:
            new_value = "FAIL"
        elif variables[var_name] == None:
            error(f"[RuntimeError] Cannot convert uninitialized value to YARN", current_line)
        new_value = str(variables[var_name])
    elif target_type == "NOOB": # var IS NOW A NOOB # typecase a variable to NOOB
        new_value = None
    else:
        error(f"[RuntimeError] Failed to convert '{var_value}'", current_line)
    
    return new_value


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

def function_statement_list():
    global current_token, current_line
    nodes = []
    while current_token.tokentype != "end_of_function_keyword":
        node = statement()
        if node is not None:
            nodes.append(node)
        if_linebreak()
    return nodes

def print_expression():
    global current_token, outputText
    if current_token.tokentype in ["numbr_literal", "numbar_literal", "troof_literal"]:
        node = current_token
        advance() # pass literal
        # print the value of the literal
        literal_value = node.tokenvalue
        print(literal_value)
        # show literal_value in outputText tkinter
        insert_output(literal_value)
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
                insert_output(string_value) # show in tkinter console
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
        # change variable value to WIN or FAIL
        variable_value = check_if_bool(variable_value)
        print(variable_value)
        insert_output(variable_value) # show in tkinter console
        advance() # pass varident
        return node
    elif current_token.tokentype in expression_tokens:
        node = expression()
        ans = check_if_bool(node)
        print(ans)
        insert_output(ans) # show in tkinter console
        return node
    else:
        error("[SyntaxError] Invalid print arguments", current_line)

def check_if_bool(ans):
    if isinstance(ans, bool) and ans == True: # because True is similar to 1 
        return "WIN"
    elif isinstance(ans, bool) and ans == False: # False similar to 0
        return "FAIL"
    elif ans == None:
        return "NOOB"
    else:
        return ans

def syntax_analyzer():
    global current_token,token_idx
    print("\nSYNTAX ANALYZER:")
    advance()
    return program()

def do_parse_tree(tokens_list):
    global tokens
    tokens = tokens_list
    parse_tree = syntax_analyzer()
    print(variables)
    print(("PROGRAM",parse_tree))

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

# beige colors
dark00 = "#2c2820"
dark0 = "#3d382d"
dark1 = "#575144"
dark2 = "#9e9a91"
dark3 = "#c6c3bb"
dark4 = "#9e998f"
# dark black colors
# dark00 = "#1f2124"
# dark0 = "#2f3136"
# dark1 = "#292b2f"
# dark2 = "#40444b"
# dark3 = "#565960"
# dark4 = "#c8ccd4"

bluishdark = "#6786b5"

# ============

# Font =======
defaultFont = ("Microsoft YaHei UI", 8, "normal")
labelFont = ("Microsoft YaHei UI", 8, "bold") 
texteditorFont = ("Consolas", 10, "normal") 
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
        # erase previous contents of textEditor
        textEditor.delete("1.0", tk.END) 
        textEditor.insert("1.0",file.read())
        file.close()
        
def execute_lexical():
    global tokens
    # get text from text editor
    text = textEditor.get("1.0", tk.END)
    
    # print("text is:\n", text)
    if text:
        tokens = parse_tkinter(text)
        print(tokens)
        for token in tokens:
            if token.tokentype != "linebreak" and token.tokentype != "empty_line": # won't include linebreak and empty line in lexeme table
                lexemeTable.insert("", "end", values=(token.tokenvalue, token.tokentype))

def execute_parser():
    global tokens
    do_parse_tree(tokens)

# update symbol table when variables dictionary changes
def update_symbol_table():
    global variables, symbolTable
    # empty the table
    for i in symbolTable.get_children():
        symbolTable.delete(i)
    # add variables again to the table
    for key, value in variables.items():
        # if value is True or False, should show WIN or FAIL
        value = check_if_bool(value)
        symbolTable.insert("", "end", values=(key, value))

def reset_symbol_table():
    global variables, symbolTable, tokens, token_idx, current_token, current_line, errorMessage
    # empty the table
    for i in symbolTable.get_children():
        symbolTable.delete(i)
    # reset variables
    variables = {'IT': None}
    # add variables again to the table
    for key, value in variables.items():
        symbolTable.insert("", "end", values=(key, value))

    # reset parser global variables
    tokens = []
    token_idx = -1
    current_token = None
    current_line = 1
    errorMessage = ""
    
def reset_lexeme_table():
    global lexemeTable
    # empty the table
    for i in lexemeTable.get_children():
        lexemeTable.delete(i)

def reset_console():
    # reset console: set outputText to empty
    outputText.configure(state=tk.NORMAL)
    outputText.delete("1.0","end")
    outputText.configure(state=tk.DISABLED)
    
def execute_code():
    # reset lexeme and symbol table
    reset_lexeme_table()
    reset_symbol_table()
    reset_console()
    
    # execute lexical analyzer and parser
    execute_lexical()
    execute_parser()
    pass

def insert_output(output):
    outputText.configure(state=tk.NORMAL) # make outputText editable
    outputText.insert('end', str(output) + "\n") # show new output in tkinter console
    outputText.configure(state=tk.DISABLED) # make outputText uneditable again

root = tk.Tk()
root.title("The Lords of the Strings LOLCODE Interpreter")

# sets the width and height of the window
window_width = 1350
window_height = 700
root.geometry(f"{window_width}x{window_height}")

# centers the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 3 # Add padding on top
root.geometry(f"+{x}+{y}")

# root.minsize(1350,700)

font.nametofont("TkDefaultFont").configure(family=defaultFont[0], size=defaultFont[1])
root.config(bg=dark0)
topFrame = tk.Frame(root, bg=bgcolor1)
bottomFrame = tk.Frame(root, bg=dark0)

# dark mode
style = ttk.Style()
style.theme_use('clam')
style.configure("Custom.Treeview", background=dark4, fieldbackground=dark4)
# Top Frame =====
# Text Editor
textEditorFrame = tk.Frame(topFrame, width=400,bg=dark0)
openfileUI = tk.Frame(textEditorFrame, bg=dark0)
filepathText = tk.Text(openfileUI, height = 1, width=54, bg=dark1, fg="white", selectbackground=dark2, selectforeground="white")
openfileButton = tk.Button(openfileUI, text="Open", command=open_file, bg=dark1, fg="white", font=labelFont, activebackground=dark0, activeforeground="white")
filepathText.configure(state=tk.DISABLED)

textEditFrame = tk.Frame(textEditorFrame, bg=dark0)
textEditor = tk.Text(textEditFrame, padx=20, pady=20, height = 10, width = 60, wrap='none', font=texteditorFont, selectbackground=dark2, selectforeground="white")

# SCROLLBAR
textEditorvsb = ttk.Scrollbar(textEditFrame, orient="vertical", command=textEditor.yview)
textEditor.configure(yscrollcommand=textEditorvsb.set, bg=dark0, fg="white", insertbackground="white") # dark mode
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
lexemeFrame = tk.Frame(topFrame, width=300, bg=dark0)
lexemeTableLabel = tk.Label(lexemeFrame, text="Lexeme Table", font=labelFont, fg="white", bg=dark0)

lexemeTableFrame = tk.Frame(lexemeFrame, width=300, bg=dark0)

lexemeTable = ttk.Treeview(lexemeTableFrame, columns=("lexeme", "classification"), show='headings', style="Custom.Treeview")
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
symbolFrame = tk.Frame(topFrame, width=300, bg=dark1)
symbolTableLabel = tk.Label(symbolFrame, text="Symbol Table", font=labelFont, fg="white", bg=dark1)
symbolTableFrame = tk.Frame(symbolFrame, width=300, bg=dark1)

symbolTable = ttk.Treeview(symbolTableFrame, columns=("identifier", "value"), show='headings', style="Custom.Treeview")
symbolTable.heading("identifier", text="Identifier")
symbolTable.heading("value", text="Value")

symbolvsb = ttk.Scrollbar(symbolTableFrame, orient="vertical", command=symbolTable.yview)
symbolTable.configure(yscrollcommand=symbolvsb.set)
symbolvsb.pack(side=tk.RIGHT, fill=tk.Y)

symbolTableLabel.pack(side=tk.TOP)
symbolTable.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
symbolTableFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

symbolFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# --------------------------------------------------------
# BOTTOM FRAME
# --------------------------------------------------------

# EXECUTE BUTTON 
executeButton = tk.Button(bottomFrame, text="EXECUTE", font=labelFont, command=execute_code, bg=dark1, fg="white", activebackground=dark0, activeforeground="white")
executeButton.pack(side=tk.TOP, fill=tk.X)

# CONSOLE CONFIGURATIONS

# console frame
outputFrame = tk.Frame(bottomFrame)

# console text
outputText = tk.Text(outputFrame, bg=dark00, padx=20, pady=20, fg="white", height = 10, width = 60, wrap='none', font=texteditorFont, selectbackground=dark2, selectforeground="white")

# console scrollbars
outputTextvsb = ttk.Scrollbar(outputFrame, orient="vertical", command=outputText.yview)
outputText.configure(yscrollcommand=outputTextvsb.set)
outputTextvsb.pack(side=tk.RIGHT, fill=tk.Y)
outputTexthsb = ttk.Scrollbar(outputFrame, orient="horizontal", command=outputText.xview)
outputText.configure(xscrollcommand=outputTexthsb.set)

# console pack and disable text editing
outputTexthsb.pack(side=tk.BOTTOM, fill=tk.X)
outputText.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
outputFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
outputText.configure(state=tk.DISABLED)

# ----------------------------------------------------------------

topFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
bottomFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Event Binds
textEditor.bind("<Tab>", insert_spaces)

# root.bind('<Configure>', on_resize) # flickering bug 

root.mainloop()

# if __name__ == '__main__':
#     tokens = parse_terminal(sys.argv[1])
#     print(tokens)
#     parse_tree = syntax_analyzer()
#     print(variables)
#     print(("PROGRAM",parse_tree))