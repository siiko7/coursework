from tokentype import *
import re

instructionType = [
    tokenType.Instruction,
    tokenType.DbDirective,
    tokenType.DwDirective,
    tokenType.DdDirective,
    tokenType.SegmentKeyword,
    tokenType.MacroKeyword,
    tokenType.EndKeyword,
    tokenType.EndmKeyword,
    tokenType.MacroName,
    tokenType.EndsKeyword
]

HexRegex = re.compile(r"^-?[0-9a-f]+h$")
DecRegex = re.compile(r"^-?[0-9]+$")
BinRegex = re.compile(r"^-?[01]+b$")
strRegex = re.compile(r"^\"[A-Za-z0-9 ]+\"$")

def isEmpty(c: int) -> bool:
    return c == '\r' or c == ' ' or c == '\n' or c == '\t' or c == '\0'

def isDelim(s: int) -> bool:
    return isEmpty(s) or s == '*' or s == ',' or s == '[' or s == ']' or s == '+' or s == '=' or s == ':'

def matchConst(num: int) -> tokenType:
    if HexRegex.match(num):
        return tokenType.HexNumber
    elif DecRegex.match(num):
        return tokenType.DecNumber
    elif BinRegex.match(num):
        return tokenType.BinNumber
    elif strRegex.match(num):
        return tokenType.Text
    else:
        return tokenType.Unknown

def hasMacro(line):
    for item in line:
        if item.typel == 'MacroName' or item.typel == 'Identifier':
            for i in macros:
                if item.token == i.name:
                    return i
    return False

def removeSpaces(s: str) -> str:
    newstr = s.strip()
    return newstr

def fillTokensVector(s: str, line: int):
    rem = removeSpaces(s)
    if len(rem) != 0:
        #itr =
        #print(itr)
        if rem in list(keyword.keys()):
        #if itr != keyword[[*keyword.keys()][-1]]:
        #if itr.name in keyword.items():
            tmpToken = Token(rem,tokenType(keyword[rem].value))
            #print(tokenType(keyword[rem].value))
            #print(tmpToken.typel(keyword[rem]).value)
            #print(tokenType(12).name)
            tokensVector.append([])
            tokensVector[line].append(tmpToken)
        else:


            kek = tokenType(matchConst(rem))
            if kek.name == 'Unknown':
                kek = tokenType.Identifier
            #print(kek)
            #print(tokenType( kek).name)
            push = Token(rem,kek)
            tokensVector.append([])
            tokensVector[line].append(push)

def tokenize(filename: str):
    isText = False
    size = 0
    token = ''
    line = 0

    test = open(filename, "r")

    for linel in test:
        if linel=='' or linel == '\n':
            continue
        linel = linel.split(';',1)[0]
        linel = linel.lower()

        i = 0
        while i < len(linel):
            if linel[i] in char:
                """separate lexems"""
                symbol = linel[i]
                linel = linel.split(symbol,1)
                linel=linel[0]+' '+symbol+' '+linel[1]
                i+=3
            else:
                i+=1
        linel = linel.split()
        for item in linel:
            if any('"' in item for item in linel) :
                count = 0
                for i in range(len(linel)):
                    if linel[i].startswith('"') and i+1!=len(linel):
                        for j in range(i+1, len(linel)):
                            linel[i] += ' ' + linel[j]
                            count +=1
                linel = linel[:len(linel)-count]
        if linel != []:
            lines.append(linel)
    test.close()
    lineindx = 0
    for line in lines:
        inx = len(line)
        for lex in line:
            fillTokensVector(lex, lineindx)
            #print(lex)
            if line.index(lex) == inx-1:
                lineindx+=1
                #print(lineindx)

def removeEmpty():
    global tokensVector
    tokensVector = [x for x in tokensVector if x != []]

