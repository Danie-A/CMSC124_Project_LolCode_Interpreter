# for sounds
import pygame
import random  # for random sounds

import regex as re # for regex in lexemes
import sys  
import math 
import tkinter as tk # for display
from tkinter import font, ttk, filedialog, simpledialog


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
lines = [] # contains strings per line of code

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
    global lines
    lines = contents.split('\n') # split contents (per line through newline) to the 'lines' list
    lexeme = ""
    items = []
    obtwFound = False
    after_line_cont = False # checker for line continuation (line after ...)
    for i, line in enumerate(lines):
        # For Multi-Line Comments
        # Check if OBTW is found
        if obtwFound:
            # Check if TLDR is found
            if find_tldr(i,line):
                obtwFound = False
                # change line to empty string
                lines[i] = ""
                items.append(Token("empty_line", line))
                continue
            else:
                # change line to empty string
                lines[i] = ""
                items.append(Token("empty_line", line))
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
                items.append(Token("empty_line", line))
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
        line_cont = False # checker for line continuation
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
                items.append(Token("parameter_separator_keyword", token))   
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
                if line_cont:
                    line_cont = False
                    after_line_cont = True
                    continue
                else:
                    if after_line_cont:
                        after_line_cont = False
                        items.append(Token("linebreak", "\\n"))
                        # append empty line (for correct line numbering)
                        items.append(Token("empty_line", ""))
                    else: 
                        items.append(Token("linebreak", "\\n"))
            elif re.fullmatch(r"", token):
                items.append(Token("epsilon", token))
            # elif re.fullmatch(r".*", token):
            #     items.append(Token("any", token))
            elif re.fullmatch(r"\+", token):
                items.append(Token("print_concatenation_keyword", token))
            elif re.fullmatch(r"!", token):
                items.append(Token("suppress_newline", token))
            elif re.fullmatch(r"\.\.\.", token):
                # if next token is not linebreak, error, else do not add to items: ... and linebreak
                if tokens[j+1] != "\n":
                    error(f"[SyntaxError] Invalid token ({token}) Token after ... should be linebreak", i+1)
                else:
                    line_cont = True
                    continue
            else:
                error(f"[LexerError] Invalid Token Detected.", i+1)

    # print items separated by newline
    for item in items:
        print(item)        
    return items

# parse function for terminal-based
def parse_terminal(file):
    contents = open(file, 'r').read()
    contents.replace('\t', '    ') # change tabs to 4 spaces
    contents = re.sub(r"(?<!O)BTW.*?(?=\n)", "", contents) # remove comments by deleting BTW and after it before \n
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

active_loops = {}
tokens = []
token_idx = -1
current_token = None
current_line = 1
errorMessage = ""

    
def advance():
    global token_idx, current_token
    if token_idx < len(tokens): # trying to fix index out of range error (added minus 1)
        token_idx += 1
        if token_idx < len(tokens):
            current_token = tokens[token_idx]
        else:
            error("[SyntaxError] End of file reached with incorrect syntax", current_line)

def restore(saved_token_idx, saved_curr_line):
    global token_idx, current_token, current_line
    token_idx = saved_token_idx
    current_token = tokens[token_idx]
    current_line = saved_curr_line

class Error(Exception):
    def __init__(self, message=None):
        self.message = message
        super().__init__(message)
        
def error(msg, line):
    global errorMessage
    # use Error class
    code = get_line(line)
    errorMessage = f"{msg} \n{code}  :  Line {line}"
    insert_output(errorMessage)
    pygame.mixer.music.load("sounds/windows-error.mp3")
    pygame.mixer.music.play(loops=0)
    raise Error(errorMessage)

def skip_empty_lines():
    global current_token, current_line
    while current_token.tokentype == "empty_line":
        advance() # skip empty lines
        current_line += 1


        
def if_linebreak():
    global current_token, current_line
    if current_token.tokentype == "linebreak":
        current_line += 1
        advance()
        skip_empty_lines()
    else:
        error(f"[SyntaxError] Linebreak expected after token: {tokens[token_idx-1].tokenvalue}", current_line)
        
def program():
    global current_token, current_line
    nodes = []
    update_symbol_table()
    skip_empty_lines()
    
    # check for function definitions outside hai
    if current_token.tokentype == "define_function_keyword":
        while current_token.tokentype == "define_function_keyword":
            check_function_def()
            if_linebreak()
    if current_token.tokentype == "start_code_delimiter":
        nodes.append(("START",current_token))
        advance()
        if_linebreak()
        
        if current_token.tokentype =="define_function_keyword":
            while current_token.tokentype == "define_function_keyword":
                check_function_def()
                if_linebreak() # pass linebreak
        
        # VARIABLE DECLARATION
        if current_token.tokentype == "start_var_declaration_delimiter": # WAZZUP
            # can only be at the start of the code
            
            advance() # pass wazzup
            if_linebreak()
            varDeclarationList = var_declaration_list()
            nodes.append(("VAR_DEC_LIST",varDeclarationList))
            if current_token.tokentype == "end_var_declaration_delimiter":
                advance() # pass BUHBYE
                if_linebreak()
            else:
                error("[SyntaxError] End variable declaration delimiter (BUHBYE) not found", current_line)
        # else: # remove so that it is optional only
            #error("[SyntaxError] Start variable declaration delimiter (WAZZUP) not found", current_line)
        
        # STATEMENTS_LIST
        statementList = statement_list()
        nodes.append(("STAT_LIST", statementList))
        if current_token.tokentype == "end_code_delimiter":
            nodes.append(("END",current_token))
            advance() # pass KTHXBYE
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
                        error(f"[SyntaxError] Variable {current_token.tokenvalue} not yet declared", current_line)
                    # else, get the value of the variable and assign it to the new variable
                    variables[varident] = variables[current_token.tokenvalue]
                    node = ("VARIABLE", varident, current_token)
                    advance()
                    var_assign_ongoing = False # set back to false
                    return node
                elif current_token.tokentype in expression_tokens:
                    ans = expression()
                    ans = check_if_bool_var(ans)
                    variables[varident] = ans
                    node = ("VARIABLE", varident, ans)
                    var_assign_ongoing = False # set back to false
                    return node
                else: 
                    lit_value = literal() 
                    variables[varident] = lit_value
                    var_assign_ongoing = False # set back to false
                    return ("VARIABLE", varident, lit_value)      
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
            error(f"[SyntaxError] Variable {current_token.tokenvalue} not yet declared", current_line)
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
        user_input = ""
    else:
        variables[varident_.tokenvalue] = user_input
    insert_output(user_input+"\n")
    update_symbol_table()
    print("User input:", user_input)

