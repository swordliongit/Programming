org 0000h
jmp Start

org 100h
string : db "Welcome to 8051 Programming"
db 0

len equ 30h
strCap equ 40h

Start:
	mov DPTR, #string
	mov R0, #strCap

ReadROMintoRAM:
	clr A
	movc A, @A+DPTR
	jz EndReadStr
	mov @R0, A
	inc len
	inc R0
	inc DPTR
	jmp ReadROMintoRAM

EndReadStr:
	mov R0, #strCap

ReverseStr: ; < a && > z
	mov A, @R0
	jz exit
	cjne A, #97, CmpLess
CmpLess:
	jc NoChange
	cjne A, #123, CmpGreater
CmpGreater:
	jnc NoChange
	
	clr C
	subb A, #32
	mov @R0, A
NoChange:
	inc R0
	jmp ReverseStr

exit:

END
