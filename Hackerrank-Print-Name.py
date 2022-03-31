
'''You are given the firstname and lastname of a person on two different lines.
Your task is to read them and print the following:
Hello firstname lastname! You just delved into python.'''

def print_full_name(first_name,last_name):
    last_name += '!'
    output = eval('print("Hello",first_name,last_name,"You just delved into python.")')
    return output
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name,last_name)

            
'''OR'''

def full_name(a,b):
    return "Hello {} {}! You just delved into spython.".format(a, b)
a =input()
b = input()

print(full_name(a,b))

'''OR'''

def full_name(f, s):
    return 'Hello %s %s! You just delved into python.' % (f, s)
first = input()
second = input()

print(full_name(first, second))

'''OR'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
first_name = input()
last_name = input()
output = "Hello {0} {1}! You just delved into python.".format(first_name,last_name)
print(output)


