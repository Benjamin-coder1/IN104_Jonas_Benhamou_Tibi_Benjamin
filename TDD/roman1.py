"""Convert to and from Roman numerals

This program is part of "Dive Into Python", a free Python book for
experienced programmers.  Visit http://diveintopython.org/ for the
latest version.
"""

__author__ = "Mark Pilgrim (mark@diveintopython.org)"
__version__ = "$Revision: 1.2 $"
__date__ = "$Date: 2004/05/05 21:57:20 $"
__copyright__ = "Copyright (c) 2001 Mark Pilgrim"
__license__ = "Python"

#Define exceptions
class RomanError(Exception): pass
class OutOfRangeError(RomanError): pass
class NotIntegerError(RomanError): pass
class InvalidRomanNumeralError(RomanError): pass


def toRoman(n): 
    """convert integer to Roman numeral"""
    table = {1000:'M' ,900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
    if type(n)!=int:
        raise NotIntegerError
    if n<=0 :
        raise OutOfRangeError
    if n>3999:
        raise OutOfRangeError
    s=''
    for elt in table:
        while (n-elt)>=0:
            n-=elt
            s+=table[elt]

    return s
    pass


def fromRoman(s):
    """convert Roman numeral to integer"""
    dico2 = {'I':1, 'V':5 , 'X':10, 'L':50, 'C':100, 'D':500 , 'M':1000 }

    for letter in s : 
        if letter not in dico2 :
            raise InvalidRomanNumeralError
    for repeat in ['MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII','CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV','IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                  'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'] : 
        if repeat in s : 
            raise InvalidRomanNumeralError

  
    else : 
        compteur = len(s)-1 
        somme = 0
        while compteur >= 0 :
            if compteur != 0 and dico2[s[compteur - 1]] < dico2[s[compteur]] :
                if (dico2[s[compteur]] - dico2[s[ compteur- 1]])  in [4,40,400,9,90,900] : 
                    somme += -dico2[s[ compteur- 1]] + dico2[s[compteur]]
                    compteur -=  2
                else : 
                    raise InvalidRomanNumeralError
            elif compteur != 0 and dico2[s[compteur - 1]] >= dico2[s[compteur]] : 
                somme += dico2[s[compteur]]
                compteur -=  1

            elif compteur == 0: 
                somme += dico2[s[0]]
                compteur -=1
        if (toRoman(somme) in dico2 and len(s) != 1) : 
            raise InvalidRomanNumeralError
        if somme >= 4000 : 
            raise InvalidRomanNumeralError
        else : 
            return somme













    
