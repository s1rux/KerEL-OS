[org 0x7C00]      ; Tell the assembler that the code will be loaded at address 0x7C00 (standard bootloader location)

start:
    xor ax, ax    ; Clear AX register
    mov ds, ax    ; Set Data Segment (DS) to 0
    mov es, ax    ; Set Extra Segment (ES) to 0

    mov si, msg   ; Load the address of the message into SI
    call print_string  ; Call the print_string function

    hlt           ; Halt the CPU (stop execution)

print_string:
    mov ah, 0x0E  ; BIOS teletype function (print character)
.print_char:
    lodsb         ; Load the next byte from SI into AL and increment SI
    cmp al, 0     ; Check if the byte is 0 (end of string)
    je .done      ; If it is, we're done
    int 0x10      ; Otherwise, print the character using BIOS interrupt
    jmp .print_char ; Repeat for the next character
.done:
    ret           ; Return from the function    

times 510-($-$$) db 0  ; Fill the rest of the boot sector with zeros
dw 0xAA55              ; Boot signature (0xAA55 at the end of the 512-byte sector)
