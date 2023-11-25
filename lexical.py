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
    "visible": r'^VISIBLE$',
}

def lexical_analyzer(contents):
    lines = contents.split('\n') # split contents (per line through newline) to the 'lines' list

    for line in lines:
        chars = list(line) # split line to each character in the line to the 'chars' list
        lexeme = "" # initialize empty temporary string
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
                if lexeme:
                    tokens.append(lexeme)  # Append non-empty lexeme as a lexeme
                    lexeme = ''
            else:
                lexeme += char # append char to lexeme
        if lexeme:
            tokens.append(lexeme)  # append any remaining lexeme as a lexeme
            
        items = []
        
        full_quote = False
        num_quote = 0
        for i,token in enumerate(tokens):
            if token == '"':
                num_quote += 1
                if num_quote == 2:
                    items.append(("string_delimiter", token))
                    num_quote = 0
            elif i > 0 and i < len(tokens)-1 and tokens[i+1] == '"' and tokens[i-1] == '"':
                items.append(("string_literal", token))
            elif re.match(r"[.a-zA-Z]+", token):
                items.append(("symbol", token))
            elif token in "+-*/":
                items.append(("expression", token))
            elif re.fullmatch(r"-?([1-9][0-9]*|0)", token):
                items.append(("numbr_literal", token))
            elif re.match(r"HAI", token):
                items.append(("code_delimiter", token))

            
            elif re.fullmatch(r"PRODUKT OF", token):
                items.append("multiply_keyword")
            elif re.fullmatch(r"QUOSHUNT OF", token):
                items.append("divide_keyword")
            elif re.fullmatch(r"MOD OF", token):
                items.append("modulo_keyword")
            elif re.fullmatch(r"BIGGR OF", token):
                items.append("return_larger_number_keyword")
            elif re.fullmatch(r"SMALLR OF", token):
                items.append("return_smaller_number_keyword")
            elif re.fullmatch(r"BOTH OF", token):
                items.append("both_true_check_keyword")
            elif re.fullmatch(r"EITHER OF", token):
                items.append("both_false_check_keyword")
            elif re.fullmatch(r"WON OF", token):
                items.append("exactly_one_is_true_check_keyword")
            elif re.fullmatch(r"NOT", token):
                items.append("negate_keyword")
            elif re.fullmatch(r"ANY OF", token):
                items.append("atleast_one_true_check_keyword")
            elif re.fullmatch(r"ALL OF", token):
                items.append("all_true_check_keyword")
            elif re.fullmatch(r"BOTH SAEM", token):
                items.append("both_argument_equal_check_keyword")
            elif re.fullmatch(r"DIFFRINT", token):
                items.append("both_argument_not_equal_check_keyword")
            elif re.fullmatch(r"MAEK", token):
                items.append("cast_type_keyword")
            elif re.fullmatch(r"A", token):
                items.append("variable_declaration_keyword")
            elif re.fullmatch(r"IS NOW A", token):
                items.append("variable_value_reassignment_keyword")
            elif re.fullmatch(r"IS NOW A", token):
                items.append("variable_value_reassignment_keyword")

            elif re.fullmatch(r"YA RLY", token):
                items.append("if_keyword")
            elif re.fullmatch(r"MEBBE", token):
                items.append("else_if_keyword")
            elif re.fullmatch(r"NO WAI", token):
                items.append("else_keyword")
            elif re.fullmatch(r"OIC", token):
                items.append("end_of_if_block_keyword")    
            elif re.fullmatch(r"WTF\?", token):
                items.append("switch_keyword")     
            elif re.fullmatch(r"OMG", token):
                items.append("switch_case_keyword")   
            elif re.fullmatch(r"OMGWTF", token):
                items.append("switch_default_keyword")
            elif re.fullmatch(r"IM IN YR", token):
                items.append("explicit_start_loop_keyword")
            elif re.fullmatch(r"UPPIN", token):
                items.append("increment_keyword") 
            elif re.fullmatch(r"NERFIN", token):
                items.append("decrement_keyword")   
            elif re.fullmatch(r"YR", token):
                items.append("concise_start_loop_keyword")   
            elif re.fullmatch(r"TIL", token):
                items.append("until_indicated_end_of_loop_keyword")
            elif re.fullmatch(r"WILE", token):
                items.append("while_indicated_end_of_loop_keyword")   
            elif re.fullmatch(r"IM OUTTA YR", token):
                items.append("break_loop_keyword")
            elif re.fullmatch(r"HOW IZ I", token):
                items.append("define_function_keyword")
            elif re.fullmatch(r"IF U SAY SO", token):
                items.append("end_of_function_keyword")
            elif re.fullmatch(r"GTFO", token):
                items.append("general_purpose_break_keyword")
            elif re.fullmatch(r"FOUND YR", token):
                items.append("return_keyword")
            elif re.fullmatch(r"I IZ", token):
                items.append("assignment_keyword")
            elif re.fullmatch(r"MKAY", token):
                items.append("end_of_code_block_keyword")

            # if for loop
            for i in reg_keys:
                if re.fullmatch(reg[i], token):
                    items.append((i, token))
                    
        return items



def parse(file):
    contents = open(file, 'r').read()
    tokens = lexical_analyzer(contents)
    return tokens




# iterate reg keys
# if match, append to items
# place reg keys in a list

reg_keys = list(reg.keys())



if __name__ == '__main__':
    print(parse(sys.argv[1]))