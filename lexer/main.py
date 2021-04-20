from le import *
from parser import *
copyfile("test1.asm", 'tmp.asm')
#print(dealwithmacro("tmp.asm"))
lexanal("tmp.asm", "lex.txt")
#macro_analysis(outputfile)
sentence_struct("tmp.asm", "struct.txt")
"""
for item in dreamlist:
    print(item.__dict__)
"""
#delete_macro('tmp.asm','tmp1.asm')
#lexanal('tmp1.asm')
firstie("tmp.asm","lex.txt","lst.txt")