listen = macro(0,0,0,0)
def initLexems(line: int):
    listening = []
    #lex = Lexem()
    global macros
    global listen
    lexems[line] = Lexem()
    if len(tokensVector[line]) == 2 and tokensVector[line][0].typel == 'Identifier' and (tokensVector[line][1].typel == 'SegmentKeyword' or tokensVector[line][1].typel == 'EndsKeyword'):
        tokensVector[line][0].typel = tokenType.UserSegment.name

        lexems[line].hasName = True
    elif len(tokensVector[line]) == 3 and tokensVector[line][1].typel == 'DbDirective':
        lexems[line].hasName = True
    elif len(tokensVector[line]) == 3 and tokensVector[line][1].typel == 'DdDirective':
        lexems[line].hasName = True
    elif len(tokensVector[line]) == 3 and tokensVector[line][1].typel == 'DwDirective':
        lexems[line].hasName = True
    elif len(tokensVector[line]) == 2 and tokensVector[line][0].typel == 'Identifier' and tokensVector[line][1].token == ':':
        tokensVector[line][0].typel = tokenType.Label
        lexems[line].hasLabel = True
    elif len(tokensVector[line]) >= 2 and tokensVector[line][0].typel == 'Identifier' and tokensVector[line][1].typel == 'MacroKeyword':
        m = macro(0,[],0,0)
        #listen = macro()
        tokensVector[line][0].typel == 'MacroName'
        m.name = tokensVector[line][0].token
        m.start = line

        lexems[line].hasName = True

        if len(tokensVector[line]) != 2:
            for i in range(2,len(tokensVector[line])):
                m.params.append(tokensVector[line][i].token)
        #m.showMacro()

        listen = m

    elif len(tokensVector[line]) == 1 and tokensVector[line][0].typel == 'EndmKeyword':
        #global listen
        listen.end = line
        macros.append(listen)
        #listening.append(listen)
        #listen.showMacro()

        #listen.showMacro()
    elif tokensVector[line][0].typel == 'Identifier':
        macrotemp = hasMacro(tokensVector[line])
        if (macrotemp != False or macrotemp.name != tokensVector[line][0].token):
            lexems[line].hasName = True
    elif tokensVector[line][0].typel != 'EndKeyword' and tokensVector[line][0].typel != 'Instruction':
        lexems[line].initErro('Unknown lexem', tokensVector[line][0])
        return

    structure(line)
    #for item in listening:
    #    item.showMacro()

def instructionCheck(offset: int, line: int) -> bool:
    for i in range(0,10):
        if tokensVector[line][offset].typel == instructionType[i].name:
            return True
    return False

def structure(line: int):
    offset = 0
    if lexems[line].hasName:
        offset+=1
    elif lexems[line].hasLabel:
        offset+=2

    if len(tokensVector[line]) == offset:
        if offset == 1 and hasMacro(tokensVector[line])==False:
            lexems[line].initErro('Name without instruction', tokensVector[line][0])
        return

    if instructionCheck(offset,line):
        if offset == 1 and tokensVector[line][offset].typel == 'Instruction':
            lexems[line].initErro("Instruction bad", tokensVector[1])
            return
        lexems[line].hasInstructions = True
        lexems[line].instrInd = offset
    else:
        m = hasMacro(tokensVector[line])
        print(m)
        if (m!=False or m.name != tokensVector[line][offset].token):
            print("LEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            lexems[line].initErro("Exptected instruction or directive", tokensVector[line][0])
            return

    offset+=1
    if len(tokensVector[line]) == offset:
        return

    coma = -1
    for i in range(0,len(tokensVector[line])):
        if tokensVector[line][i].token == ',':
            coma = i

    lexems[line].hasOperands = True
    lexems[line].numOfOperands = 1
    lexems[line].opInd[1] = offset

    if coma != -1:
        lexems[line].opLen[1] = coma - offset
        lexems[line].numOfOperands = 2
        lexems[line].opInd[2] = coma + 1
        lexems[line].opLen[2] = len(tokensVector[line]) - coma - 1
    else:
        lexems[line].opLen[1] = len(tokensVector[line]) - offset


def proceedTokens():
    removeEmpty()
    global lexems
    lexems = [None] * len(tokensVector)

    for i in range(0, len(tokensVector)):
        initLexems(i)

    for i in range(0, len(tokensVector)):
        if lexems[i].hasError:
            continue

        m = hasMacro(tokensVector[i])

        if m == False:
            continue
        else:
            print(m.__dict__)

        lexems[i].hasMacro = True





tokenize("test1.asm")
proceedTokens()

"""
for item in tokensVector:
    for items in item:
        print(items.token, items.typel)
"""

#for line in lines:
 #   print(line)
#fillTokensVector(string,0)


#print(hasMacro(tokensVector[0]))
#initLexems(2)

#for item in macros:
#    item.showMacro()

for line in lexems:
    print(line.__dict__, '\n\n')

#for item in macros:
#    print(item.__dict__)
