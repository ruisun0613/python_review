"""
10-1. Learning Python: Open a blank file in your text editor and write a
few lines summarizing what you’ve learned about Python so far. Start each
line with the phrase In Python you can. . . . Save the file as
learning_python.txt in the same directory as your exercises from this
chapter. Write a program that reads the file and prints what you wrote two
times: print the contents once by reading in the entire file, and once by
storing the lines in a list and then looping over each line.
"""
from pathlib import Path

path = Path('python/chapter10/learning_python.txt')
contents = path.read_text()
print(contents)

# storing the lines
lines = contents.splitlines()
print(lines)
for line in lines:
    print(line)
"""
10-2. Learning C: You can use the replace() method to replace any word in
a string with a different word. Here’s a quick example showing how to
replace 'dog' with 'cat' in a sentence:
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.
"""
java_language = contents.replace("Python", "Java")
cpp_language = contents.replace("Python", "C++")

print(java_language)
print(cpp_language)
"""
10-3. Simpler Code: The program file_reader.py in this section uses a
temporary variable, lines, to show how splitlines() works. You can skip the
temporary variable and loop directly over the list that splitlines() returns:
for line in contents.splitlines():
Remove the temporary variable from each of the programs in this section,
to make them more concise.
"""
for line in contents.splitlines():
    print(line)