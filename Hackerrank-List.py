
                                                    #LIST

'''Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above.
Iterate through each command in order and perform the corresponding operation on your list.'''

n = int(input('Enter number of iterations:'))
output = []
for i in range(0,n):
    l = input().split()
    if l[0]== 'print':
        print(output)
    elif l[0] == 'insert':
        output.insert(int(l[1]), int(l[2]))
    elif l[0] == 'remove':
        output.remove(int(l[1]))
    elif l[0] == 'append':
        output.append(int(l[1]))
    elif l[0] == 'sort':
        output.sort()
    elif l[0] == 'pop':
        output.pop()
    else:
        output.reverse()

