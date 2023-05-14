# PMB_CODE
a super basic programing language 


PMX Language Documentation

PMX is a custom programming language designed to provide a simplified and markup-like syntax for executing Python code. It allows you to write Python code in a more expressive and concise manner, making it easier to read and understand.

Syntax
------
The syntax of the PMX language resembles a markup language, with commands enclosed in square brackets ([]). Each command represents a specific action or functionality.

Printing Text
--------------
To print text, use the pr command followed by the text enclosed in double quotes (""):

    pr["Hello, World!"]

This command will output Hello, World! to the console.

User Input
----------
To read user input, use the inp command followed by the prompt enclosed in double quotes (""):

    name = inp["Enter your name: "]

This command will prompt the user to enter their name, and the input will be stored in the name variable.

Arithmetic Calculation
----------------------
To perform arithmetic calculations, use the calc command followed by the expression enclosed in double quotes (""):

    result = calc["2 + 3"]

This command will evaluate the expression 2 + 3 and store the result in the result variable.

Processing Lists
----------------
To process each item in a list, use the listp command followed by the list enclosed in double square brackets ([[]]):

    listp[[1, 2, 3, 4, 5]]

This command will print each item in the list on a separate line.

File Processing
---------------
To process the content of a file, use the filep command followed by the filename enclosed in double quotes (""):

    filep["example.txt"]

This command will read the content of the file example.txt and print it to the console.

Conditional Execution
---------------------
To perform conditional execution based on a condition, use the cond command followed by the condition enclosed in double quotes (""):

    condition = cond["5 > 3"]
    if condition:
        pr["Condition is true"]
    else:
        pr["Condition is false"]

This command will evaluate the condition 5 > 3. If the condition is true, it will print Condition is true, otherwise it will print Condition is false.

Looping
-------
To create a loop, use the loop command followed by the count enclosed in square brackets ([]):

    count = 3
    for i in loop[count]:
        pr["Loop iteration: " + str(i)]

This command will iterate count number of times and print the loop iteration number.

Note on Syntax
--------------
- PMX uses square brackets ([]) to enclose commands and double quotes ("") to enclose text or expressions.
- There are no indents in the PMX language. Commands are written on separate lines.
- PMX is designed to be a simplified version of Python and may not support all the features of Python.

Usage
-----
To use the PMX language, create a .pmx file and write PMX code using the syntax described above. Save the file and execute it using the Python script that interprets PMX code. The Python script will execute the PMX code and provide the desired functionality.

Make sure to have the Python script and the .pmx file in the same directory. Adjust the filenames and paths as necessary.
'''

print(pmx_documentation)



