def datatypes():
    int_o = 21  #int
    string_o = "hello"   #str, 
    float_o = 3.14  #float 
    bool_o = True   #bool
    list_o = [1, 21, 42]    #list
    dicto_o = {"a": 1}    #dict
    tuple_o = (2, "sus")    #tuple
    set_o = {1, 2, 3}   #set

    result = [type(x).__name__ for x in [int_o, string_o, float_o, bool_o, list_o, dicto_o, tuple_o, set_o]]
    print(result)

if __name__ == '__main__':
    datatypes()