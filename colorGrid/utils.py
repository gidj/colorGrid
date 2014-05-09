import random

def random_octal_str(digits):
    """ Takes a number of digits and generates a random octal number and
    returns it as a string. If the generated number has fewer than the given
    number of digits, it is padded with zeros at the front """

    n = "" 
    for i in xrange(digits):
        n += '7'

    num = random.randint(0, int(n, 8))
    octal_str = format(num, 'o')
    
    while len(octal_str) < digits:
        octal_str = '0' + octal_str

    return octal_str
