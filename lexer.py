import regex as re
import sys

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
    # print("lines are:", lines)
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
                # print("THIS RUNS!!!!!!!\n\n\n")
                obtwFound = True
                # change line to empty string
                lines[i] = ""
                continue
                
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

if __name__ == '__main__':
    print(parse(sys.argv[1]))