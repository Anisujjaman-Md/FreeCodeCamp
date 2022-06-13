def sort(abc):
    for i in range(len(abc)):
        for j in range(len(abc) - 1):
            if abc[j] > abc[j + 1]:
                abc[j], abc[j + 1] = abc[j + 1], abc[j]
    return abc