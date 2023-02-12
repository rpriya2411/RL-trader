def match2(string, pattern):
    if not pattern:
        return  not string
    i, j = 0, 0
    while i < len(string) and j < len(pattern):
        # print(string[i], pattern[j])
        if j+1 < len(pattern) and pattern[j+1] == '+':
            # match string[i] with pattern[j]
            while (i<len(string)) and (string[i] == pattern[j] or pattern[j]=='.'):
                if (j+2) < len(pattern) and pattern[j+2] == string[i]:
                    break
                i += 1
                
            j += 2
        elif string[i] == pattern[j] or pattern[j] == '.':
            i += 1
            j += 1
        else:
            break    
    
    if i == len(string) and j == len(pattern):
        return True
    else:
        return False

print(match2('BAAAAAC', 'BA+C'))
print(match2('BAAAAAC', 'BA+D'))
print(match2('BAAAAAC', 'BA+'))
print(match2('BAAAAAC', '.A+.'))
print(match2('BAAAAAC', '.+C'))   
print(match2('BAAAAACDB', '.+C.+'))      