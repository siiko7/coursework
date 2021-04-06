reg32=('eax','ebx','edx','ecx','esi','ebp','esp','edi')                                                  #32-ох розрядні регістри
reg8=('ah','al','bh','bl','dh','dl','ch','cl')                                                           #8-ми розрядні регістри
segm_reg=('cs','ds','es','fs','gs','ss')                                                                     #сегментні регістри
instruction=('std','pop','inc','add','or','and','mov','cmp','jnz')                                                #команди
directive=('segment','macro','ends','end','db','dw','dd','endm')                                     #директиви
typeop=('ptr',)                                                                                           #тип оператора
hexad=('a','b','c','d','e','f','h')                                                                         #16-теричні числа
char=('+','*',':','[',']',',')                                                                          #односимвольні лексеми
types=('byte','dword')
dec=('0','1','2','3','4','5','6','7','8','9')  

dictionary={reg32:'register32', reg8:'register8', segm_reg:'segment_register',       #словник що зберігає в собі вищеописані кортежі
        instruction:'instruction', directive:'directive', typeop:'operator_ident_type_def',
        char:'symbol', types:'type'} 
