# Developing-a-Lightweight-Markup-Language
A python code to convert customized input syntex to html input.
A lightweight markup language (LML), also termed a simple or humane markup language, is a markup language with simple, unobtrusive syntax. It is designed to be easy to write using any generic text editor and easy to read in its raw form. Lightweight markup languages are used in applications where it may be necessary to read the raw document as well as the final rendered output.
So,
      Our main aim was to develop a lightweight markup language, in which we will define our own customized syntax and that code will return the output as a text file that will be input for a html page.

For example, in our code;
                                         We provided the symbol ‘$’ to be converted into bold sign of the html input.  
  i.e. if we are given a string, which is starting with ‘$’ and ending with the same symbol, then our python code will convert the first ‘$’ symbol with ‘<b>’ and the ending ‘$’ symbol with ‘</b><br>’.

Our code is capable to convert an alphabetic text file into a html input file. Each line will be separated with the full stop mark (‘.’).
The user is required to provide a text file with the below mentioned symbols and the code will return the corresponding html input text file.
Some input syntax, output syntax and their principal role in html output is mentioned below:
In the below table, the symbols other than alphabets are the input symbols that are required to be converted. And the string, which is between a specific symbol will remain unchanged.
The code is easy to be extended as per the requirements. Just a small modification in the code and the code will be ready for new input format along with old ones.
