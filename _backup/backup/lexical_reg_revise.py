import regex as re
import sys

reg = {
    "varident": r'^[a-zA-Z][a-zA-Z0-9_]*$',
    "numbr_literal": r'^-?([1-9][0-9]*|0)$',
    "numbar_literal": r'^(-?[0-9]*(\.[0-9]+)?)$',
    "yarn_literal": r'^\"[^\"\']*\"$',
    "troof_literal": r'^(WIN|FAIL)$',
    "type_literal": r'^(NOOB|NUMBR|NUMBAR|YARN|TROOF)$',
    "hai": r'^HAI$',
    "kthxbye": r'^KTHXBYE$',
    "wazzup": r'^WAZZUP$',
    "buhbye": r'^BUHBYE$',
    "btw": r'^BTW$',
    "obtw": r'^OBTW$',
    "tldr": r'^TLDR$',
    "ihasa": r'^I HAS A$',
    "itz": r'^ITZ$',
    "r": r'^R$',
    "sum": r'^SUM OF$',
    "diff": r'^DIFF OF$',
    "produkt": r'^PRODUKT OF$',
    "quoshunt": r'^QUOSHUNT OF$',
    "mod": r'^MOD OF$',
    "biggr": r'^BIGGR OF$',
    "smallr": r'^SMALLR OF$',
    "both": r'^BOTH OF$',
    "either": r'^EITHER OF$',
    "won": r'^WON OF$',
    "not": r'^NOT$',
    "any": r'^ANY OF$',
    "all": r'^ALL OF$',
    "bothsaem": r'^BOTH SAEM$',
    "diffrint": r'^DIFFRINT$',
    "smoosh": r'^SMOOSH$',
    "maek": r'^MAEK$',
    "a": r'^A$',
    "isnowa": r'^IS NOW A$',
    "visible": r'^VISIBLE$',
    "gimmeh": r'^GIMMEH$',
    "orly?": r'^O RLY\?$',
    "yarly": r'^YA RLY$',
    "mebbe": r'^MEBBE$',
    "nowai": r'^NO WAI$',
    "oic": r'^OIC',
    "wtf?": r'^WTF\?$',
    "omg": r'^OMG$',
    "omgwtf": r'^OMGWTF$',
    "iminyr": r'^IM IN YR$',
    "uppin": r'^UPPIN$',
    "nerfin": r'^NERFIN$',
    "yr": r'^YR$',
    "til": r'^TIL$',
    "wile": r'^WILE$',
    "imouttayr": r'^IM OUTTA YR$',
    "howiz": r'^HOW IZ I$',
    "ifusayso": r'^IF U SAY SO$',
    "gtfo": r'^GTFO$',
    "foundyr": r'^FOUND YR$',
    "iiz": r'^I IZ$',
    "mkay": r'^MKAY$',
}

