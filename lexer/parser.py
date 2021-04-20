
from le import *
class Lexem:
    def __init__(self):
        self.tokens = None
        self.analysed = []
        self.lstructure = None
        self.offset = -1
        self.size = 0
        self.bytes = None
        self.instr = None
        self.seg = None

    def has_instruciton(self):
        for item in self.analysed:
            if 'instruction' in item:
                return True
        return False
    def segment_end_ends(self):
        for item in self.analysed:
            if ('segment' in item or 'end' in item or 'ends' in item):
                return True
        return False
    def get_instruction(self):
        for item in self.analysed:
            if 'instruction' in item:
                self.instr = item[1]
    def get_size(self):
        size = 0
        if self.instr != None:
            inst = self.instr
            if inst == 'jnz':
                operand = self.tokens[0]
                lbl = self.tokens[1]


def parse_lexems():
    parsed_list = []
    token = []
    analyse = []
    stru = []
    for item in outputfile:
        made = None
        made1 = []
        made2 = None
        test = []
        if type(item) is list:
            token.append(item)
        if type(item) is str:
            item = item.split()
            analyse.append(item)

        if type(item) is Structure:
            stru.append(item)


    for item in token:
        lexem = Lexem()
        lexem.tokens = item
        lexem.lstructure = stru[token.index(item)]
        #print(item)
        a = -1
        b = -1

        parsed_list.append(lexem)
    index = 0
    flag = 0
    for item in analyse:

        if item[0] != '1':
            parsed_list[index-1].analysed.append(item)
        else:
            index+=1
            if index != 42:
                parsed_list[index-1].analysed.append(item)
        if item == analyse[-1]:
            parsed_list[-1].analysed.append(item)
    #for x in parsed_list:
    #    print(x.__dict__)
        #break
    #print(len(parsed_list))
    #print(token)
    #print(analyse)
    #print(len(stru))
    #print(len(parsed_list))
    return parsed_list
def first():
    parsed_lexems = parse_lexems()
    offset = 0
    for lexeme in parsed_lexems:
        pass
        if lexeme.has_instruciton() == False:
            lexeme.offset = -offset
            continue
        if lexeme.segment_end_ends():
            lexeme.offset = -offset
            offset = 0
            continue
        if lexeme.has_instruciton() == True:
            lexeme.get_instruction()
        lexeme.offset = offset
