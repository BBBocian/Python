def email_name(email):
    name=""
    for i in email:
        if i == "@":
            print(name)
            break
        else:
            name +=i
            
    
def print_digits(message):

    dig_list = [x for x in message if x.isdigit()]

    print(dig_list)
    

def print_digits2(message):

    print(re.findall("\d",message))
