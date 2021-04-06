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
			new_list2 = 'm:{} mn:{} lenmn:{} o1:{} o1len:{} o2:{} o2len:{}'.format(mark,mnemcode,lexinfil,op1,lexinop1,op2,lexinop2)
			fucklist.append(new_list2)
			
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
			
	for i in range(0, len(outputfile)):
		#print(outputfile[i])
		outfile.write(str(outputfile[i]))
		outfile.write('\n')
	"""
	outfile.close()
	#print(outputfile)
	#print(fucklist)
	#print(nth)

def first(testfile, lexems, out):
	test = open(testfile, "r")
	lex = open(lexems, "r")
	output = open(out, "r")

	usrident = []
	flag =0
	data = []

	for line in lex:
		line = line.split()
		#print(line)
		if line[1] == 'data':
			flag=2
			continue
		if flag == 2 and line[3] == 'identifier' and line[0] == '1':
			data.append(line[1])
		if line[1] == 'code':
			flag = 1
			continue
		if flag == 1 and line[3] == 'identifier' and line[0] == '1':
			usrident.append(line[1])
			continue
		if line[1] == 'ends':
			flag = 0
			continue

		continue

	lex.seek(0)
	c = 0
	testline = ''
	flag = 0
	print(usrident)
	print(data)



	

