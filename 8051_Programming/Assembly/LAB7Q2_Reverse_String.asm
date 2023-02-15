org 0000h
jmp Start

org 100h
string : db "ABCDEFGHIJKLMNOP"
db 0

len equ 30h

Start:
	mov len, #0
	mov DPTR, #string
	mov R0, #40h
	mov R1, #90h
WriteROMintoRAM:
	clr A
	movc A, @A+DPTR
	jz EndReadStr
	mov @R0, A
	inc len
	inc R0
	inc DPTR
	jmp WriteROMintoRAM

EndReadStr:
	mov DPTR, #40h
ReadStringIntoStack:
	
	push DPL
	push DPH

	inc DPTR	

	mov R0, DPL
	clr A
	mov A, @R0

	jz WriteReversedStart
	jmp ReadStringIntoStack

WriteReversedStart:
	mov R0, #60h

WriteReversed:

	pop DPH
	pop DPL

	mov R1, DPL
	clr A
	mov A, @R1

	mov @R0, A

	jz exit

	inc R0

	jmp WriteReversed

exit:

END
	
