mac1 macro
std
endm
mac2 macro a
pop a
endm
data segment
author db "sukhoveyko_oleksiy_variant_20"
immba db 0bah
immbb db 02h
immbc db 2h
immda dd 2fh
immdb dd 1h
immdc dd 0fh
immsa db "qwerty"
data ends
code segment
jnz exit
start :
mac1
std
mac2 ecx
pop ecx
inc immba
inc byte ptr gs : [ esi * 4 ]
inc dword ptr gs : [ esi * 4 ]
inc dword ptr [ esi * 4 ]
inc byte ptr ss : [ eax * 2 ]
add ah , al
add ebx , ecx
or dl , immba
or dl , [ edx * 2 ]
and ds : [ edx * 2 ] , ecx
and [ esi * 2 ] , al
mov ecx , 0ddh
mov al , 1h
cmp dword ptr [ ecx * 4 ] , 5555h
cmp byte ptr [ ebx * 1 ] , 0ddh
jnz start
exit :
code ends
end
