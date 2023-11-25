import regex as re

# token = "0000950"
# if re.fullmatch(r"-?([1-9][0-9]*|0)", token):
#     print("TRUE")
# else: 
#     print("FALSE")

lines = [
    'This is                a "string" with "multiple words" and "PRODUKT            OF" and QUOSHUNT OF'
]


for line in lines:
    chars = list(line)
    lexeme = ""
    tokens = []
    in_quotes = False

    for char in chars:
        if char == '"':
            if in_quotes:  # If in_quotes is True (already inside quotes)
                if lexeme:
                    tokens.append(lexeme)  # Append the string inside quotes as a lexeme
                    lexeme = ''
            tokens.append(char)  # Append the quote '"' itself as a lexeme
            in_quotes = not in_quotes  # Toggle in_quotes
        elif char == " " and not in_quotes:
            if lexeme:
                tokens.append(lexeme)  # Append non-empty lexeme as a lexeme
                lexeme = ''
        else:
            lexeme += char  # Append char to lexeme

    # Check for specific phrases not within quotes
    if lexeme.upper() == "PRODUKT OF" or lexeme.upper() == "QUOSHUNT OF":
        tokens.append(lexeme)  # Append the specific phrase as a lexeme

    if lexeme:
        tokens.append(lexeme)  # Append any remaining lexeme as a lexeme

    # Printing tokens to check the output
    print(tokens)

# token = "-0"

# if re.fullmatch(r"(-?(0|[1-9][0-9]*)(\.[0-9]+)?)", token):
#     print("TRUE")
# else:
#     print("FALSE")