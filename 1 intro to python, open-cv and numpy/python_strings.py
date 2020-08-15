x = ['abc', '1121', 'mnnm', 'aba']
stringCount = 0
for s in x:
    if len(s) > 2:
        if s[0] == s[len(s)-1]:
            stringCount = stringCount +1

print('String count is ', stringCount)
