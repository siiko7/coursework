from data import *
import re, string
import shutil
#Створення по тестовій програмі таблиць лексем та таблиць структури речень
"""
таблица лекем:
номер, лексема, длина лексемы в символах тип лексемы

таблица структур речення:

"""
dreamlist = []
macrosure = []

class Structure:
	def __init__(self):
		self.m = -1
		self.mn = -1
		self.lenmn = -1
		self.op1 = -1
		self.lenop1 = -1
		self.op2 = -1
		self.lenop2 = -1

class MacroKiller:
	def __init__(self, macrocommand, inside):
		self.macrocommand = macrocommand
		self.inside = inside
	def add_macro(self,macroc):
		self.macrocommand.append(macroc)
	def add_inside(self,insideadd):
		self.inside.append(insideadd)
	def show(self):
		print(self.macrocommand,'\n',self.inside)

macro_dick={}
macro_list=[]
outputfile = []

def mac2args(listfrommacro,replace,item):
	change = listfrommacro
	for i in range(0, len(change)):
		if change[i] == replace:
			change[i] = item
	return change

def remove_duplicates(lst):
    res = []
    for x in lst:
        if x not in res:
            res.append(x)
    return res

def copyfile(testfile,tmpfile):
	tmpfile = open(tmpfile, "w")
	global macrosure
	flag2 = 0
	status = 0
	flag = 0
	kekfile = []
	anotherone = []
	newlist = []
	nw2=[]
	slst =[]
	save =''
	with open(testfile) as test:
		for line in test:
			if line=='' or line=='\n':
				continue
			line = line.split(';',1)[0] #remove comments
			line = line.lower() #read lines in lowercase

			i=0

			while i < len(line):
				if line[i] in char:
					"""separate lexems"""
					symbol = line[i]
					line = line.split(symbol,1)
					line=line[0]+' '+symbol+' '+line[1]
					i+=3
				else:
					i+=1
			lexem = ''
			#print(line)
			line = line.split()

			#print(line)
			for item in line:
				if any('"' in item for item in line) :
					count = 0
					for i in range(len(line)):
						if line[i].startswith('"') and i+1!=len(line):
							for j in range(i+1, len(line)):
								line[i] += ' ' + line[j]
								count +=1
					line = line[:len(line)-count]
			#print(line)
			for i in range(0,len(line)):

				if line[i] == 'macro'and len(line) == 2:
					macrok = MacroKiller([],[])
					macrok.add_macro(line[0:-1])
					flag = 1
					break
				elif line[i] == 'macro'and len(line) == 3:
					macrok = MacroKiller([],[])
					macrok.add_macro(line[::len(line)-1])
					flag = 1
					break
				if flag == 1:

					if line[i] == 'endm':
						flag = 0
						continue
					macrok.add_inside(line)
					dreamlist.append(macrok)

					break
			#outputfile.append(line)


								#outputfile.append(macroiter(list[j-1])[i])
			#for item in line:
			#outputfile.append(line)
			kekfile.append(line)
	macrosure = remove_duplicates(dreamlist)
	#print(len(dreamlist))
	#for i in range(0,len(macrosure)):
		#if dreamlist[i]==dreamlist[i-1]:
	#	macrosure[i].show()
	#for mac in macrosure:
	#	mac.show()
	#macrok.show()
	#print(type(macrok.macrocommand))
	finalplease = iwantout(kekfile)
	#print(macrosure)
	#iwantout(kekfile)
	#iwantout(kekfile)

	#print(finalplease)

	#print(kekfile,'\n')
	#print(macro_list)
	for list_ in finalplease:
		tmpfile.write(' '.join(list_) + '\n')
	tmpfile.close()


def iwantout(lst):
	flag = 0
	appendthis = []
	mac2 = []
	change = ''
	toChange = ''
	foundMacro = 0
	kek = 0
	flag2 = 0
	macdi = {}
	liap=0
	for line in lst:
		#print(line)
		appendthis.append(line)
		for mac in macrosure:
			for item in mac.macrocommand:
				if item == line:
					for item2 in mac.inside:
						appendthis.append(item2)
				else:
					if len(item)== len(line)==2 and item[0] in line:
						for item2 in mac.inside:
							#print(line)
							#appendthis.append(item2)
							newlist =list(item2) + list(line[1].split(' '))
							newlist.pop(newlist.index(item[1]))
							#print(newlist)
							appendthis[1:] += [newlist]
							break
							#print(appendthis[appendthis.index(item2)])
							#print(appendthis.index(item2))
					#	break




	#print(mac2)
	return appendthis

