#class Facebook:
#    def __init__(self, first_name, last_name, mobile, email):
#        self.first_name = first_name
#        self.last_name = last_name
#        self.mobile = mobile
#        self.email = email
        

#    def printAll(self):
#        print('first_name: ' + self.first_name)
#        print('last_name: ' + self.last_name)
#        print('mobile: ' + self.mobile)
#        print('email: ' + self.email)



#def create():
#    dic_person={}
#    first_name=input("What's your first name? ")
#    last_name=input("What's your last name? ")
#    mobile=input("What's your mobile phone number? ")
#    email=input("What's your email address? ")
#    #Facebook(first_name,last_name,mobile,email)
#    dic_person=dict(zip(['first_name','last_name','mobile','email'],[first_name,last_name,mobile,email]))
#    print(dic_person)
#    return dic_person



#def read_all(person):
#    if len(person)==0 :
#        print("no data")
#    else :
#        values_list=[]
#        for person_val in person :
#            values_list.append(person_val.values())
#        for dic_person in values_list :
#            dic_person.printAll()

#def read_by_condition():
#        __main__()

#if __name__ == "__main__" :
#    person=[]
#    while True:
#        print("Choose the menu you want below:")
#        print("1:create   2:read all  3:read by condition  4:exit")
#        choose_num=int(input())
#        if choose_num == 1:
#            dic_person=create()
#            person.append(dic_person)
#        elif choose_num == 2:
#            read_all(person)
#        elif choose_num == 3:
#            read_by_condition()
#        elif choose_num == 4:
#            break
#        else :
#            print("incalid menu number!")


class Facebook:
    def __init__(self, first_name, last_name, mobile, email):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.email = email
        

    def printAll(self):
        print('first_name: ' + self.first_name)
        print('last_name: ' + self.last_name)
        print('mobile: ' + self.mobile)
        print('email: ' + self.email)



def create():
    dic_person={}
    first_name=input("What's your first name? ")
    last_name=input("What's your last name? ")
    mobile=input("What's your mobile phone number? ")
    email=input("What's your email address? ")
    list_person=Facebook(first_name,last_name,mobile,email)
    return list_person



def read_all(person):
    if len(person)==0 :
        print("no data")
    else :
        for list_person in person  :
            list_person.printAll()
            print("None\n")

def read_by_condition(person):
    dic_person={}
    search=input("keyword>")
    print("\n")
    for list_person in person  :
        dic_person=dict(zip(['first_name','last_name','mobile','email'],[list_person.first_name,list_person.last_name,list_person.mobile,list_person.email]))
        for i in dic_person.keys():
            if dic_person.get(i)==search :
                list_person.printAll()
                print("None\n")
            


if __name__ == "__main__" :
    a = Facebook("oh", "eh", "123", "asdfas")
    b = Facebook("eh", "oh", "456", "bvdsa")

    person=[a,b]
    while True:
        print("Choose the menu you want below:")
        print("1:create   2:read all  3:read by condition  4:exit")
        choose_num=int(input("prompt>"))
        if choose_num == 1:
            list_person=create()
            person.append(list_person)
        elif choose_num == 2:
            read_all(person)
        elif choose_num == 3:
            read_by_condition(person)
        elif choose_num == 4:
            break
        else :
            print("incalid menu number!")



