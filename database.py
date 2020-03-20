# i wan't to work by a database file .txt
import openpyxl


# function goto get input frome user and return that in string that can change to dict by eval()
def get_Specifications(locate_of_poiter):
    # get Specifications of new product and append them look like a dictonary
    print("we need some information about your pruduct")
    try_value_input = False
    while (not try_value_input):  # FOR ERROR CONTROL code VALUE ERROR
        try:
            code = int(input('please enter code: '))
            try_value_input = True
        except ValueError:
            print("please enter a integer Value")
            try_value_input = False

    name = input('please enter name: ')  # name is string and don't need error control value  error

    try_value_input = False
    while (not try_value_input):  # FOR ERROR CONTROL weight VALUE ERROR
        try:
            weight = input('please enter weight(kilo): ')
            try_value_input = True
        except ValueError:
            print("please enter a integer Value")
            try_value_input = False

    try_value_input = False
    while (not try_value_input):  # FOR ERROR CONTROL hight VALUE ERROR
        try:
            hight = input('please enter hight(centimeter): ')
            try_value_input = True
        except ValueError:
            print("please enter a integer Value")
            try_value_input = False

    try_value_input = False
    while (not try_value_input):  # FOR ERROR CONTROL width VALUE ERROR
        try:
            width = input('please enter width(centimeter): ')
            try_value_input = True
        except ValueError:
            print("please enter a integer Value")
            try_value_input = False

    try_value_input = False
    while (not try_value_input):  # FOR ERROR CONTROL price VALUE ERROR
        try:
            price = int(input('please enter price(integer and toman): '))
            try_value_input = True
        except ValueError:
            print("please enter a integer Value")
            try_value_input = False

            # print input specifications for User approval:
    print("\nyou\'r new product is :\nname = %s \nweight = %s \nhight = %s \nwidth = %s \nprice = %s " % (
        name, weight, hight, width, price))
    user_approval = input("\nare all of the information that enter ,True??:(y/n) ")
    if user_approval == 'n':  # User approval chek
        final_string = get_Specifications(locate_of_poiter)
    else:
        if locate_of_poiter == 0:
            final_string = '{ \"code\" : %s ,\"name\" : \"%s\", \"weight\" : %s, \"hight\" : %s, \"width\" : %s, \"price\" : %s}' % (
                code, name, weight, hight, width, price)
        else:
            final_string = '\n{ \"code\" : %s ,\"name\" : \"%s\", \"weight\" : %s, \"hight\" : %s, \"width\" : %s, \"price\" : %s}' % (
                code, name, weight, hight, width, price)
    return final_string


def append_new_data(addres_of_file):  # this function wan't to append new data to database
    try:  # for error control , if addres of file is wrong or file become lost.
        my_file = open(addres_of_file, 'a+')
        my_file.write(get_Specifications(my_file.tell()))
        my_file.close()
    except FileNotFoundError:
        print("ADDRES OF DATA FILE IS WRONG!! ")
        addres_of_file = input('please enter the TRUE addres ')
        append_new_data(addres_of_file)


def get_list_data(addres_of_file):  # make a list of dictionarys of datas
    try:
        my_file = open(addres_of_file, "r")
        list_information = my_file.readlines()
        # print(list_information)
        final_list = []
        for data in list_information:
            dictonary = eval(data)
            final_list.append(dictonary)
        my_file.close()
        return final_list
    except FileNotFoundError:
        print("ADDRES OF DATA FILE IS WRONG!! ")
        addres_of_file = input('please enter the TRUE addres ')
        get_list_data(addres_of_file)


def overwrite_database(list_information, addres_of_file):
    my_file = open(addres_of_file, 'w')
    for data in list_information:
        string = str(data)
        string += '\n'
        my_file.write(string)
    my_file.close()


# search a data by this code and return this dictonary
def search_data(addres_of_file, code):
    reference_list = get_list_data(addres_of_file)
    # for arg in Reference_list:
    #    if arg["code"] == code :
    #        return arg                 
    # use lambda and filter
    if_value = filter(lambda c: c['code'] == code, reference_list)
    if_value = list(if_value)
    return if_value


def print_data_in_TXT(addres_of_file, addres_of_final_file):  # print data as addres_of_file to addres_of_final_file

    my_list = open(addres_of_final_file, 'w')  # overwrithe file or make it
    refrence_list = get_list_data(addres_of_file)  # get a list of dict

    user_approval_sorting = input('do you wan\'t sorting by price?(y/n)')  # asking user to now do sort by price or no
    if user_approval_sorting == 'y':
        Ascending_Descending = int(input(
            'send the number you wan\'t:\n1.descending\n2.ascending\n:'))  # asking for now sorting descending or ascending
        if Ascending_Descending == 2:
            refrence_list = sorted(refrence_list, key=lambda arg: arg['price'])
        elif Ascending_Descending == 1:
            refrence_list = sorted(refrence_list, key=lambda arg: arg['price'], reverse=True)

    temp = 1
    for arg in refrence_list:  # print data arg in txt
        # print(arg)
        my_list.write('%s : %s\ncode : %s\nweight : %s\nhight : %s\nwidth : %s\nprice : %s\n\n' % (
            temp, arg['name'], arg['code'], arg['weight'], arg['hight'], arg['width'], arg['price']))
        temp += 1


def correction_data(addres_of_file, code):  # funcion for correction a wrong data
    refrence_list = get_list_data(addres_of_file)
    wrong_list = list(filter(lambda data: data['code'] == code, refrence_list))  # fine wrong datas
    for data in wrong_list:  # maybe we have two data whith wrong same code
        print(
            "\nyou\'r wrong prodct is :\nname = %s \ncode = %s\nweight = %s \nhight = %s \nwidth = %s \nprice = %s " % (
                data['name'], data['code'], data['weight'], data['hight'], data['width'], data['price']
            )
        )
        number_of_wrongs = int(input('how many value is wrong :'))
        if number_of_wrongs <= 6:
            for i in range(number_of_wrongs):
                wrong_key = input('please enter the key of wrong value to correction :')
                refrence_list[refrence_list.index(data)][wrong_key] = input('enter correct value %s:' % wrong_key)

    overwrite_database(refrence_list, addres_of_file)


def remove_data(addres_of_file, code):
    refrence_list = get_list_data(addres_of_file)
    wrong_list = list(filter(lambda data: data['code'] == code, refrence_list))
    for data in wrong_list:
        refrence_list.remove(data)
    overwrite_database(refrence_list, addres_of_file)

# my_file = open ( '/media/mahdi/3892E45A92E41DDE/Document/python/project bronzi/v2/data.txt','w')
# refrence_list = get_list_data('/media/mahdi/3892E45A92E41DDE/Document/python/project bronzi/V1/data.txt'
# )
# for data in refrence_list :
#    my_file.write('%s,\"%s\",%s,%s,%s,%s\n'%(data['code'],data['name'],data['weight'],data['hight'],data['width'],data['price']))