def macroiter(macroword,listing):
	tmplist = []
	flag = 0
	for i in range(0,len(listing)):
		if 'macro' in listing[i-1] and macroword in listing[i-1]:
			#print(macro_list[i])
			flag = 1
			#break
		if flag == 1:
			tmplist.append(listing[i])
			if 'endm' in listing[i+1]:
				flag = 0
				continue
			#break
	return tmplist
def lexanal(testfile, outfile):
	global macro_list
	macrostring = []
	outfile = open(outfile, "w")
	newline = []
	macroname=''
	macroplace=[]
	macrocommands=[]

	flag = 0
	index = 0
	with open(testfile) as test:
		for line in test:
			n=0
			i=0

			if line=='' or line=='\n':
				continue
			n = 0 #lexem number
			i=0
			line = line.split(';',1)[0] #remove comments
			line = line.lower() #read lines in lowercase



			while i < len(line):
				if line[i] in char:
					#separate lexems
					symbol = line[i]
					line = line.split(symbol,1)
					line=line[0]+' '+symbol+' '+line[1]
					i+=3
				else:
					i+=1


			lexem = ''
			#print(line)
			line = line.split()

			#print(line)

			for item in line:
				if any('"' in item for item in line) :
					count = 0
					for i in range(len(line)):
						if line[i].startswith('"') and i+1!=len(line):
							for j in range(i+1, len(line)):
								line[i] += ' ' + line[j]
								count +=1
					line = line[:len(line)-count]


								#outputfile.append(line2)
			outputfile.append(line)
			#print(line)
			"""
			for item in line:
				if any('"' in item for item in line) :
					count = 0
					for i in range(len(line)):
						if line[i].startswith('"') and i+1!=len(line):
							for j in range(i+1, len(line)):
								line[i] += ' ' + line[j]
								count +=1
					line = line[:len(line)-count]
			"""

					#macro_list.append(line)

				#print(line)
				#break
			"""
			for i in range(0,len(outputfile)):
				for list in macro_list:
					for j in range(0,len(list)):
						if list[j] == 'macro' and list[j-1] in outputfile[i] and 'macro' not in outputfile[i]:
							if len(outputfile[i]) == 1:
								#print(macroiter(list[j-1]))
								#outputfile.insert()

								outputfile.insert(i+1,macroiter(list[j-1])[0])


				#               for k in range(0,len(macro_list)):
				#                   if list[j-1] in macro_list[k-1]:
				#                       print(macro_list[k])
				#                       continue
								break
							if len(outputfile[i]) == 2:
								#print(outputfile[i])
								#print(next(iter(macro_list)))
								break
							#print(list)
							break
					#   break
					#break
				#break
				"""
				#print(outputfile[i])
			for item in line:
				lexem = item
				typel = lextype(lexem)
				n+=1

				if typel == 'string_const':
					lexem=lexem[1:len(lexem)-1]

				lexem = lexem.strip()
				#print(lexem)
				length = len(lexem)
				#print(line)
				#print(n, lexem, length, typel)
				new_list = '{} {} {} {}'.format(n,lexem,length,typel)
				outputfile.append(new_list)


				#print(new_list)
				#outputfile.append(n,lexem,length,typel)
				outfile.write('%d'%n)
				outfile.write(' %s'%lexem)
				outfile.write(' %d'%length)
				outfile.write(' %s'%typel)
				outfile.write('\n')
				lexem = ''
			outputfile.append('')
	#print(outputfile)
	#print(macro_list)
	#print(macrostring)
	#print(macroiter('mac1'))
	#for i in range(0, len(outputfile)):
	#   print(outputfile[i])
	#for i in range(0, len(macroplace)):
	#   print(macroplace[i])
	#macroplace[0].remove("macro")
	#for i in range(0, len(macroplace)):
#       print(macroplace[i])
	#print(macroname)
	#print(macroplace)
			#break
	#testfile.close()
	#outfile.close()

def macroju():
	#for i in range(0,len(outputfile)):
	#   if type(outputfile) is list:
	#       print(outputfile[i])
	pass

