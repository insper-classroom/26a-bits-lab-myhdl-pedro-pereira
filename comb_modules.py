# -*- coding: utf-8 -*-
"""Exercice 1

Implemente a equacão:

q = a or !b
"""


from myhdl import *


@block
def exe1(q, a, b):
    """
    q = a or !b
    """

    @always_comb
    def comb():
        q.next = a or not b

    return instances()


@block
def exe2(q, a, b, c):
    """
    Implemente a tabela verdade a seguir:

    A B C | Q
    ------|--
    0 0 0 | 1
    0 0 1 | 0
    0 1 0 | 0
    0 1 1 | 1
    1 0 0 | 1
    1 0 1 | 0
    1 1 0 | 0
    1 1 1 | 1

    Não utilize IF!
    """

    @always_comb
    def comb():
        q.next = a or b

    return instances()


@block
def exe3(q, a, b, c, d, e):
    """
    Exercice 3

    Implemente o circuito lógico a seguir:

               __
    a---------\  \
              |   )-  __
    b---------/__/  -|  \
                     |   )-
    c----------------|__/  -  __
                            -|  \
                             |   )-
    d------------------------|__/  -  __
                                    -|  \
                                     |   )-----
    e--------------------------------|__/
    """

    @always_comb
    def comb():
        q.next = a

    return instances()


@block
def exe4(led, sw):
    """
    led0 é sw[0] and (não sw[1])
    """

    @always_comb
    def comb():
        led[0].next = sw[0] and (not sw[1])

    return instances()


@block
def exe5(leds, sw):
    """
    led0 é uma copia da chave sw0
    led1 é sw0 & sw1
    led2 é o led1 invertido
    led3 é xor entre sw0 e sw1
    todos os outros leds acesos
    """

    @always_comb
    def comb():
        pass

    return instances()


@block
def sw2hex(hex_pins, sw):
    """
    Faz a conversão de binário para display de 7 segmentos
    """

    @always_comb
    def comb():
        if sw[4:0] == 0:
            hex_pins.next = "1000000"
        elif sw[4:0] == 1:
            hex_pins.next = "1111001"
        elif sw[4:0] == 2:
            hex_pins.next = "1000000"
        elif sw[4:0] == 3:
            hex_pins.next = "1000000"
        elif sw[4:0] == 4:
            hex_pins.next = "1000000"
        elif sw[4:0] == 5:
            hex_pins.next = "1000000"
        elif sw[4:0] == 6:
            hex_pins.next = "1000000"
        elif sw[4:0] == 7:
            hex_pins.next = "1000000"
        elif sw[4:0] == 8:
            hex_pins.next = "1000000"
        elif sw[4:0] == 9:
            hex_pins.next = "1000000"
        elif sw[4:0] == 10:
            hex_pins.next = "1000000"
        elif sw[4:0] == 11:
            hex_pins.next = "1000000"
        elif sw[4:0] == 12:
            hex_pins.next = "1000000"
        elif sw[4:0] == 13:
            hex_pins.next = "1000000"
        elif sw[4:0] == 14:
            hex_pins.next = "1000000"
        else:
            hex_pins.next = "1000000"

    return instances()
