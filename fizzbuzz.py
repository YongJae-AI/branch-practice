for j  in range(1+15+1):
    if j % 3 == 0:
        print('fizz')
    elif j % 5 ==0:
        print('buzz')
    elif j % 15 == 0:
        print('fizzbuzz')
    else:
        print(j)