def search(lexem, dic): #looking for lexem type in dictionary
	if lexem in dic:
		return 1
	return 0

def lextype(lexem): #returns lexem type
	if lexem == '':
		return -1

	for key in dictionary:
		if search(lexem, key):
			return dictionary[key]

	if lexem[0]=='"' and lexem[len(lexem)-1]=='"':
		return 'string_const'

	if lexem[len(lexem)-1] == 'h':
		return 'hex_const'

	if lexem[0].isalpha() and lexem[0] in list(string.ascii_lowercase):
		return 'identifier'

	for i in range(0, len(lexem)):
		if lexem[i] in dec:
			return 'decimal'



def sentence_struct(testfile, outfile):

	number = 0
	outfile = open(outfile, "w")
	fucklist = []
	with open(testfile) as test:
		outfile.write('%s'%'mark')
		outfile.write('\t%s'%'mnemcode')
		outfile.write('\t%s'%'lexems in field')
		outfile.write('\t\t%s'%'operand1')
		outfile.write('\t%s'%'lexems in operand1')
		outfile.write('\t%s'%'operand2')
		outfile.write('\t%s'%'lexems in operand2')
		outfile.write('\n')

		for line in test:
			i=0
			mark = 0
			mnemcode = 0
			lexinfil = 0
			op1 = 0
			lexinop1 = 0
			op2 = 0
			lexinop2 = 0
			lexc = 0
			nextl = 0
			if line=='' or line=='\n':
				continue
			line = line.split(';',1)[0] #remove comments
			line = line.lower() #read lines in lowercase


			while i < len(line):
				if line[i] in char:
					"""separate lexems"""
					symbol = line[i]
					line = line.split(symbol,1)
					line=line[0]+' '+symbol+' '+line[1]
					i+=3
				else:
					i+=1

			lexem = ''

			line = line.split()
			for item in line:
				if any('"' in item for item in line) :
					count = 0
					for i in range(len(line)):
						if line[i].startswith('"') and i+1!=len(line):
							for j in range(i+1, len(line)):
								line[i] += ' ' + line[j]
								count +=1
					line = line[:len(line)-count]
			for j in range(0,len(line)):
				lexem = line[j]
				typel = lextype(line[j])
				for i in range(0, len(macro_list)):
					if macro_list[i] == lexem:
						typel = 'instruction'
						#print('KEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEK')
				#print(lexem, typel)
				if typel == 'identifier' and nextl == 0:
					lexc+=1
					mark = 1
					lexem = ''
					nextl = 'symbol'
					continue
				if typel == 'symbol' and nextl == 'symbol':
					break

				if typel == 'instruction' or typel == 'directive':
					lexinfil = 1
					lexc+=1
					mnemcode = lexc
					lexem = ''
					nextl = 'kekw'
					continue
				if typel != 'instruction' and typel != 'directive' and nextl =='kekw':
					lexc+=1
					op1 = lexc
					lexinop1=1
					nextl = 'notIorD' #not onstrucion or directive
					continue
				if lexem != ',' and nextl == 'notIorD':
					lexc+=1
					lexinop1+=1
					continue
				if lexem == ',':
					lexc+=1
					nextl = 'notIorDafterC'
					continue
				if op1!=0 and typel!= 'instruction' and typel != 'directive' and nextl == 'notIorDafterC':
					lexc+=1
					op2 = lexc
					lexinop2 = 1
					nextl = 'longer2'
					continue
				if op1!=0 and nextl == 'longer2':
					lexc+=1
					lexinop2+=1
					continue

			#print(mark,mnemcode,lexinfil,op1,lexinop1,op2,lexinop2)
			struct = Structure()
			struct.m = mark
			struct.mn = mnemcode
			struct.lenmn = lexinfil
			struct.op1 = op1
			struct.lenop1 = lexinop1
			struct.op2 = op2
			struct.lenop2 = lexinop2
			#new_list2 = 'm:{} mn:{} lenmn:{} o1:{} o1len:{} o2:{} o2len:{}'.format(mark,mnemcode,lexinfil,op1,lexinop1,op2,lexinop2)
			fucklist.append(struct)

			outfile.write('%s'%mark)
			outfile.write('\t%s'%mnemcode)
			outfile.write('\t\t%s'%lexinfil)
			outfile.write('\t\t\t%s'%op1)
			outfile.write('\t\t%s'%lexinop1)
			outfile.write('\t\t\t%s'%op2)
			outfile.write('\t\t%s'%lexinop2)
			outfile.write('\n')
			#print(line)
	cunt = 0
	checked = 0
	#for i in range(0, len(outputfile)):

	for i in range(0, len(outputfile)):
		if outputfile[i] == '':
			outputfile[i] = fucklist[checked]
			checked+=1

	"""
	for i in range(0, len(fucklist)):
		print(fucklist[i].m)
		print(fucklist[i].mn)
		print(fucklist[i].lenmn)
		print(fucklist[i].op1)
		print(fucklist[i].lenop1)
		print(fucklist[i].op2)
		print(fucklist[i].lenop2)
		print('\n')
	"""
	outfile.close()
	#print(outputfile)
	#print(fucklist)
	#print(nth)