class Function: # function class
    def __init__(self, name, body, vars):
        self.name = name # string
        self.body = body # list
        self.vars = vars # dictionary

functions = {} # list of functions

# functions = {"funcname": {funcbody:[], token_start_idx:10, funcvars:{"x": 1, "y": 2, "z": 3}}}
# end marker - if u say so
# saved_main = {tokens: None, token_idx: None, current_line: None}
# save variables: tokens, token_idx, current_token, current_line


# only the syntax --- to edit
def check_function_def():
    global current_token, current_line
    advance() # pass HOW IZ I
    if current_token.tokentype == "variable_identifier":
        funcname = current_token.tokenvalue
        advance() # pass function name
        
        # initialize function variables
        funcvars = {}
        # FUNCTION PARAMETERS
        # funcname var YR x AN YR y AN YR z
        while current_token.tokentype != "linebreak":
            if current_token.tokentype == "parameter_separator_keyword":
                advance() # pass YR (for first parameter)
                if current_token.tokentype != "variable_identifier":
                    error("[SyntaxError] Invalid function parameter (parameter name not found)", current_line)
                else:
                    # place current_token.tokenvalue in funcvars
                    funcvars[current_token.tokenvalue] = None
                    advance() # pass parameter name
            elif current_token.tokentype == "and_keyword":
                advance() # pass AN
                if current_token.tokentype != "parameter_separator_keyword":
                    error("[SyntaxError] Invalid function parameter (YR not found)", current_line)
                else:
                    advance() # pass YR
                    if current_token.tokentype != "variable_identifier":
                        error("[SyntaxError] Invalid function parameter (YR not found)", current_line)
                    else:
                        funcvars[current_token.tokenvalue] = None
                        advance() # pass parameter name
            else:
                error("[SyntaxError] Invalid function parameter (YR / AN YR not found)", current_line)
        
        if_linebreak() # pass linebreak ?
        
        # save starting token idx and current line
        tokenidx = token_idx
        currentline = current_line
        # FUNCTION BODY
        funcbody = []
        while current_token.tokentype != "end_of_function_keyword": # save the succeeding tokens until IF U SAY SO is found
            # get the token idx and current line
            funcbody.append(current_token)
            
            # NOT CHECKING STATEMENT VALIDITY YET
            # run in another process to check if it will result in an error
            if current_token.tokentype == "linebreak":
                current_line += 1
                advance() # go to next token
                skip_empty_lines()
            else:
                advance() # go to next token 

        # functions = {"funcname": {funcbody:[], tokenidx:20, currentline:5, funcvars:{"x": 1, "y": 2, "z": 3}}}
        # put in functions list
        functions[funcname] = {
            "funcbody": funcbody, 
            "tokenidx": tokenidx, 
            "currentline":currentline, 
            "funcvars": funcvars
            }
        advance() # pass IF U SAY SO     
        return ("FUNCTION", functions[funcname])
    else:
        error("[SyntaxError] Invalid function name", current_line)
    
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

# for FUNCTIONS (reusable)
def get_op_value():
    if current_token.tokentype in expression_tokens:
        ans = expression() # pass expression
    elif current_token.tokentype == "variable_identifier":
        var_token = varident() # pass variable
        ans = variables[var_token.tokenvalue]
    elif current_token.tokentype in ["numbr_literal", "numbar_literal", "troof_literal", "string_delimiter"]:
        ans = literal() # pass literal
    else:
        error("[SyntaxError] Invalid expression", current_line)
    return ans

# show the line based on the current_line
def get_line(line):
    global lines
    return lines[line-1]

# 🌍 GLOBAL VARIABLES FOR FUNCTIONS    
saved_main = {"tokens": [], "token_idx": -1, "current_line": 1, "variables": {"IT":None}, "var_assign_ongoing": False}
function_on = 0 # checker if function is running (if function is on, the symbol table should print the saved main NOT the function variables)
loop_on = 0
has_return = 0 # checker for found yr

