def run():
    my_list = [1, "helo", True, 4.5]
    my_dict = {'firstname':'Luis','lastname':'Hernandez'}

    super_list=[
        {'firstname':'Luis','lastname':'Hernandez'},
        {'firstname':'gerardo','lastname':'pintor'},
        {'firstname':'Valentin','lastname':'Reyes'},
        {'firstname':'Mario','lastname':'pintor'}
    ]
    super_dic = {
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-2, -1, 0, 1, 2],
        "floating_nums":[1.5, 2.5, 3.7]
    }

    for key, value in super_dic.items():
        print(key,'-',value)

    print('\nsuper lista\n')
    for element in super_list:
        print(element.items())
        #for key, value in element.items():
        #    print(key,'-',value)



if __name__ == '__main__':
   run()