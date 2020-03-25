# a=input()
a = '5/8/5*5/5'
postexp = ''
a = list(a)
for i in range(len(a)-1):
    if a[i] == '*' or a[i] == '/':
        if (i == 0 or i == 1):
            postexp = str(a[i-1] + a[i+1]+a[i])
        else:
            postexp = str(postexp+a[i+1]+a[i])

print(postexp)
