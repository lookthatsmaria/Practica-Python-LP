import os
import sys

from antlr4 import *
from logo3dLexer import logo3dLexer
from logo3dParser import logo3dParser
from visitor import Visitor

# In order to start the program, we write a new line with a call to
# a procediment specified by the user in the arguments, if not is
# given, by default, the program calls to to the main
if len(sys.argv) == 2:
    file_object = open(sys.argv[1], 'a')
    file_object.write('\nmain()')
    file_object.close()
else:
    call = sys.argv[2] + '(' + sys.argv[3]
    for i in range(4, len(sys.argv)):
        call = call + ','
        call = call + sys.argv[i]
    call = call + ')'
    file_object = open(sys.argv[1], 'a')
    file_object.write('\n')
    file_object.write(call)
    file_object.close()

input_stream = FileStream(sys.argv[1])
lexer = logo3dLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = logo3dParser(token_stream)
tree = parser.root()
visitor = Visitor()
visitor.visit(tree)

# Removes the last line from file (the call that we added in the beginning)
with open(sys.argv[1], "r+", encoding="utf-8") as file:
    file.seek(0, os.SEEK_END)
    pos = file.tell() - 1
    while pos > 0 and file.read(1) != "\n":
        pos -= 1
        file.seek(pos, os.SEEK_SET)
    if pos > 0:
        file.seek(pos, os.SEEK_SET)
        file.truncate()