def statement():
    global function_on, has_return, current_token, var_assign_ongoing, tokens, token_idx, current_line, variables, saved_main
    if current_token.tokentype == "define_function_keyword": # checks for function definitions after var_declaration and before kthxbye
        func_details = check_function_def()
        return ("FUNCTION_DEF", func_details)
    elif current_token.tokentype == "function_call": # [] no function nesting
        advance() # pass I IZ
        if current_token.tokentype != "variable_identifier":
            error("[SyntaxError] Invalid function name", current_line)
        else:
            # FUNCTION PARAMETERS
            # funcname YR SUM OF 1 AN 2 AN YR <expr/lit/var>
            funcname = current_token.tokenvalue

            if funcname not in functions: # check if funcname is in functions
                error("[SyntaxError] Function not yet declared", current_line)
            advance() # pass funcname
            
            args = [] # parameter arguments list
            
            # FUNCTION ARGUMENTS
            while current_token.tokentype != "linebreak":
                if current_token.tokentype == "parameter_separator_keyword":
                    advance() # pass YR (for first parameter)
                    param_val = get_op_value()
                    args.append(param_val)
                elif current_token.tokentype == "and_keyword":
                    advance() # pass AN
                    if current_token.tokentype != "parameter_separator_keyword":
                        error("[SyntaxError] Invalid function parameter (YR not found)", current_line)
                    else:
                        advance() # pass YR
                        param_val = get_op_value()
                        args.append(param_val)
                else:
                    error("[SyntaxError] Invalid function argument", current_line)
            # check total number of parameters if same with number of arguments 
            numParams = len(functions[funcname]["funcvars"])
            if numParams != len(args):
                error(f"[FunctionError] Does not meet required number of arguments ({numParams}) in {funcname} function", current_line)
            
            funcvars = functions[funcname]["funcvars"]
            
            # update function's funcvars with the arguments
            params = list(funcvars.keys())

            for i in range(numParams):
                funcvars[params[i]] = args[i]
            funcvars["IT"] = None # place IT in dictionary
            
            # save main details (PC)
            saved_main = {"token_idx": token_idx, "current_line": current_line, "variables": variables, "var_assign_ongoing": var_assign_ongoing}
        
            # update main details with function details
            # functions = {"funcname": {funcbody:[], token_start_idx:10, funcvars:{"x": 1, "y": 2, "z": 3}}}
            token_idx = functions[funcname]["tokenidx"]
            current_line = functions[funcname]["currentline"]
            variables = functions[funcname]["funcvars"]
            var_assign_ongoing = False # initialize to false first
            current_token = tokens[token_idx]

            if function_on == 1:
                error("[SyntaxError] Function nesting is not allowed or implementable", current_line)
            function_on = 1 # run function
            # RUN FUNCTION BODY
            while current_token.tokentype != "end_of_function_keyword":
                # check if function is off, break
                if function_on == 0:                  
                    break
                statement()
                if_linebreak()
            
            if has_return == 0: # no return value; IT in main is still NOOB
                saved_main["variables"]["IT"] = None

            # restore main details (PC)
            token_idx = saved_main["token_idx"]
            current_token = tokens[token_idx]
            current_line = saved_main["current_line"]
            variables = saved_main["variables"]
            var_assign_ongoing = saved_main["var_assign_ongoing"]
            
            has_return = 0 # set has_return back to 0
            function_on = 0 # set function off (only one function at a time, no nesting)
            return ("FUNCTION_CALL", funcname, args)
    elif current_token.tokentype == "print_keyword": 
        advance() # pass VISIBLE
        ans = "" # initialize empty string
        newline = True # checker for ! (suppress newline)
        while current_token.tokentype != "linebreak":
            operand = print_expression()
            ans = str(ans) + str(operand)
            if current_token.tokentype == "print_concatenation_keyword":
                advance() # advance +
            elif current_token.tokentype == "suppress_newline":
                # if next token is linebreak, do not print newline else error
                if tokens[token_idx+1].tokentype == "linebreak":
                    advance() # pass !
                    newline = False
                else:
                    error("[SyntaxError] Suppress newline (!) must be followed by linebreak", current_line) 
            elif current_token.tokentype == "linebreak":
                break
            else:
                error("[SyntaxError] : no + keyword detected", current_line)
        
        # ans = print_expression()
        print(ans)
        place_in_IT(ans) # place in IT variable
        if newline == True:
            insert_output(ans + "\n")
        else:
            insert_output(ans)
        return ("PRINT", ans)  
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
                lit_value = literal()
                variables[var_dest_token.tokenvalue] = lit_value
                update_symbol_table()
                var_assign_ongoing = False # set back to false, variable reassignment done
                return ("ASSIGN", var_dest_token, lit_value)
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
                handle_full_typecast(var_dest_token.tokenvalue, type_literal_.tokenvalue, current_line)
                advance() # pass NUMBAR/NUMBR/TROOF/YARN
                update_symbol_table()
                var_assign_ongoing = False # set back to false, variable reassignment done
                return("FULL_TYPECAST", var_dest_token, type_literal_)
            else:
                error("[SyntaxError] Invalid typecast literal", current_line)
        
        elif current_token.tokentype == "linebreak": # var only as statement
            # get the value of variable and place in IT
            value = variables[var_dest_token.tokenvalue]
            place_in_IT(value) # place in IT variable
            return ("VARIABLE", var_dest_token, value)
        else:
            error("[SyntaxError] Invalid variable value reassignment. R not found. ", current_line)
    
    elif current_token.tokentype in flow_control_tokens:  #FLOW CONTROL
        if current_token.tokentype == "explicit_start_loop_keyword": #IM IN YR
            node = loop()
            loop_on = 0
        elif current_token.tokentype == "if_keyword":
            if_else_statement()
        elif current_token.tokentype == "switch_keyword":
            switch_statement()
    
    elif current_token.tokentype in ["numbr_literal", "numbar_literal", "troof_literal", "string_delimiter"]:
        ans = literal() # returns literal value
        place_in_IT(ans) # place in IT variable
        return ("LITERAL", ans)
    # to check if conflicting with switch-case
    elif current_token.tokentype == "general_purpose_break_keyword": # GTFO
        if function_on == 0:
            if loop_on == 0:
                error("[SyntaxError] GTFO found outside function and loop", current_line)
            else:
                advance()
                return "break"
        else:
            advance() # pass GTFO
            # make NOOB in IT main
            saved_main["variables"]["IT"] = None
            function_on = 0 # set function off
            return ("BREAK", None)
    elif current_token.tokentype == "return_keyword": #FOUND YR    
        if function_on == 0:
            error("[SyntaxError] Return keyword not allowed outside function", current_line)
        else:
            advance() # pass FOUND YR
            ans = get_op_value() # pass var, literal, or expression
            # place in IT variable in saved_main
            saved_main["variables"]["IT"] = ans
            has_return = 1 # set has_return to 1 so IT would not be NOOB when it goes back to the function call running
            print("placed answer in IT: ", ans)
            function_on = 0 # set function off
            return ("RETURN", ans)
    # else check if expression (can also be a statement)
    else:
        if current_token.tokentype in expression_tokens:
            expression_ = expression()
            return expression_
        else:
            error("[SyntaxError] Invalid statement", current_line)

# FOR SMOOSH TYPECASTING
def subconvert_to_string(value):
    if isinstance(value, bool):
        if value == True:
            return "WIN"
        else:
            return "FAIL"
    elif value == None:
        error("[ConcatenationError] Cannot implicitly typecast null value to string", current_line)
    else:
        return str(value)

