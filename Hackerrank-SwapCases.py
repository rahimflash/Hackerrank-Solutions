
'''You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.'''



def swapCases(name):
    r = ''
    for c in name:
        if c.isupper():
            r += c.lower()
        else:
            r += c.upper()
    return ''.join(r)
if __name__ == '__main__':
    name = input()
    result = swapCases(name)
    print(result)

                                           # '''-----OR-----'''
def swap_case(s):
    Output = '';
    for char in s:
        if(char.isupper()==True):
            Output += (char.lower());
        elif(char.islower()==True):
            Output += (char.upper());
        else:
            Output += char;
    return Output;

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

                                       # '''-----OR-----'''

def swap_case(s):
    output = ''
    s = input()
    for i in s:
        if i.isupper() == True:
             output += i.lower()
        else:
            output += i.upper()
    return output
result = swap_case(s)
print(result)

                                                #'''-------OR-----------------'''

def swap_case(s):
    output = ''
    for i in s:
        if i.isupper() == True:
            output += i.swapcase()
        else:
            output += i.swapcase()

    return output

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)