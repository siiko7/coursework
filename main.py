from le import *
import os

copyfile("test1.asm", 'tmp.asm')
lexanal("tmp.asm", "lex.txt")
sentence_struct("tmp.asm", "struct.txt")
firstie("tmp.asm","lex.txt","lst.txt")

for filename in os.listdir('.'):
    f = os.path.join('.',filename)
    if os.path.isfile(f):

        if '.py' in f or 'test1.asm' in f or 'TASM' in f or 'lst' in f or 'test2.asm' in f or 'TEST2.LST' in f:
            print(f)
        else:
            os.remove(f)
    
            
                
