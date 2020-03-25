
for i in range(len(li)):
    if a[i] == '*':
        final.append(a[i-1])
        final.append(a[i+1])
        final.append(a[i])

print(''.join(final))