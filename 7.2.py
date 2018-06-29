def count_2sub_match(a, b):
    tmp = []
    licznik = 0
    for i in range(0, len(b)-1):
        partB = b[i:i+2]
        if partB not in tmp:
            for j in range(0, len(a)-1):
                if a[j:j+2] == partB:
                    licznik += 1
        tmp.append(b[i:i + 2])
    return licznik

print(count_2sub_match('abcdz', 'ababdz'))