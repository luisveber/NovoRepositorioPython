def disemvowel(string_):
    str = 'aeiouAEIOU'
    for x in range(len(str)):
        string_ = string_.replace(str[x],"")
    print(string_)
    

disemvowel('luis HENRIQUE VebER')