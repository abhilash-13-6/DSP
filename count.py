def reverse_statement(statement):
    stack = []

    
    for word in statement.split():
        stack.append(word)

    reversed_words = []
    
    
    while stack:
        reversed_words.append(stack.pop())

    
    return ' '.join(reversed_words)


input_statement = "Python is a powerful language"
reversed_statement = reverse_statement(input_statement)
print("Original:", input_statement)
print("Reversed:", reversed_statement)
