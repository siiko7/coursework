
from enum import Enum
import re

class tokenType(Enum):
    DbDirective, DwDirective, DdDirective, Instruction, SegmentKeyword, MacroKeyword, PtrKeyword, DwKey, ByteKey, EndKeyword, EndmKeyword, EndsKeyword, Register32, Register8, Symbol, Identifier, HexNumber, DecNumber, BinNumber, Text, UserSegment,SegmentRegister, Label, MacroName, Unknown = range(25)

class end_token:
    def __init__(self):
        strtoken = None
        typet = None

class macro:
    def __init__(self):
        self.name = None
        self.params = []
        self.start = -1
        self.end = -1

class Lexem:
    def __init__(self):
        self.error = ''
        self.error_token = None
        self.has_error = None

        self.instrIndex = 0;

        self.operandIndices = [None] * 5
        self.operandLengths = [None] * 5
        self.operandTypes =[None] * 5
        self.sum1_tk = []
        self.sum2_tk = []

        self.has_segment_prefix = None
        self.segment_prefix = None
        self.bytes = None

        self.hasLabel = False
        self.hasName = False
        self.hasOperands = False
        self.hasInstruction = False
        self.hasMacro = False
        self.offset = 0
        self.size = 0
        self.numberOfOperands = 0

    def SetError(self, error, end_token):
        self.error = error
        self.error_token = end_token
        self.has_error = True

char=('+','*',':','[',']',',')
keyword = { }
keyword["db"] = tokenType.DbDirective.name
keyword["dw"] = tokenType.DwDirective.name
keyword["dd"] = tokenType.DdDirective.name
keyword["segment"] = tokenType.SegmentKeyword.name
keyword["std"] = tokenType.Instruction.name
keyword["pop"] = tokenType.Instruction.name
keyword["inc"] = tokenType.Instruction.name
keyword["add"] = tokenType.Instruction.name
keyword["or"] = tokenType.Instruction.name
keyword["and"] = tokenType.Instruction.name
keyword["mov"] = tokenType.Instruction.name
keyword["cmp"] = tokenType.Instruction.name
keyword["jnz"] = tokenType.Instruction.name
keyword["ptr"] = tokenType.PtrKeyword.name
keyword["dword"] = tokenType.DwKey.name
keyword["byte"] = tokenType.ByteKey.name
keyword["macro"] = tokenType.MacroKeyword.name
keyword["end"] = tokenType.EndKeyword.name
keyword["endm"] = tokenType.EndmKeyword.name
keyword["ends"] = tokenType.EndsKeyword.name
keyword["eax"] = tokenType.Register32.name
keyword["ebx"] = tokenType.Register32.name
keyword["ebp"] = tokenType.Register32.name
keyword["esp"] = tokenType.Register32.name
keyword["ecx"] = tokenType.Register32.name
keyword["edx"] = tokenType.Register32.name
keyword["esi"] = tokenType.Register32.name
keyword["edi"] = tokenType.Register32.name
keyword["ah"] = tokenType.Register8.name
keyword["al"] = tokenType.Register8.name
keyword["bh"] = tokenType.Register8.name
keyword["bl"] = tokenType.Register8.name
keyword["ch"] = tokenType.Register8.name
keyword["cl"] = tokenType.Register8.name
keyword["dh"] = tokenType.Register8.name
keyword["dl"] = tokenType.Register8.name
keyword["*"] = tokenType.Symbol.name
keyword["+"] = tokenType.Symbol.name
keyword[":"] = tokenType.Symbol.name
keyword["["] = tokenType.Symbol.name
keyword["]"] = tokenType.Symbol.name
keyword["-"] = tokenType.Symbol.name
keyword[","] = tokenType.Symbol.name
keyword["="] = tokenType.Symbol.name

numberHexRegex = re.compile(r"^-?[0-9a-f]+h$")
numberDecRegex = re.compile(r"^-?[0-9]+$")
stringRegex = re.compile(r"^\"[A-Za-z0-9 ]+\"$")
identifierRegex = re.compile(r"^-?[a-z]\w*$")

vectorOfTokens = [[]]
lines = []
lexems = []
macros = []
listeningMacro = macro()

instrucions = [tokenType.Instruction, tokenType.DbDirective, tokenType.DwDirective, tokenType.DdDirective, tokenType.SegmentKeyword, tokenType.MacroKeyword, tokenType.EndKeyword, tokenType.EndmKeyword, tokenType.EndsKeyword, tokenType.MacroName]

def tokenTypeByValue(value: str) -> int:
    if numberDecRegex.match(value):
        return tokenType.DecNumber
    elif stringRegex.match(value):
        return tokenType.Text
    elif numberHexRegex.match(value):
        return tokenType.HexNumber
    elif identifierRegex.match(value):
        return tokenType.Identifier

    return -1

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
            #vectorOfTokens = end_token(rem,tokenType(keyword[rem].value))
            Token = end_token()
            Token.strtoken = rem
            Token.typet = keyword[rem]
            #print(tokenType(keyword[rem].value))
            #print(tmpToken.typet(keyword[rem]).value)
            #print(tokenType(12).name)
            vectorOfTokens.append([])
            vectorOfTokens[line].append(Token)
        else:


            kek = tokenType(tokenTypeByValue(rem))
            push = end_token()
            push.strtoken = rem
            push.typet = kek.name
            vectorOfTokens.append([])
            vectorOfTokens[line].append(push)


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
    removeEmpty()


def removeEmpty():
    global lis
    global vectorOfTokens
    vectorOfTokens = [x for x in vectorOfTokens if x != []]

def hasMacro(tokens):
    for token in tokens:
        if token.typet == 'MacroName' or token.typet == 'Identifier':
            for i in macros:
                if i.name.strtoken == token.strtoken:
                    return i
    return 0

