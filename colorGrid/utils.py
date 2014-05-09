import random
def random_octal_str(digits):
    n = "" 
    for i in xrange(digits):
        n += '7'

    num = random.randint(0, int(n, 8))
    octal_str = format(num, 'o')
    
    while len(octal_str) < digits:
        octal_str = '0' + octal_str

    return octal_str