def delete_macro(testfile, newfile):
	file1 = open(testfile, "r")
	file2 = open(newfile, "w")
	flag = 0

	rem = []
	for line in file1:
		if 'macro' in line:
			flag = 1
			rem.append(line)
		if flag == 1:
			rem.append(line)
			if 'endm' in line:
				flag = 0
		#if line not in rem:
			#file2.write(line)

	a = 0
	for i in range(0, len(rem)):
		try:
			if 'macro' in rem[i] and len(rem[i].split(' ')) == 2:
				a=1
				continue

			if rem[i+1] == 'endm\n':
				del rem[i]
			else:
				a=0
		except IndexError:
			break

	print(rem)
	#for i in range(len(rem)):
	#	if 'mac1' in rem[i]:
	#		print("KEKE", rem[i])

	file1.seek(0)
	flag2 = 0
	save = []
	for line in file1:
		#print(line[:-1])
		for x in dreamlist:
			for y in x.macrocommand:
				if y[0] in line:
					save.append(line)

		#print(line)
		if line in save:
			continue
		if 'data'in line:
			flag = 1
		if flag == 1:
			file2.write(line)
			if 'ends' in line:
				flag = 0
		if 'code' in line:
			flag2 = 1
		if flag2 == 1:
			file2.write(line)
			if 'end' in line:
				flag2 = 0
	#print(save)
