from lexer import CLexer  

# Read input from an external text file
file_pathname = 'code.txt'  
with open(file_pathname, 'r') as file:
    code_from_file = file.read()

# Create lexer and display tokens as a table
lexer = CLexer(code_from_file)
lexer.display_tokens_table()
