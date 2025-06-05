;nasm -f elf64 fibonacci.s && ld fibonacci.o -o fibonacci -lc --dynamic-linker /lib64/ld-linux-x86-64.so.2

global _start
extern printf, scanf

section .bss
	userInput resb 1; reserve buffer (1 byte)

section .data
	message db "Input max Fn", 0x0a
	outFormat db "%lld", 0x0a, 0x00;printf format, newline, null term
	inFormat db "%d", 0x00;scanf format null term

section .text
_start:
	call printMessage
	call getInput
	call initFib
	call loopFib
	call Exit

getInput:
	mov rdi, inFormat
	mov rsi, userInput
	sub rsp, 8 ;stack alignment (push/pop also viable)
	call scanf
	add rsp, 8
	ret

printMessage:
	mov rax, 1;syscall no. 1
	mov rdi, 1;fd 1 for stdout
	mov rsi, message
	mov rdx, 13;byte length to print
	syscall ;execute
	ret

printFib:
	push rax;save regs
	push rbx

	mov rdi, outFormat ;set 1st arg (print format)
	mov rsi, rbx 	   ;set 2nd arg (Fib Num)
	call printf	; printf(outFormat, rbx)

	pop rbx;restore regs
	pop rax
	ret

initFib:
	xor rax, rax;zero working registers and start at 0x1
	xor rbx, rbx
	inc rbx
	ret

loopFib:
	call printFib
	add rax, rbx
	xchg rax, rbx
	cmp rbx, [userInput];set rbx to upper limit of fib num
	js loopFib
	ret

Exit:
	mov rax, 60;exit
	mov rdi, 0
	syscall
