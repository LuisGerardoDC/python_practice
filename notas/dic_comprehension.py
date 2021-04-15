def dictionary_pw_2():
    dict_pw2 = {i: i**2 for i in range(1,101)}
    for key,value in dict_pw2.items():
        print(key,'-',value)

def qube_not_div_three():
    qube_not_div_three = {i: i**3 for i in range(1,101) if i%3!=0}
    for key,value in qube_not_div_three.items():
        print(key,'-',value)

def reto():
    print({i:i**.5 for i in range(1,1001)})

if __name__=='__main__':
    reto()