def lexical_analyzer(contents):
    lines = contents.split('\n') # split contents (per line through newline) to the 'lines' list

    lexeme = "" # initialize empty temporary string
    multi_word = False # initialize multi_word to false
    for line in lines:
        chars = list(line) # split line to each character in the line to the 'chars' list
        if multi_word == False:
            lexeme = ""
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
                print("lexeme is ", lexeme)
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
                else: # if lexeme is not empty
                    print("ELSE RUNS")
                    if lexeme:
                        tokens.append(lexeme)
                        lexeme = '' # set lexeme to empty again
            else:
                lexeme += char # append char to lexeme
        if lexeme:
            tokens.append(lexeme)  # append any remaining lexeme as a lexeme
            lexeme = '' # set lexeme to empty again
        
        items = []
        
        full_quote = False
        num_quote = 0
        for i,token in enumerate(tokens):
            if token == '"':
                num_quote += 1
                if num_quote == 2:
                    num_quote = 0
                items.append(("string_delimiter", token))
            elif i > 0 and i < len(tokens)-1 and tokens[i+1] == '"' and tokens[i-1] == '"':
                if num_quote == 1:
                    items.append(("string_literal", token))
            # elif re.fullmatch(r"[a-zA-Z][a-zA-Z0-9_]*", token):
            #     items.append(("variable_identifier", token))
            # elif re.fullmatch(r"-?([1-9][0-9]*|0)", token):
            #     items.append(("numbr_literal", token))
            # elif re.fullmatch(r"-?(0|[1-9][0-9]*)(\.[0-9]+)?", token):
            #     items.append(("numbar_literal", token))
            
            # # TO-DO
            # # [] function identifier
            # # [] loop identifier
            
            # elif re.fullmatch(r"WIN|FAIL", token):
            #     items.append(("troof_literal", token))
            # elif re.fullmatch(r"NOOB|NUMBR|NUMBAR|YARN|TROOF", token):
            #     items.append(("type_literal", token))
            # elif re.fullmatch(r"HAI", token):
            #     items.append(("start_code_delimiter", token))
            # elif re.fullmatch(r"KTHXBYE", token):
            #     items.append(("end_code_delimiter", token))
            
            # # Variable Declaration
            # elif re.fullmatch(r"WAZZUP", token):
            #     items.append(("start_var_declaration_delimiter", token))
            # elif re.fullmatch(r"BUHBYE", token):
            #     items.append(("end_var_declaration_delimiter", token))
            
            # # Comments
            # elif re.fullmatch(r"BTW", token):
            #     items.append(("line_comment_delimiter", token))
            
            # # [] TO-DO Comment Literal
            
            # elif re.fullmatch(r"OBTW", token):
            #     items.append(("start_block_comment", token))
            # elif re.fullmatch(r"TLDR", token):
            #     items.append(("end_block_comment", token))
            
            # elif re.fullmatch(r"I HAS A", token):
            #     items.append(("variable_declaration", token))
            
            # elif re.fullmatch(r"ITZ", token):
            #     items.append(("variable_assignment", token))
            
            # elif re.fullmatch(r"R", token):
            #     items.append(("variable_value_reassignment", token))
                        
            # #Arithmetic/Mathematical Operations
            # elif re.fullmatch(r"SUM OF", token):
            #     items.append(("add_keyword", token))
            # elif re.fullmatch(r"DIFF OF", token):
            #     items.append(("subtract_keyword", token))
            # elif re.fullmatch(r"PRODUKT OF", token):
            #     items.append(("multiply_keyword",token))
            # elif re.fullmatch(r"QUOSHUNT OF", token):
            #     items.append(("divide_keyword",token))
            # elif re.fullmatch(r"MOD OF", token):
            #     items.append(("modulo_keyword",token))
            # elif re.fullmatch(r"BIGGR OF", token):
            #     items.append(("return_larger_number_keyword",token))
            # elif re.fullmatch(r"SMALLR OF", token):
            #     items.append(("return_smaller_number_keyword",token))
            # #Boolean Operations
            # elif re.fullmatch(r"BOTH OF", token):
            #     items.append(()"both_true_check_keyword")
            # elif re.fullmatch(r"EITHER OF", token):
            #     items.append("both_false_check_keyword")
            # elif re.fullmatch(r"WON OF", token):
            #     items.append("exactly_one_is_true_check_keyword")
            # elif re.fullmatch(r"NOT", token):
            #     items.append("negate_keyword")
            # elif re.fullmatch(r"ANY OF", token):
            #     items.append("atleast_one_true_check_keyword")
            # elif re.fullmatch(r"ALL OF", token):
            #     items.append("all_true_check_keyword")
            # #Comparison Operation Keywords
            # elif re.fullmatch(r"BOTH SAEM", token):
            #     items.append("both_argument_equal_check_keyword")
            # elif re.fullmatch(r"DIFFRINT", token):
            #     items.append("both_argument_not_equal_check_keyword")
            
            # elif re.fullmatch(r"SMOOSH", token):
            #     items.append("concatenation_keyword")
            # elif re.fullmatch(r"MAEK", token):
            #     items.append("cast_type_keyword")
            # elif re.fullmatch(r"A", token):
            #     items.append("variable_declaration_keyword")
            # elif re.fullmatch(r"IS NOW A", token): 
            # #Input/Output Keyword
            #     items.append(("variable_value_reassignment_keyword", token))
            # elif re.fullmatch(r"VISIBLE", token):
            #     items.append("print_keyword")
            # elif re.fullmatch(r"GIMMEH", token):
            # #Flow-control Keywords
            #     items.append("input_keyword")
            # elif re.fullmatch(r"O RLY", token):
            #     items.append("if_keyword")
            # elif re.fullmatch(r"YA RLY", token):
            #     items.append("if_true_keyword")
            # elif re.fullmatch(r"MEBBE", token):
            #     items.append("else_if_keyword")
            # elif re.fullmatch(r"NO WAI", token):
            #     items.append("else_keyword")
            # elif re.fullmatch(r"OIC", token):
            # #Switch-case keywods
            #     items.append(("end_of_if_block_keyword", token))    
            # elif re.fullmatch(r"WTF\?", token):
            #     items.append(("switch_keyword", token))     
            # elif re.fullmatch(r"OMG", token):
            #     items.append(("switch_case_keyword", token))   
            # elif re.fullmatch(r"OMGWTF", token):
            #     items.append(("switch_default_keyword", token))
            # #Loop related keywords/ Inc and Dec
            # elif re.fullmatch(r"IM IN YR", token):
            #     items.append(("explicit_start_loop_keyword", token))
            # elif re.fullmatch(r"UPPIN", token):
            #     items.append(("increment_keyword",token)) 
            # elif re.fullmatch(r"NERFIN", token):
            #     items.append(("decrement_keyword", token))   
            # elif re.fullmatch(r"YR", token):
            #     items.append(("concise_start_loop_keyword", token))   
            # elif re.fullmatch(r"TIL", token):
            #     items.append(("until_indicated_end_of_loop_keyword", token))
            # elif re.fullmatch(r"WILE", token):
            #     items.append(("while_indicated_end_of_loop_keyword", token))   
            # elif re.fullmatch(r"IM OUTTA YR", token):
            #     items.append(("break_loop_keyword", token))
            # #Function/Assignment keywords
            # elif re.fullmatch(r"HOW IZ I", token):
            #     items.append(("define_function_keyword", token))
            # elif re.fullmatch(r"IF U SAY SO", token):
            #     items.append(("end_of_function_keyword", token))
            # elif re.fullmatch(r"GTFO", token):
            #     items.append(("general_purpose_break_keyword", token))
            # elif re.fullmatch(r"FOUND YR", token):
            #     items.append(("return_keyword", token))
            # elif re.fullmatch(r"I IZ", token):
            #     items.append(("assignment_keyword", token))
            # elif re.fullmatch(r"MKAY", token):
            #     items.append(("end_of_assignment_keyword", token))

            # if for loop
            for i in reg_keys:
                if re.fullmatch(reg[i], token):
                    items.append((i, token))
                    break
                    
        return items



def parse(file):
    contents = open(file, 'r').read()
    tokens = lexical_analyzer(contents)
    return tokens


reg_keys = list(reg.keys())

if __name__ == '__main__':
    print(parse(sys.argv[1]))