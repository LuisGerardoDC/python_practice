def pow_2_numbers():
    numbers=[(i+1)**2 for i in range(100) ]
    print(numbers)

def list_no_div_three():
    numbers=[i**2 for i in range (1,101) if (i%3 != 0)]
    print(numbers)

def mult_four_six_nine():
    print([
        i for i in range(1,10000)
        if (i%4==0 and i%6==0 and i%9==0)
    ])

if __name__ == '__main__':
    mult_four_six_nine()