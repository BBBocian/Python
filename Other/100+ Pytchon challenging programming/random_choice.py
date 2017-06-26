import random

def random_even_0_10():
    x = random.choice([x for x in range(0,11) if x%2 ==0])

    print(x)

#random_even_0_10()

def random_even_div_5_7():
    x = random.choice([x for x in range(201) if x%5==0 and x%7==0])

    print(x)

#random_even_div_5_7()

def random5_in_100_200():

    for i in range(5):
        print(random.choice([x for x in range(100,201)]))

    # or:

    #print(random.sample(range(100,201),5))

#random5_in_100_200()

def random5_even_in_100_200():

    x = random.sample(([x for x in range(100,201) if x%2==0]),5)

    print(x)

#random5_even_in_100_200()

def random5_div_by_5_7_in_100_200():

    x=random.sample([x for x in range(1,1001) if x%5==0 and x%7==0],5)

    print(x)

#random5_div_by_5_7_in_100_200()

def random_int_7_15():
    x = random.randrange(7,15)
    print(x)

random_int_7_15()