def convert_to_string():
    # if variable, get value then typecast
    if current_token.tokentype == "variable_identifier":
        var_token = varident() # goes to next token after var, get variable token
        value = variables[var_token.tokenvalue]
        value = subconvert_to_string(value)        
    elif current_token.tokentype in ["numbr_literal", "numbar_literal", "troof_literal", "string_delimiter"]:
        lit_value = literal()
        value = subconvert_to_string(lit_value)
    elif current_token.tokentype in expression_tokens:
        ans = expression()
        ans = check_if_bool(ans)
        value = subconvert_to_string(ans)
    else:
        error("[SyntaxError] Invalid operand", current_line)
    return value
        
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
    elif current_token.tokentype == "concatenation_keyword": # SMOOSH
        advance() # pass SMOOSH
        ans = "" # initialize empty string
        while current_token.tokentype != "linebreak":
            operand = convert_to_string() # convert to string
            ans = ans + operand
            if current_token.tokentype == "and_keyword":
                advance() # pass AN
            elif current_token.tokentype == "linebreak":
                break
            else:
                error("[SyntaxError] : no AN keyword detected", current_line)
        print(ans)
    if var_assign_ongoing == False: # place in IT variable if not a variable assignment statement
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
        error(f"[ArithmeticError] Invalid String. Cannot convert '{string}' to NUMBR/NUMBAR", current_line)
        # return None # prev

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
        advance() # pass keyword
        
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
                else: 
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
                advance() # pass numbr/numbar literal
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
                    else: right = variables[current_token.tokenvalue]
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
                if isinstance(variables[current_token.tokenvalue], str): # check if string
                    left = typecast_string(variables[current_token.tokenvalue])
                else: 
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
                    if isinstance(variables[current_token.tokenvalue], str): # check if string
                        right = typecast_string(variables[current_token.tokenvalue])
                    else: 
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
                return result
            elif comparisonType == "both_argument_not_equal_check_keyword": # Equal to !=
                result = "WIN" if left != right else "FAIL"
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
    global loop_on, current_token, current_line
    loop_on = 1
    if current_token.tokentype == "explicit_start_loop_keyword":
        advance()
        if current_token.tokentype == "variable_identifier":
            loop_name = current_token.tokenvalue
            advance()
            if current_token.tokentype == "increment_keyword": #UPPIN   
                op_type = "increment"
            elif current_token.tokentype == "decrement_keyword": #NERFIN
                op_type = "decrement"
            else:
                error("[Syntax Error] Loop operation not found", current_line)
            advance()
            if current_token.tokentype == "parameter_separator_keyword":
                advance() # pass YR
                if current_token.tokentype == "variable_identifier":
                    loop_variable = current_token.tokenvalue
                    # check if value can be incremented or decremented and if it exists
                    numbr_pattern = r"-?([1-9][0-9]*|0)"
                    numbar_pattern = r"-?(0|[1-9][0-9]*)(\.[0-9]+)?"
                    if loop_variable in variables.keys():
                        if re.fullmatch(numbr_pattern, str(variables[loop_variable])):
                            variables[loop_variable] = handle_semi_typecast(loop_variable, "NUMBR", current_line)
                        elif re.fullmatch(numbar_pattern, str(variables[loop_variable])):
                            variables[loop_variable] = handle_semi_typecast(loop_variable, "NUMBAR", current_line)
                        elif str(variables[loop_variable]) == "WIN" or variables[loop_variable] == True: 
                            variables[loop_variable] = 1
                        elif str(variables[loop_variable]) == "FAIL" or variables[loop_variable] == False or variables[loop_variable] == None: 
                            variables[loop_variable] = 0
                        else:
                            error(f"[Logic Error] Variable {loop_variable} cannot be incremented or decremented", current_line)
                    else:
                        error("[Logic Error] Variable does not exist", current_line)
                    active_loops[loop_name] = loop_variable #save the loop name and associated variable to active loops
                    advance()
                    # optional TIL and WILE
                    savedpc_expression = 0
                    saved_currline_expr = 0
                    if current_token.tokentype == "until_indicated_end_of_loop_keyword":
                        # end_cond_type = "until"
                        advance()
                        savedpc_expression = token_idx
                        saved_currline_expr = current_line
                        expr = expression()
                        #check if result is troof
                        print(expr)
                        if expr not in ["FAIL","WIN"]:
                            error("[RuntimeError] Expression in loop operation did not convert to troof", current_line)
                        # CODE BLOCK FOR LOOP
                        if_linebreak()
                        savedpc_codeblock = token_idx
                        saved_currline_codeblock = current_line
                        code_block = loop_statement_list()
                        #GTFO
                        if code_block == "break":
                            print("break runs")
                            #skip lines
                            while current_token.tokentype != "break_loop_keyword":
                                    if current_token.tokentype == "linebreak":
                                        current_line += 1
                                    if current_token.tokentype == "end_code_delimiter":
                                        error("[Syntax Error] IM OUTTA YR not found", current_line)
                                    advance()
                            if current_token.tokentype == "break_loop_keyword": #OUTTA YR
                                advance()
                                if current_token.tokentype == "variable_identifier":
                                    if current_token.tokenvalue == loop_name:
                                        advance()
                                        return "break"
                                else:
                                    error("[Syntax Error] Loop variable identifier not found", current_line)
                            else:
                                error("[Syntax Error] IM OUTTA YR not found", current_line)
                        print("Nodes after loop statement list",code_block)
                        if current_token.tokentype == "break_loop_keyword": #OUTTA YR
                            advance()
                            if current_token.tokentype == "variable_identifier":
                                if current_token.tokenvalue == loop_name:
                                    advance()
                                    savedpc_end = token_idx
                                    saved_currline_end = current_line
                                    if_linebreak()
                                    loop_complete = False
                                    while loop_complete == False:
                                        #increment or decrement
                                        if op_type == "increment":
                                            variables[loop_variable] = variables[loop_variable] + 1
                                            update_symbol_table()
                                        elif op_type == "decrement":
                                            variables[loop_variable] = variables[loop_variable] - 1
                                            update_symbol_table()
                                        else: 
                                            error("[RuntimeError] No operation type given", current_line)
                                        #revaluate expression
                                        restore(savedpc_expression, saved_currline_expr)
                                        expr = expression()
                                        print(expr)
                                        if expr not in ["FAIL","WIN"]:
                                            error("[RuntimeError] Expression in loop operation did not convert to troof", current_line)
                                        if expr == "FAIL":
                                            #loop again
                                            restore(savedpc_codeblock, saved_currline_codeblock)
                                            code_block = loop_statement_list()
                                            #GTFO
                                            if code_block == "break":
                                                restore(savedpc_end, saved_currline_end)
                                                active_loops.pop(loop_name)
                                                loop_complete = True
                                                # return "break"
                                        else:
                                            restore(savedpc_end, saved_currline_end)
                                            active_loops.pop(loop_name)
                                            loop_complete = True

                    elif current_token.tokentype == "while_indicated_end_of_loop_keyword":
                        advance()
                        savedpc_expression = token_idx
                        saved_currline_expr = current_line
                        expr = expression()
                        #check if result is troof
                        print(expr)
                        if expr not in ["FAIL","WIN"]:
                            error("[RuntimeError] Expression in loop operation did not convert to troof", current_line)
                        # CODE BLOCK FOR LOOP
                        if_linebreak()
                        savedpc_codeblock = token_idx
                        saved_currline_codeblock = current_line
                        code_block = loop_statement_list()
                        if code_block == "break":
                            #skip lines
                            while current_token.tokentype != "break_loop_keyword":
                                    if current_token.tokentype == "linebreak":
                                        current_line += 1
                                    if current_token.tokentype == "end_code_delimiter":
                                        error("[Syntax Error] IM OUTTA YR not found", current_line)
                                    advance()
                            if current_token.tokentype == "break_loop_keyword": #OUTTA YR
                                advance()
                                if current_token.tokentype == "variable_identifier":
                                    if current_token.tokenvalue == loop_name:
                                        advance()
                                        return "break"
                                else:
                                    error("[Syntax Error] Loop variable identifier not found", current_line)
                            else:
                                error("[Syntax Error] IM OUTTA YR not found", current_line)
                        print("Nodes after loop statement list",code_block)
                        if current_token.tokentype == "break_loop_keyword": #OUTTA YR
                            advance()
                            if current_token.tokentype == "variable_identifier":
                                if current_token.tokenvalue == loop_name:
                                    advance()
                                    savedpc_end = token_idx
                                    saved_currline_end = current_line
                                    if_linebreak()
                                    loop_complete = False
                                    while loop_complete == False:
                                        #increment or decrement
                                        if op_type == "increment":
                                            variables[loop_variable] = variables[loop_variable] + 1
                                            update_symbol_table()
                                        elif op_type == "decrement":
                                            variables[loop_variable] = variables[loop_variable] - 1
                                            update_symbol_table()
                                        else: 
                                            error("[RuntimeError] No operation type given", current_line)
                                        #revaluate expression
                                        restore(savedpc_expression, saved_currline_expr)
                                        expr = expression()
                                        print(expr)
                                        if expr not in ["FAIL","WIN"]:
                                            error("[RuntimeError] Expression in loop operation did not convert to troof", current_line)
                                        if expr == "WIN":
                                            #loop again
                                            restore(savedpc_codeblock, saved_currline_codeblock)
                                            code_block = loop_statement_list()
                                            #GTFO
                                            if code_block == "break":
                                                restore(savedpc_end, saved_currline_end)
                                                active_loops.pop(loop_name)
                                                loop_complete = True
                                                # return "break"                        
                                        else:
                                            restore(savedpc_end, saved_currline_end)
                                            active_loops.pop(loop_name)
                                            loop_complete = True

                    # elif current_token.tokentype == "linebreak": # infinite loop until GTFO
                    #     end_cond_type = None
                    else:
                        error("[Syntax Error] Unknown loop condition type", current_line)
                    
                else:
                    error("[Syntax Error] Variable identifier not found", current_line)
            else:
                error("[Syntax Error] YR not found", current_line)
        else:
            error("[Syntax Error] Label for the loop not found", current_line)
    else:
        error("[Syntax Error] Invalid Loop operation", current_line)