def firstie(asm, lexer, lst):
	delete_macro(asm, 'newasm.asm')
	lexanal('newasm.asm', 'newlex.txt')
	test = open('newasm.asm', "r")
	lex = open('newlex.txt', "r")
	out = open(lst, "w")
	out2 = open('MyLst.txt',"w")
	first = open(asm, "r")
	identifier_list = []
	data_list = []
	flag = 0

	macrolines = []

	for line in lex:
		line = line.split()
		if line[1] == 'data':
			flag = 2
			continue
		if flag == 2 and line[3] == 'identifier' and line[0] == '1':
			data_list.append(line[1])
		if line[1] == 'code':
			flag = 1
			continue
		if flag == 1 and line[3] == 'identifier' and line[0] == '1':
			identifier_list.append(line[1])
			continue
		if line[1] == 'ends':
			flag = 0
			continue
		continue

	"""
	for x in dreamlist:
		for y in x.macrocommand:
			if y[0] in identifier_list:
				identifier_list.remove(y[0])
	"""
	#print(identifier_list, data_list)

	lex.seek(0)
	count = 0
	secondline = ''
	test_test = ''
	flag = 0
	identifier_all = []
	lineNum = 0

	france = 0
	for line in lex:
		line = line.split()
		#print(line)
		if line[0] == '1':
			firstline = first.readline()
			secondline = test.readline()
			#firstline = first.readline()
			#print(secondline,'\n\n')
			while (secondline != firstline):
				out.write(firstline)
				firstline = first.readline()
				lineNum+=1
			out.write('%04X'%count)
			out.write('\t%s'%secondline)
			out2.write('%04X'%count)
			out2.write('\t%s'%secondline)




			lineNum+=1
			lab=0
			directive = 0
			command = ''
			register1 = 0
			register2 = 0
			register = 0
			p = 0
			op2 = 0
			macro = 0
			errr = 0
			er = 0
			mem = 0
			seg = 0
			dec1 = 0
			dec2 = 0
			dec4 = 0
		if line[3] == 'identifier' and line[0] == '1':
			lab = 1
			if line[1]=='code':
				flag = 1
				continue
			if flag == 1 and line[0] == '1' and line[3] == 'identifier':
				identifier_all.append(line[1])
				continue
			if line[1] == 'ends':
				flag = 0
				continue
			continue
		#print(identifier_list, identifier_all)
		"""
		for x in dreamlist:
			for y in x.macrocommand:
				if y[0] in identifiers:
					identifiers.remove(y[0])
		#print(identifiers)
		"""
		#print(identifier_list,identifiers)
		tmp=''
		#testline = test.readline()

		"""
		for x in dreamlist:
			for y in x.macrocommand:
				#for z in y:
				#print(y)
				#print(testline)
				if y[0] in testline:
					#print(testline)
					#macrolines.append(lineNum)
					continue
			for z in x.inside:
				if len(z) == 2 and z[0] in testline and z[1] in testline:
					#print(testline)
					macrolines.append(lineNum)
					continue
		"""
			#tmp = asm.readline()
		#print(macrolines)
		"""
		for x in dreamlist:
			for y in x.macrocommand:
				#ass
				#print(y[0])
				breakpoint()
				if line[1] == y[0]:
					print('kek', lineNum)
		"""
					#out.write('----\n')
		#print(line[1])
		if lab==1:
			if line[3] == 'directive':
				directive = 1
				if line[1] == 'db':
					inc = 1
					continue
				if line[1] == 'dw':
					inc = 2
					continue
				if line[1] == 'dd':
					inc = 4
					continue

				if line[1] == 'segment' or line[1] == 'ends':
					count = 0
					continue

		if lab==1 and directive==1:
			if line[3]=='hex_const':
				count+=inc
				continue
			if line[3] == 'string_const':
				count+=inc*int(line[2],10)
				continue
		if line[3] == 'instruction' and line[0] == '1':
			if line[1] == 'std':
				count+=1
				continue
			if line[1] == 'pop':
				command = 'pop'
				continue
			if line[1] == 'inc':
				command = 'inc'
				continue
			if line[1] == 'add':
				command = 'add'
				continue
			if line[1] == 'or':
				command = 'or'
				continue
			if line[1] == 'and':
				command = 'and'
				continue
			if line[1] == 'mov':
				command = 'mov'
				continue
			if line[1] == 'cmp':
				command = 'cmp'
				continue
			if line[1] == 'jnz':
				command = 'jnz'
				continue

		if line[3] == 'instruction' and line[0] != '1':
			print('\n Instruction wrong place %d'%lineNum)

		if command == 'pop':
			if line[3] == 'register32':
				count+=1
				continue

			if er != 1:
				print('\nBad registers at %d'%lineNum)
				er = 1
			continue

		if command == 'inc':
			if line[1] in data_list:
				count+=6
				continue
			if line[3] == 'segment_register':
				if line[1] == 'ds':
					count-=1
				seg+=1
				continue
			if line[1] == 'byte' or line[1] == 'dword' or line[1] == 'ptr':
				continue
			if line[1]==':' and seg==1:
				seg+=1
				continue
			if line[1] == '[':
				mem+=1
				continue
			if line[3] == 'register32' and mem==1:
				mem+=1
				continue
			if line[1] == '*' and mem == 2:
				mem+=1
				continue
			if line[3] == 'decimal' and mem == 3:
				if line[1] == '1':
					dec2=0
				if line[1] == '2' or line[1] == '4':
					dec2=5
				mem+=1
				continue
			if line[1] == ']' and mem == 4:
				mem +=1
			if mem == 5:
				if seg ==2:
					count+=3+dec2
					#print(count)
					continue
				if seg==0:
					count+=2+dec2
					#print(count)
					continue
				print('\nError addressing %d'%lineNum)
				continue
			if er !=1:
				print('\nError addressing %d'%lineNum)
				er = 1
			continue

		if command=='add':
			if line[0]=='2' and line[3]=='register32':
				register1=32
				continue
			if line[0]=='2' and line[3]=='register8':
				register1=8
				continue
			if line[0]=='3' and line[1]==',':
				continue
			if line[0]=='4' and line[3]=='register32':
				register2=32
				if register1==register2:
					count+=2
					register1=0
					register2=0
					#print(count)
					continue
				print('\nERROR: Expected (add reg, reg) (%d)'%count_str)
				continue
			if line[0]=='4' and line[3]=='register8':
				register2=8
				if register1==register2:
					count+=2
					register1=0
					register2=0
					#print(count)
					continue
				print('\nERROR: Expected (add reg, reg) (%d)'%lineNum)
				continue
			if er!=1:
				print('\nERROR: Expected (add reg, reg) (%d)'%lineNum)
				er=1
			continue

		if command=='or':
			if line[3] == 'segment_register':
				if line[1] == 'ds':
					count-=1
				seg+=1
				continue
			if line[1] == ':' and seg == 1:
				seg+=1
				continue
			if line[1] == 'byte' or line[1] == 'dword' or line[1] == 'ptr':
				continue
			if line[1] in data_list:
				count+=6
				continue

			if (line[3] == 'register32' or line[3] == 'register8') and mem == 0:
				mem+=1
				#print('im here', mem, count, lineNum)
				continue
			if line[1] == ',' and mem == 1:
				mem+=1
				continue
			if line[1] == '[' and mem == 2:
				mem+=1
				continue
			if line[3] == 'register32' and mem == 3:
				mem+=1
				#print('im here',lineNum)
				continue
			if line[1] == '*' and mem == 4:
				mem+=1
				continue
			if line[3] == 'decimal' and mem == 5:
				if line[1] == '1':
					dec2=0
				if line[1] == '2' or line[1] == '4':
					dec2=5
				mem+=1
				continue
			if line[1] == ']' and mem == 6:
				mem+=1
			if mem == 7:
				if seg == 2:
					count+=3+dec2
					#print('im here',lineNum)
					#print(count)
					continue
				if seg == 0:
					#print('im here',lineNum)
					count+=2+dec2
					#print(count)
					continue
				print('\nExpected or reg, mem %d'%lineNum)
				continue
			if er != 1:
				print('\nExpected or reg, mem %d'%lineNum)
				out.write('Expected or reg, mem %d\n'%lineNum)
				er = 1
			continue

		if command == 'and':
			if line[3] == 'segment_register':
				if line[1] == 'ds':
					count-=1
				seg+=1
				continue
			if line[1] == ':' and seg == 1:
				seg+=1
				continue
			if line[1] == 'byte' or line[1] == 'dword' or line[1] == 'ptr':
				continue
			if line[1] in data_list:
				count+=6
				continue

			if line[1] == '[' and mem == 0:
				mem+=1
				continue
			if line[3] == 'register32' and mem == 1:
				mem+=1
				#print('im here',lineNum)
				continue
			if line[1] == '*' and mem == 2:
				mem+=1
				continue
			if line[3] == 'decimal' and mem == 3:
				if line[1] == '1':
					dec2=0
				if line[1] == '2' or line[1] == '4':
					dec2=5
				mem+=1
				continue
			if line[1] == ']' and mem == 4:
				mem+=1
				continue
			if (line[3] == 'register32' or line[3] == 'register8') and mem == 6:
				mem+=1
			if line[1] == ',' and mem == 5:
				mem+=1
				continue
			if mem == 7:
				if seg == 2:
					count+=3+dec2
					#print('im here',lineNum)
					#print(count)
					continue
				if seg == 0:
					#print('im here',lineNum)
					count+=2+dec2
					#print(count)
					continue
				print('\nExpected or reg, mem %d'%lineNum)
				continue
			if er != 1:
				print('\nExpected or reg, mem %d'%lineNum)
				er = 1
			continue

		if command=='mov':
			if line[0]=='2' and line[3]=='register32':
				register=32
				continue
			if line[0]=='2' and line[3]=='register8':
				register=8
				continue
			if line[0]=='3' and line[1]==',':
				continue
			if line[0]=='4' and (register==32 or register==8):
				if line[3]=='hex_const' or line[3]=='string_const':
					if line[3]=='hex_const':
						#b=0
						j=int(line[2],10)
						b=int(line[1][0:j-1],16)
					if register==8 and b<256:
						count+=2
						#print(count)
						continue
					if register==32:
						count+=5
						#print(count)
						continue
					print('\nERROR: Expected (mov reg, imm) (%d)'%lineNum)
					continue
				if er!=1:
					print('\nERROR: Expected (mov reg, imm) (%d)'%lineNum)
					er=1
				continue

		if command == 'cmp':
			if line[3] == 'segment_register':
				if line[1] == 'ds':
					count-=1
				seg+=1
				continue
			if line[1] == ':' and seg == 1:
				seg+=1
				continue
			if line[1] == 'byte' or line[1] == 'dword' or line[1] == 'ptr':
				continue
			if line[1] in data_list:
				count+=6
				continue

			if line[1] == '[' and mem == 0:
				mem+=1
				continue
			if line[3] == 'register32' and mem == 1:
				mem+=1
				#print('im here',lineNum)
				continue
			if line[1] == '*' and mem == 2:
				mem+=1
				continue
			if line[3] == 'decimal' and mem == 3:
				if line[1] == '1':
					dec2=0
				if line[1] == '2' or line[1] == '4':
					dec2=5
				mem+=1
				continue
			if line[1] == ']' and mem == 4:
				mem+=1
				continue
			if line[1] == ',' and mem == 5:
				mem+=1
				continue
			if (line[3] == 'hex_const' or line[3] == 'string_const') and mem == 6:
				if line[3] == 'hex_const':
					j=int(line[2],10)
					b=int(line[1][0:j-1],16)
				if line[3] == 'string_const':
					count += int(line[2],10)-1
				if seg == 2:
					if b<=255:
						count+=4+dec2
						#print(count, lineNum)
						continue
					else:
						#print(count,lineNum)
						count+=7+dec2
						continue
					print('\nERROR: Expected (cmp mem, imm)(%d)'%lineNum)
					continue
				if seg == 0:
					if b<=255:
						count+=3+dec2
						#print(count,lineNum)
						continue
					else:
						count+=6+dec2
						#print(count,lineNum)
						continue
					print('\nERROR: Expected (cmp mem, imm)(%d)'%lineNum)
					continue
				print('\nERROR: Expected (cmp mem, imm)(%d)'%lineNum)
				continue
			if er!=1:
				print('\nERROR: Expected (cmp mem, imm)(%d)'%lineNum)
				er = 1
			continue
		if command == 'jnz':
			if line[1] in identifier_all:
				count+=2
				#print(count,lineNum)
				continue
			if line[1] in identifier_list:
				#print(count,lineNum)
				count+=6
				continue
			print('\nIdentifier error (%d)'%lineNum)
			continue
	out2.close()
	additonalParse('MyLst.txt', 'tables.txt')
	apend = open('tables.txt', "r")
	for line in apend:
		out.write(line)


