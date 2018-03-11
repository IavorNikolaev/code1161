"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# i think this will give me a list of the words in the brackets 
some_words = ['what', 'does', 'this', 'line', 'do', '?'] # this gave me a the list of the words in the brackets 
# Each element in the list will be asigned to the value word, then each value in the some_words list will be printed one by one. 
for word in some_words: #the above happened 
    print(word)

for x in some_words:# Each element in the list will be asigned to the value X, then each value in the some_words list will be printed one by one.
    print(x) # The above happened 

print(some_words) #the list of some_words will be printed 
# The above happened 

if len(some_words) > 3: #If the list Some_words contains more than 3 ellements then the string bellow will be printed.
    print('some_words contains more than 3 words') #The above happened 

def usefulFunction(): # It will print a list of six atributes 
    # It printed six features of my computer 
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