def if_else_statement():
    global current_token
    has_YA_RLY = False
    has_match = False

    value_tocheck = variables["IT"] #stores result of initial statement for basis of value

    if current_token.tokentype == "if_keyword": #O RLY
        advance() #pass O RLY?
        if current_token.tokentype == "linebreak":
            if_linebreak() #pass linebreak
            if current_token.tokentype == "if_true_keyword":
                has_YA_RLY = True
                advance() #pass YA RLY
                if value_tocheck == "WIN":
                    if current_token.tokentype == "linebreak":
                        if_linebreak() #pass linebreak
                        while current_token.tokentype != "else_keyword": #multiple statements in code block
                            if current_token.tokentype != "end_of_if_block_keyword":
                                statement()
                                if current_token.tokentype == "linebreak":
                                    if_linebreak() #pass linebreak
                            if current_token.tokentype in ["else_if_keyword", "else_keyword", "end_of_if_block_keyword"]:
                                break

                        while current_token.tokentype != "end_of_if_block_keyword": #pass entire NO WAI and MEBBE block
                            advance()
                            if current_token.tokentype == "linebreak":
                                if_linebreak()

                        if current_token.tokentype == "end_of_if_block_keyword":
                            advance() #pass OIC 
                        else:
                            error("[Syntax Error] Expected OIC", current_line) 

                            
                    else: 
                        error("[Syntax Error] Expected linebreak after YA RLY", current_line)

                else:
                    
                    while current_token.tokentype != "else_if_keyword":
                        if current_token.tokentype != "linebreak":
                            advance() #pass entire YA RLY block
                        if current_token.tokentype == "linebreak":
                            if_linebreak() #pass linebreak
                        if current_token.tokentype == "else_keyword":
                            break
                        if current_token.tokentype == "end_of_if_block_keyword":
                            break
                    
                    while current_token.tokentype != "else_keyword":
                        if current_token.tokenvalue == "else_keyword":
                            break
                        if current_token.tokentype == "end_of_if_block_keyword":
                            break
                        advance() #pass MEBBE
                        
                        statement()
                        if current_token.tokentype == "linebreak":
                            if_linebreak() #pass linebreak
                        else:
                            error("[Syntax Error] Expected linebreak statement in MEBBE", current_line)
                        
                        if variables["IT"] == "WIN" and not has_match:
                            has_match = True
                            while current_token.tokentype != "else_if_keyword":
                                statement()
                                if current_token.tokentype == "linebreak":
                                    if_linebreak() #pass linebreak
                                if current_token.tokentype ==  "else_keyword":
                                    break
                        
                        elif variables["IT"] == "FAIL" or has_match:
                            while current_token.tokentype != "else_if_keyword":
                                advance() #pass entire MEBBE block
                                if current_token.tokentype == "linebreak":
                                    if_linebreak() #pass linebreak
                                if current_token.tokentype ==  "else_keyword":
                                    break

                        elif variables["IT"] == "WIN" and has_match:
                            error("[Syntax Error] MEBBE conditions must be unique", current_line)

                    if current_token.tokentype == "else_keyword" and value_tocheck == "FAIL":
                        advance() #pass NO WAI
                        if current_token.tokentype == "linebreak":
                            if_linebreak() #pass linebreak
                        else: 
                            error("[Syntax Error] Expected linebreak after NO WAI", current_line)

                        if not has_match:
                            while current_token.tokentype != "end_of_if_block_keyword":
                                statement()
                                if current_token.tokentype == "linebreak":
                                    if_linebreak() #pass linebreak
                                else:
                                    error("[Syntax Error] Expected linebreak after statement", current_line)                              
                        elif has_match:
                            while current_token.tokentype != "end_of_if_block_keyword":
                                advance() # pass statement
                                if current_token.tokentype == "linebreak":
                                    if_linebreak() #pass linebreak
    

                    if current_token.tokentype == "end_of_if_block_keyword":
                        advance() #pass OIC 
                    else:
                        error("[Syntax Error] Expected OIC", current_line)   
            else:
                error("[Syntax Error] Expected YA RLY", current_line) 
        else:
            error("[Syntax Error] Expected linebreak after O RLY?", current_line) 
    else:
        error("[Syntax Error] Expected O RLY?", current_line) 