def initLexems(line):
    global listeningMacro
    lexems[line] = Lexem()
    if len(vectorOfTokens[line]) == 2 and vectorOfTokens[line][0].typet == 'Identifier' and (vectorOfTokens[line][1].typet == 'SegmentKeyword' or vectorOfTokens[line][1].typet == 'EndsKeyword'):
        vectorOfTokens[line][0].typet = tokenType.UserSegment.name

        lexems[line].hasName = True
    elif len(vectorOfTokens[line]) == 3 and vectorOfTokens[line][1].typet == 'DbDirective':
        lexems[line].hasName = True
    elif len(vectorOfTokens[line]) == 3 and vectorOfTokens[line][1].typet == 'DdDirective':
        lexems[line].hasName = True
    elif len(vectorOfTokens[line]) == 3 and vectorOfTokens[line][1].typet == 'DwDirective':
        lexems[line].hasName = True
    elif len(vectorOfTokens[line]) == 2 and vectorOfTokens[line][0].typet == 'Identifier' and vectorOfTokens[line][1].strtoken == ':':
        vectorOfTokens[line][0].typet = tokenType.Label.name
        lexems[line].hasLabel = True
    elif len(vectorOfTokens[line]) >= 2 and vectorOfTokens[line][0].typet == 'Identifier' and vectorOfTokens[line][1].typet == 'MacroKeyword':
        m = macro()
        vectorOfTokens[line][0].typet = 'MacroName'
        m.name = vectorOfTokens[line][0]
        m.start = line
        m.start = line

        lexems[line].hasName = True

        if len(vectorOfTokens[line]) != 2:
            for i in range(2,len(vectorOfTokens[line])):
                m.params.append(vectorOfTokens[line][i])
        listeningMacro = m
        #print(listeningMacro.__dict__)
        #print(listeningMacro.name.strtoken, [x.strtoken for x in listeningMacro.params])
    elif len(vectorOfTokens[line]) == 1 and vectorOfTokens[line][0].typet == 'EndmKeyword':
         listeningMacro.end = line
         macros.append(listeningMacro)
    elif vectorOfTokens[line][0].typet == 'Identifier':
        tmp = macro()
        if tmp != 0 or tmp.name.strtoken != vectorOfTokens[line][0].strtoken:
            lexems[line].hasName = True
    elif vectorOfTokens[line][0].typet != 'EndKeyword' and vectorOfTokens[line][0].typet != 'Instruction':
        lexems[line].SetError("Unknown lexem type", vectorOfTokens[line][0].strtoken)
        return

    determineStructure(line)

def isInstrucion(offset, line):
    for i in range(0, 10):
        if vectorOfTokens[line][offset].typet == instrucions[i].name:
            return True
    return False

def determineStructure(line):
    offset = 0

    if lexems[line].hasName:
        offset += 1
    elif lexems[line].hasLabel:
        offset += 2

    if len(vectorOfTokens[line]) == offset:
        if offset == 1 and hasMacro(vectorOfTokens[line]) == 0:
            lexems[line].SetError("Name without instruction", vectorOfTokens[line][0])
        return

    if isInstrucion(offset,line):
        if offset == 1 and vectorOfTokens[line][offset].typet == 'Instruction':
            lexems[line].SetError("Named instruction", vectorOfTokens[line][1])
            return
        lexems[line].hasInstruction = True
        lexems[line].instrIndex = offset
    else:
        m = hasMacro(vectorOfTokens[line])
        if not m or m.name.strtoken != vectorOfTokens[line][offset-1].strtoken:
            lexems[line].SetError("Expected instruction or directive", vectorOfTokens[line][0])
            return

    offset += 1
    if len(vectorOfTokens[line]) == offset:
        return

    coma = -1
    for i in range(offset,len(vectorOfTokens[line])):
        if vectorOfTokens[line][i].strtoken == ',':
            coma = i
    lexems[line].hasOperands = True
    lexems[line].numberOfOperands = 1
    lexems[line].operandIndices[1] = offset

    if coma != -1:
        lexems[line].operandLengths[1] = coma - offset
        lexems[line].numberOfOperands = 2
        lexems[line].operandIndices[2] = coma+1
        lexems[line].operandLengths[2] = len(vectorOfTokens[line]) - coma -1
    else:
        lexems[line].operandLengths[1] = len(vectorOfTokens[line]) - offset

def proceedTokens():
    removeEmpty()
    global lexems
    lexems = [None] * len(vectorOfTokens)
    for i in range(0, len(vectorOfTokens)):
        initLexems(i)
    for i in range(0, len(vectorOfTokens)):
        if lexems[i].has_error:
            continue
        m = hasMacro(vectorOfTokens[i])
        if m == 0:
            continue

        lexems[i].hasMacro = True

        if len(vectorOfTokens[i])-1 != len(m.params):
            continue

        param_replace = {}
        for p in range(0, len(m.params)):
            param_replace[m.params[p].strtoken] = vectorOfTokens[i][p+1]
        print(param_replace)
        for j in range(m.start+1, m.end):
            vectorOfTokens.insert(i+1,vectorOfTokens[j])
            lexems.insert(i+1,lexems[j])
            i+=1



        #if items.strtoken in alist.keys():
    #for item in alist:
    #    print(item,alist[item].strtoken)

tokenize('test1.asm')
proceedTokens()


for token in vectorOfTokens:
    for tokens in token:
        print(tokens.__dict__)


    #print(lexems[i].__dict__, '\n')

#print(vectorOfTokens[0][0].typet)
#print(len(lexems))

"""
for macro in macros:
    print(macro.__dict__)
    print(macro.name.strtoken, [x.strtoken for x in macro.params])
"""
