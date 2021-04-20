from enum import Enum
from numpy import ndarray
import numpy as np

char=('+','*',':','[',']',',')

class tokenType(Enum):
    DbDirective, DwDirective, DdDirective, Instruction, SegmentKeyword, MacroKeyword, PtrKeyword, DwKey, ByteKey, EndKeyword, EndmKeyword, EndsKeyword, Register32, Register8, Symbol, Identifier, HexNumber, DecNumber, BinNumber, Text, UserSegment,SegmentRegister, Label, MacroName, Unknown = range(25)

keyword = {}

keyword["db"] = tokenType.DbDirective
keyword["dw"] = tokenType.DwDirective
keyword["dd"] = tokenType.DdDirective
keyword["segment"] = tokenType.SegmentKeyword
keyword["std"] = tokenType.Instruction
keyword["pop"] = tokenType.Instruction
keyword["inc"] = tokenType.Instruction
keyword["add"] = tokenType.Instruction
keyword["or"] = tokenType.Instruction
keyword["and"] = tokenType.Instruction
keyword["mov"] = tokenType.Instruction
keyword["cmp"] = tokenType.Instruction
keyword["jnz"] = tokenType.Instruction
keyword["ptr"] = tokenType.PtrKeyword
keyword["dword"] = tokenType.DwKey
keyword["byte"] = tokenType.ByteKey
keyword["macro"] = tokenType.MacroKeyword
keyword["end"] = tokenType.EndKeyword
keyword["endm"] = tokenType.EndmKeyword
keyword["ends"] = tokenType.EndsKeyword
keyword["eax"] = tokenType.Register32
keyword["ebx"] = tokenType.Register32
keyword["ebp"] = tokenType.Register32
keyword["esp"] = tokenType.Register32
keyword["ecx"] = tokenType.Register32
keyword["edx"] = tokenType.Register32
keyword["esi"] = tokenType.Register32
keyword["edi"] = tokenType.Register32
keyword["ah"] = tokenType.Register8
keyword["al"] = tokenType.Register8
keyword["bh"] = tokenType.Register8
keyword["bl"] = tokenType.Register8
keyword["ch"] = tokenType.Register8
keyword["cl"] = tokenType.Register8
keyword["dh"] = tokenType.Register8
keyword["dl"] = tokenType.Register8

keyword["cs"] = tokenType.SegmentRegister
keyword["ds"] = tokenType.SegmentRegister
keyword["es"] = tokenType.SegmentRegister
keyword["fs"] = tokenType.SegmentRegister
keyword["gs"] = tokenType.SegmentRegister
keyword["ss"] = tokenType.SegmentRegister

keyword["*"] = tokenType.Symbol
keyword["+"] = tokenType.Symbol
keyword[":"] = tokenType.Symbol
keyword["["] = tokenType.Symbol
keyword["]"] = tokenType.Symbol
keyword["-"] = tokenType.Symbol
keyword[","] = tokenType.Symbol
keyword["="] = tokenType.Symbol

class Token:
    def __init__(self, token: str, typel):
        self.token = token
        self.typel = tokenType(typel).name

class typeOperand:
    Const8,Const32,Register8,Register32,LabelFwd,LabelBack,Memory,Memory8,Memory32= range(9)

class Lexem:
    def __init__(self, error = '', error_token = None, hasError = None, instrInd = 0, opInd = ndarray((5,),int), opLen = [None]*5,
    opType = ndarray((5,),typeOperand), sum1 = None, sum2 = None, hasSegment = None, segment = None,
    hasLabel = False, hasName = False, hasOperands = False, hasInstructions = False, hasMacro = False,
    offset = 0, size = 0, numOfOperands = 0):
        self.error = error
        self.error_token = error_token
        self.hasError = hasError
        self.instrInd = instrInd
        self.opInd = opInd
        self.opLen = opLen
        self.opType = opType
        self.sum1 = sum1
        self.sum2 = sum2
        self.hasSegment = hasSegment
        self.segment = segment
        self.hasLabel = hasLabel
        self.hasName = hasName
        self.hasOperands = hasOperands
        self.hasInstructions = hasInstructions
        self.hasMacro = hasMacro
        self.offset = offset
        self.size = size
        self.numOfOperands = numOfOperands

    def initErro(self, error: str, tokens):
        self.error = error
        self.error_token = tokens.token
        self.hasError = True


class macro:
    def __init__(self, name, params,  start, end):
        self.name = name
        self.params = params
        self.start = start
        self.end = end
    def showMacro(self):
        print(self.name, self.params, self.start, self.end)

tokensVector = [[]]
lines = []
lexems = []
macros = []

#rint(keyword['eax'].name)
#print(lex.typel(keyword[lex.token]).name)
