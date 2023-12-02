from lexical import Token, parse
import sys

# Errors

# Nodes

# Parts
def program():
    pass

def syntax_analyzer(tokens):
    idx = 0
    currToken = tokens[idx]
    lineidx = 0
    
    ast = program()
        
if __name__ == '__main__':
    tokens = parse(sys.argv[1])
    ast = syntax_analyzer(tokens)
    print(ast)