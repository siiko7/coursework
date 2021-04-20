.486
MAC1 MACRO
	Std
ENDM

MAC2 MACRO A
	Pop A
ENDM

DATAA SEGMENT USE32 ;WORD PUBLIC 'DATA'
	ASSUME  DS:DATAA
	AUTHOR DB "Sukhoveyko Oleksiy Variant 20"
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
	Inc dword ptr gs:[esi*4]
	Inc dword ptr [esi*4]
	Inc byte ptr ss:[eax*2]

	Add ah, al
	Add ebx, ecx

	Or dl, ImmBA
	Or dl, [edx*2]

	And ds:[edx*2], ecx
	And [esi*2], al

	Mov ecx, 0ddh
	Mov al, 1h

	Cmp dword ptr [ecx*4],  5555h
	Cmp byte ptr [ebx*1],  0ddh

	Jnz START
	EXIT:

CODE ENDS
END
