def maior(*numeros):
    maior_num = 0
    for num in numeros:
        if num == 0:
            num = maior_num
        if num > maior_num:
            num = maior_num
    print(maior_num)




maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)