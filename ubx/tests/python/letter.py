rows = 5
for i in range(1, rows+1):
    # since ascii of A is 65
    for j in range(65, 65+i):
        a = chr(j)  # chr(65) -> A
        print(a, end=' ')
    print()