###### DO NOT UNCOMMENT (W/O MEBBE) ###################################

# def if_else_statement():
#     global current_token
#     has_YA_RLY = False

#     if current_token.tokentype == "if_keyword": #O RLY
#         advance() #pass O RLY?
#         if current_token.tokentype == "linebreak":
#             # advance() #pass linebreak
#             if_linebreak()
#             if current_token.tokentype == "if_true_keyword":
#                 advance() #pass YA RLY
#                 if variables["IT"] == "WIN":
#                     has_YA_RLY = True           
#                     if current_token.tokentype == "linebreak":
#                         if_linebreak() #pass linebreak
#                         while current_token.tokentype != "else_keyword": #multiple statements in code block
#                             if current_token.tokentype != "end_of_if_block_keyword":
#                                 statement()
#                                 if_linebreak() #pass linebreak
#                             else:
#                                 break
#                         while current_token.tokentype != "end_of_if_block_keyword": #pass entire NO WAI block
#                             advance()
#                             if current_token.tokentype == "linebreak":
#                                 if_linebreak()
#                     else: 
#                         error("[Syntax Error] Expected linebreak after YA RLY", current_line)

#                 elif variables["IT"] == "FAIL":
#                     if not has_YA_RLY:
#                         while current_token.tokentype != "else_keyword": #to pass entire YA RLY block
#                             if current_token.tokentype != "end_of_if_block_keyword":
#                                 advance()
#                                 if current_token.tokentype == "linebreak":
#                                     if_linebreak()
#                             else:
#                                 break
                    
#                     if current_token.tokentype == "else_keyword":
#                         advance() #pass NO WAI
#                         if current_token.tokentype == "linebreak":
#                             if_linebreak() #pass linebreak
#                             while current_token.tokentype != "end_of_if_block_keyword": #multiple statements in code block
#                                 statement()
#                                 if current_token.tokentype == "linebreak":
#                                     if_linebreak()                   
#                         else:
#                             error("[Syntax Error] Expected linebreak after NO WAI", current_line) 

#                 if current_token.tokentype == "end_of_if_block_keyword":
#                     advance() #pass OIC 
#                 else:
#                     error("[Syntax Error] Expected OIC", current_line)  
#             else:
#                 error("[Syntax Error] Expected YA RLY", current_line) 
#         else:
#             error("[Syntax Error] Expected linebreak after O RLY?", current_line) 
#     else:
#         error("[Syntax Error] Expected O RLY?", current_line) 


def switch_statement():
    global current_token
    has_gtfo = False
    statement_value = variables["IT"]
    has_omg_match = False

    if current_token.tokentype == "switch_keyword":
        advance() #pass WTF?
        if current_token.tokentype == "linebreak":
            if_linebreak() #pass linebreak
            while current_token.tokentype != "end_of_if_block_keyword":
                if current_token.tokentype == "switch_case_keyword":
                    advance() #pass OMG
                    if current_token.tokentype in ["numbr_literal", "numbar_literal", "troof_literal", "string_literal"]:
                        if isinstance(statement_value, str):
                            statement_value = typecast_string(statement_value)
                        if statement_value == current_token.tokenvalue and not has_omg_match: #when a case is satisfied
            
                            has_omg_match = True
                            advance() #pass value literal
                            if_linebreak() #pass line break
                            if current_token.tokentype == "general_purpose_break_keyword":
                                has_gtfo = True
                                advance() #pass GTFO
                                if_linebreak() #pass linebreak
                            else:
                                if current_token.tokentype != "switch_case_keyword":
                                    while current_token.tokentype != "general_purpose_break_keyword":
                                        statement()
                                        if current_token.tokentype == "linebreak":
                                            if_linebreak()
                                        if current_token.tokentype == "general_purpose_break_keyword":
                                            has_gtfo = True
                                            advance() #pass GTFO
                                            if current_token.tokentype == "linebreak":
                                                if_linebreak()
                                            break
                                        elif current_token.tokentype == "switch_default_keyword":
                                            break
                                        elif current_token.tokentype == "switch_case_keyword":
                                            advance() #pass omg
                                            advance() #pass value literal
                                            if_linebreak() #pass linebreak
                                            
                                        elif current_token.tokentype == "end_of_if_block_keyword":
                                            break
                                else:
                                    error("[Logic Error] Missing code block for this case", current_line)
                        elif statement_value == current_token.tokenvalue and has_omg_match:
                            error("[Syntax Error] OMG literal must be unique at", current_line)
                        else: 
                            while current_token.tokentype != "switch_case_keyword":
                                advance() #pass entire OMG block
                                if current_token.tokentype == "linebreak":
                                    if_linebreak()
                                if current_token.tokentype == "switch_default_keyword":
                                    break

                    else:
                        error("[Logic Error] Invalid value literal", current_line) 
                elif current_token.tokentype == "switch_default_keyword":
                    advance() #pass OMGWTF
                    if_linebreak() # pass linebreak
                    if has_gtfo or has_omg_match:
                        while current_token.tokentype != "end_of_if_block_keyword":
                            advance()
                            if current_token.tokentype == "linebreak":
                                if_linebreak() #pass linebreak
                            if current_token.tokentype == "general_purpose_break_keyword":
                                error("[Syntax Error] OMGWTF does not need GTFO", current_line)  
                    else:
                        while current_token.tokentype != "end_of_if_block_keyword":
                            statement()
                            if current_token.tokentype == "linebreak":
                                if_linebreak() #pass linebreak
                            if current_token.tokentype == "general_purpose_break_keyword":
                                error("[Syntax Error] OMGWTF does not need GTFO", current_line)  
                    
                else:
                    error("[Syntax Error] Expected OMG", current_line)

        else:
            error("[Syntax Error] Expected linebreak", current_line) 
    else:
        error("[Syntax Error] Expected WTF?", current_line)

    if current_token.tokentype == "end_of_if_block_keyword":
        advance() #pass OIC
    else:
        error("[Syntax Error] Expected OIC?", current_line) 
        

