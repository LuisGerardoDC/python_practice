def divisors(num):
    divisors = []
    for i in range(1,num + 1):
        if num % i  == 0:
            divisors.append(i)
    return divisors

def divisors_comprehension(num):
    return[ i for i in range(1, num + 1) if num%i == 0]

def run():
    num= int(input('Ingresa un numero: '))
    
    print(divisors(num))
    print(divisors_comprehension(num))

    print('termino el programa')

if __name__=='__main__':
    run()