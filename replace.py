def replace_words(text, replacement_map):
    
    words = text.split()
    
    
    replaced_words = [
        replacement_map.get(word, word) for word in words
    ]
    
   
    return ' '.join(replaced_words)


text = "Python is great and Python is easy"
replacement_map = {
    "Python": "Java",
    "easy": "fun"
}

result = replace_words(text, replacement_map)
print("Original Text:", text)
print("Modified Text:", result)