def handle_full_typecast(var_name, target_type, current_line):
    global current_token
    yarn_pattern = r"^-?(0|[1-9][0-9]*)(\.[0-9]+)?$"
    
    #Get the value associated w/ variable identifier
    var_value = variables.get(var_name, "NOOB")

    #perfrom type conversion based on target type
    if target_type == "NUMBR":
        if var_value == "WIN" or (var_value == True and isinstance(var_value, bool)):   #Note: consider string literals WIN and FAIL, not just troof
            new_value = 1
            variables[var_name] = new_value
        elif var_value == "FAIL" or (var_value == False and isinstance(var_value, bool)):
            new_value = 0
            variables[var_name] = new_value
        elif isinstance(var_value, str):
            # test yarn_pattern
            if re.fullmatch(yarn_pattern, var_value):
                var_value = re.sub(r'\.\d+', '', var_value)
                variables[var_name] = int(var_value)
            else:
                error(f"[RuntimeError] Invalid String. Cannot convert '{var_value}' to NUMBR", current_line)
        elif isinstance(var_value, float):
            variables[var_name] = int(var_value)
        elif isinstance(var_value, int):
            variables[var_name] = var_value
        elif var_value == None: # explicit typecasting of noob to numbr
            variables[var_name] = 0
        else:
            error(f"[RuntimeError] Cannot convert '{var_value}' to NUMBR", current_line)
            
    elif target_type == "NUMBAR":
        if var_value == True or var_value=="WIN":   #Note: consider string literals WIN and FAIL, not just troof
            new_value = 1.0
            variables[var_name] = new_value
        elif var_value == False or var_value=="FAIL":
            new_value = 0.0
            variables[var_name] = new_value
        elif isinstance(var_value, str):
            if re.fullmatch(yarn_pattern, var_value):
                variables[var_name] = float(var_value)
            else:
              error(f"[RuntimeError] Invalid String. Cannot convert '{var_value}' to NUMBAR", current_line)  
        elif isinstance(var_value, float):
            variables[var_name] = var_value
        elif isinstance(var_value, int):
            variables[var_name] = float(var_value)
        elif var_value == None:
            variables[var_name] = 0.0 # explicit typecasting of noob to numbar
        else:
            error(f"[RuntimeError] Cannot convert '{var_value}' to NUMBAR", current_line)
    elif target_type == "TROOF":
            if var_value == "" or var_value == None or var_value==0: # None to False allowed
                new_value = False # will print FAIL in Symbol Table
            elif var_value == "WIN":
                new_value = True # equivalent to WIN troof_literal
            elif var_value == "FAIL":
                new_value = False # equivalent to FAIL troof_literal
            else:
                new_value = True # equivalent to WIN
        
            variables[var_name] = new_value
            
    elif target_type == "YARN":
        if variables[var_name] == True and isinstance(variables[var_name], bool):
            variables[var_name] = "WIN"
        elif variables[var_name] == False and isinstance(variables[var_name], bool):
            variables[var_name] = "FAIL"
        elif variables[var_name] == None:
            variables[var_name] = "" # explicit typecasting of noob to yarn (empty string)
        else:
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
                var_value = re.sub(r'\.\d+', '', var_value)
                new_value = int(var_value) # change to integer
            else:
                error(f"[RuntimeError] Invalid String. Cannot convert '{var_value}' to NUMBR", current_line)
        elif isinstance(var_value, float):
            new_value = int(var_value) # change float to integer
        elif isinstance(var_value, int):
            new_value = var_value # integer still same
        else: # for None
            error(f"[RuntimeError] Cannot convert '{var_value}' to NUMBR", current_line)

    elif target_type == "NUMBAR":
        if var_value == True or var_value=="WIN":   #Note: consider string literals WIN and FAIL, not just troof
            new_value = 1.0
        elif var_value == False or var_value=="FAIL":
            new_value = 0.0
        elif isinstance(var_value, str):
            if re.fullmatch(yarn_pattern, var_value):
                new_value = int(var_value)
            else:
              error(f"[RuntimeError] Invalid String. Cannot convert '{var_value}' to NUMBAR", current_line)  
        elif isinstance(var_value, float): # float still the same
            new_value = var_value
        elif isinstance(var_value, int):
            new_value = float(var_value)
        else: # for None
            error(f"[RuntimeError] Cannot convert '{var_value}' to NUMBAR", current_line)
    elif target_type == "TROOF":
        if var_value == "" or var_value == 0 or var_value == None: # implicit typecasting of None to False
            new_value = False # will print FAIL in Symbol Table
        elif var_value == "WIN":
            new_value = True # equivalent to WIN troof_literal
        elif var_value == "FAIL":
            new_value = False # equivalent to FAIL troof_literal
        elif var_value == None:
            error("[RuntimeError] Cannot convert uninitialized value to TROOF", current_line)            
        elif var_value == False:
            new_value = False # still False
        else:
            new_value = True # equivalent to WIN
                        
    elif target_type == "YARN":
        if isinstance(var_value, bool) and var_value == True:
            new_value = "WIN"
        elif isinstance(var_value, bool) and var_value == False:
            new_value = "FAIL"
        elif var_value == None: # none to string only in explicit typecasting
            error(f"[RuntimeError] Cannot convert uninitialized value to YARN", current_line)
        else:
            new_value = str(var_value)
    elif target_type == "NOOB": # var IS NOW A NOOB # typecase a variable to NOOB
        new_value = None
    else:
        error(f"[RuntimeError] Failed to convert '{var_value}'", current_line)
    
    return new_value



                            
