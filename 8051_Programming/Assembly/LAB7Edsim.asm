
org 40h
str: db "Welcome to 8051 Programming"
db 0

Start:

	mov R0, #str
	mov A, @R0
Main:
	inc R0
	mov B, #16
	
	div AB
	
	cjne R0, #0, FirstCheck
	jmp exit
FirstCheck:
	cjne A, #4, NextCheck
	jmp Main

NextCheck:
	cjne A, #5, Found
	jmp Main
Found:
	
	subb A, #20
	mov @R0, A
	jmp Main

exit:

END
