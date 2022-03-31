import re
import email.utils


n = int(input())
for i in range(n):
    x,y = input().split()
    m = re.match(r'<[a-z0-9](\w|-|\.|_)+@[a-z]+\.[a-z]{1,3}>',y)
    if bool(m):
        print(x,y)

'''OR'''

n = int(input())
for i in range(n):
    p = email.utils.parseaddr(input())
    if re.match(r'[a-z][\w.-]+@[a-z]+\.[a-z]{1,3}$', p[1], re.I):
        print(email.utils.formataddr(p))


n = int(input())
for i in range(n):
    x,y = input().split()
    if re.match(r'<[a-z0-9][\w.-]+@[a-z]+\.[a-z]{1,3}>', y):
        print(x, y)