def literal():
    if current_token.tokentype in ["numbr_literal", "numbar_literal", "troof_literal"]:
        type = current_token.tokentype
        value = current_token.tokenvalue
        if type == "numbr_literal":
            final_value = int(value)
        elif type == "numbar_literal":
            final_value = float(value)
        elif type == "troof_literal":
            if value == "WIN":
                final_value = True
            else:
                final_value = False
        advance() # pass literal value
        return final_value
    elif current_token.tokentype == "string_delimiter": # string literal
        advance() # pass "
        if current_token.tokentype == "string_literal":
            final_value = current_token.tokenvalue
            advance() # pass string value
            if current_token.tokentype == "string_delimiter":
                advance() # pass "
                return final_value
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

def loop_statement_list():
    global current_token, current_line
    nodes = []
    while current_token.tokentype != "break_loop_keyword":
        if current_token.tokentype == "end_code_delimiter":
            error("[Syntax Error] OUTTA YR not found",current_line)
        if current_token.tokentype == "general_purpose_break_keyword":
            advance()
            return "break"
        node = statement()
        if node is not None:
            nodes.append(node)
        if_linebreak()
    return nodes

def print_expression():
    global current_token
    if current_token.tokentype in ["numbr_literal", "numbar_literal", "troof_literal"]:
        literal_value = current_token.tokenvalue
        advance() # pass literal
        # print the value of the literal
        return literal_value
    elif current_token.tokentype == "type_literal":
        if current_token.tokenvalue == "NOOB":
            advance() # pass NOOB
            return "NOOB"
        else:
            error("[PrintError] Cannot print a type literal", current_line)
    elif current_token.tokentype == "string_delimiter": # string literal
        advance() # pass opening "
        if current_token.tokentype == "string_literal":
            string_value = current_token.tokenvalue
            advance() #string delimiter
            if current_token.tokentype == "string_delimiter":
                advance()  # pass closing "
                #extract/print value of string literal 
                return string_value
            else:
                error("[SyntaxError] String delimiter expected", current_line)
        else:
            error("[SyntaxError] Invalid string literal", current_line)
    elif current_token.tokentype == "variable_identifier": # check if variable identifier
        node = ("VARIDENT", current_token.tokentype, current_token.tokenvalue)
        if current_token.tokenvalue not in variables:
            error(f"[SyntaxError] Variable {current_token.tokenvalue} not yet declared", current_line)
        #extract/print value of var identifier
        variable_value = variables[current_token.tokenvalue]
        # change variable value to WIN or FAIL
        variable_value = check_if_bool(variable_value)
        advance() # pass varident
        # next should be linebreak or AN, else error
        if current_token.tokentype == "linebreak" or current_token.tokentype == "print_concatenation_keyword" or current_token.tokentype == "suppress_newline":
            return variable_value
        else:
            error("[SyntaxError] Invalid print arguments", current_line)
    elif current_token.tokentype in expression_tokens:
        node = expression()
        ans = check_if_bool(node)
        return ans
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

def check_if_bool_var(ans):
    if isinstance(ans, bool) and ans == True: # because True is similar to 1 
        return "WIN"
    elif isinstance(ans, bool) and ans == False: # False similar to 0
        return "FAIL"
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

# Global Variables ===
fileLoaded = False
file_path = ""
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

def insert_spaces(event):
    textEditor.insert(tk.INSERT, " " * 4)
    return 'break'

# SOUNDS
sounds = ["anitamaxwynn","fbi-open-up", "windows-error", "ws-in-the-sshat", "oof", "omg", "shout", "wow", "bro", "wait", "whoareyou", "shish", "anitamaxwynn2", "hbd", "hbd2", "walangpasok", "fewmoments", "brb", "justdoit", "hellothere", "alert", "lol"] 

# Program Functions
def open_file():
    global fileLoaded, file_path
    filename = "sounds/"+random.choice(sounds)+".mp3"
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(loops=0)
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
    text = text.replace('\t', '    ') # change tabs to 4 spaces
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

def reset_global_variables(): 
    global tokens, token_idx, current_token, current_line, errorMessage, variables, saved_main, function_on, loop_on, has_return
    tokens = []
    token_idx = -1
    current_token = None
    current_line = 1
    errorMessage = ""
    variables = {'IT': None}         
    saved_main = {"tokens": [], "token_idx": -1, "current_line": 1, "variables": {"IT":None}, "var_assign_ongoing": False}
    function_on = 0 # checker if function is running (if function is on, the symbol table should print the saved main NOT the function variables)
    loop_on = 0
    has_return = 0 # checker for found yr

def execute_code():
    # play meme sound
    filename = "sounds/"+random.choice(sounds)+".mp3"
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(loops=0)
    # reset global vars
    reset_global_variables()
    # reset lexeme and symbol table
    reset_lexeme_table()
    reset_symbol_table()
    reset_console()
    # execute lexical analyzer and parser
    execute_lexical()
    execute_parser()
    pass

def insert_output(output):
    color = "white"
    if errorMessage != "":
        color = "#f59393"
    if output == None:
        output = "NOOB"
    outputText.configure(state=tk.NORMAL) # make outputText editable
    start_index = outputText.index('end') # get the index before inserting the text
    outputText.insert('end', str(output)) # show new output in tkinter console
    end_index = outputText.index('end') # get the index after inserting the text
    outputText.tag_configure(color, foreground=color) # configure a tag for red text
    outputText.tag_add(color, start_index, end_index) # apply the tag to the inserted text
    outputText.configure(state=tk.DISABLED) # make outputText uneditable again
    
root = tk.Tk()
root.title("The Lords of the Strings LOLCODE Interpreter")

pygame.mixer.init() # for sounds

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
filepathText = tk.Text(openfileUI, height = 1, width=54, bg=dark1, fg="white", selectbackground=dark2, selectforeground="white", padx=5)
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

root.mainloop()

# if __name__ == '__main__':
#     tokens = parse_terminal(sys.argv[1])
#     print(tokens)
#     parse_tree = syntax_analyzer()
#     print(variables)
#     print(("PROGRAM",parse_tree))