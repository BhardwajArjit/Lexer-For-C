from lexer import CLexer

# Read input from an external text file
file_pathname = 'code.txt'  
with open(file_pathname, 'r') as file:
    code_from_file = file.read()

# Create lexer and get tokens
lexer = CLexer(code_from_file)
tokens = lexer.get_tokens()

# Print tokens to the terminal
for token in tokens:
    if len(token) == 3:  # Check if the token has an address (for IDENTIFIER)
        print(f'{token[0]}: {token[1]} (Address: {token[2]})')
    else:
        print(f'{token[0]}: {token[1]}')
