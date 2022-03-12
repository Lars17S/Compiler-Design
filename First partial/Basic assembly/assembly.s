# asignación
.text 
.globl main 
main: 
        lw $t0, $v0     # load $v0 value into $t0 register
        sw $v0, $t0     # store $v0 value into $t0 register
------------------------
# declaración int
.data
x: .word 80

.text  
.globl main  
main:  
    li $t0, 20  # load 20 integer (could be any integer)
    lw $t0, x   # load x value into $t0 register
    sw x, $t0   # store x value into $t0 register
------------------------
# if sin else
.text
.globl main
main:
        li $t0, 10
        li $t1, 10
        beq $t0, $t1, L1        # if (t0 == t2) {goto L1}
L1:
        # code
        j exit
------------------------
# if con else
.text
.globl main
main:
        li $t0, 10
        li $t1, 10
        beq $t0, $t1, L1        # if (t0 == t2) {goto L1}
        j L2                    # else {goto L2}
L1:
        # code
        j exit
L2:
        # code
        j exit
------------------------
# while
.text
.globl main
main:
        li $t0, 10 # load 10 integer into $t0
loop:
        blt $t0, $zero, exit    # if ($t0 < 0) goto exit
        addi $t0, $t0, -1       # substract 1 to $t0
        j loop                  # loop
------------------------
# do while
.text
.globl main
main:
        li $t0, 10      # load 10 integer into $t0
loop:
        addi $t0, $t0, -1       # substract 1 to $t0
        blt $t0, $zero, exit    # if ($t0 < 0) goto exit
        j loop                  # loop
------------------------
# aritmética
.text
.globl main
main:
        li $t0, 10              # load 10 integer into $t0
        li $t1, 10              # load 10 integer into $t1
        add $t2, $t0, $t1       # sum $t0 + $t1 and save into $t2
------------------------
# comparación
.text
.globl main
main:
        li $t0, 10              # load 10 integer into $t0
        li $t1, 20              # load 10 integer into $t1
        bgt $t1, $t0, exit      # if ($t1 > $t0) then goto EXIT