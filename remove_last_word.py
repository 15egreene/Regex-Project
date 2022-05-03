# Length of Last word
# Create a function that given a string as a parameter of upper/lower case letters 
# and empty space characters (" "), return the length of the last word. Meaning, 
# the word that appears far most to the right if we loop through the words.
ex = "Hello World"
# Example Output: 5

def letters(string):
    output = list(string)
    print(output)
    for x in output:
        return list(output)[-1]
letters(["mom", "dad", "dog", "time"])




def find_space(string):
    output = string.split(" ")
    x = len(output[-1])
    print(x)
find_space('stupid alex')