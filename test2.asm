.486
MAC1 MACRO
	Std
ENDM

MAC2 MACRO A
	Pop A
ENDM

DATAA SEGMENT USE32 ;WORD PUBLIC 'DATA'
	ASSUME  DS:DATAA
	AUTHOR DB "SP Course Work var20 Sukhoveyko Olexiy FPM KB-94 2021-02-26"
	ImmBA DB 0bah
	ImmBB DB 02h
	ImmBC DB 2h
	ImmDA DD 2fh
	ImmDB DD 1h
	ImmDC DD 0fh
	ImmSA DB "qwerty"
DATAA ENDS

CODE SEGMENT USE32 ;WORD PUBLIC 'CODE'
	ASSUME  CS:CODE, DS:DATAA
	Jnz EXIT
	START:

	MAC1
	MAC2 ecx

	Inc ImmBA
	Inc byte ptr gs:[esi*4]
	Inc word ptr gs:[esi*4]
	Inc word ptr [esi*4]
	Inc byte ptr ss:[eax*2]

	Add ah, al
	Add ebx, ecx

	Or dl, ImmBA
	Or dl, [edx*2]

	And ds:[edx*2], ecx
	And [esi*2], al

	mov eax, 'kek' 
	Mov ecx, ds:[ecx*4]
	Mov al, ss:[ebx*1]

	Cmp al, 0ddh
	Cmp ecx, 5555h

	Jnz START
	EXIT:
	;MOV AX,4c00h
	;INT 21h
CODE ENDS
END
