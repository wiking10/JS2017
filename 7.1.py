def substr_conc(str):
    k = 1
    result = ""
    while k <= len(str):
        result += str[:k]
        k += 1
    return result

print(substr_conc("Test"))