def additonalParse(lst, tables):
	lst = open(lst,"r")
	out = open(tables, "w")

	out.write('\n')
	out.write('\n')
	out.write('%5s'%'Symbol Name')
	out.write('%12s'%'Type')
	out.write('%10s'%'Value')
	out.write('\n\n')

	label = ''
	labelLength = ''
	segment = ''

	for line in lst:
		line = line.split()

		if 'segment' in line:
			segment = line[line.index('segment')-1]
		if 'ends' in line:
			segment = ''

		lexem = ''
		for item in line:
			lexem = item
			lexem2 = item
			lexem_type = lextype(lexem)

			if lexem_type == 'identifier' and line.index(lexem2) == 1 and 'segment' not in line and 'ends' not in line:
				if line[line.index(lexem2)+1] == 'db':
					lsttype = 'Byte'
				elif line[line.index(lexem2)+1] == 'dw':
					lsttype = 'Word'
				elif line[line.index(lexem2)+1] == 'dd':
					lsttype = 'Dword'
				else:
					lsttype = 'Near'

				label = lexem2
				out.write('%5s'%label)
				out.write('%12s'%lsttype)
				out.write('%10s:'%segment)
				out.write('%s'%line[0])
				out.write('\n')
				continue

	out.write('\n\n')
	out.write('Macro Name')
	out.write('\n\n')

	for x in dreamlist:
		for y in x.macrocommand:
			out.write('%s\n'%y[0])

	out.write('\n\n')
	out.write('Groups & Segments\t\tBit\t\tSize')
	out.write('\n')
	lst.seek(0)
	label = ''
	labelLength = ''
	for line in lst:
		line = line.split()

		if 'segment' in line:
			label=line[line.index('segment')-1]
		if 'ends' in line:
			labelLength = line[line.index('ends')-2]

		if label != '' and labelLength != '':
			out.write('%s\t\t\t\t'%label)
			out.write('32\t\t\t\t')
			out.write('%s'%labelLength)
			out.write('\n')
			label = ''
			labelLength = ''
			continue
