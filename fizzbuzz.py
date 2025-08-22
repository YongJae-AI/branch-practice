for j  in range(1,15+1):
    if  j ==0:
        print(j)
    elif j % 15 == 0:
        print('fizzbuzz')
    elif j % 3 ==0:
        print('fizz')
    elif j % 5 == 0:
        print('buzz')
    else:
        print(j)
