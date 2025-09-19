import numpy as np

def find_largest_word_using_dsp(stream):
    
    words = stream.split()
    
    
    signal = np.array([len(word) for word in words])
    
   
    max_length = np.max(signal)  
    max_index = np.argmax(signal) 
   
    largest_word = words[max_index]
    
    return largest_word


stream_input = "Find the largest word in this stream of text right now"
largest = find_largest_word_using_dsp(stream_input)
print(f"The largest word is: {largest}")
