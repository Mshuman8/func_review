################################################################################
#                               FUNCTION REVIEW                                #
################################################################################

####Review the format of a function (def, function name, parameters, colon, code of function, return):

def length_checker(item):
    length = len(item)
    print("The length is " + str(length))
    return length
    

# It might be helpful to show the students this again. You can save a string as a variable and use it as an argument for your function. Then you can set your function WITH A SPECIFIC VARIABLE equal to a variable because whatever the function returns will be what is saved.  Then you can print the variable to check. 
name = "Eliseo"
len_my_name = length_checker(name)
print(len_my_name)



## Creation of function:

#It takes three cups of sugar to make a batch of cookies.  Create a function whose parameter is the number of batches of cookies you will be making and will determine how many cups of sugar you need. 

def sugar_for_cookies(num_batches):
    total_sugar = num_batches*3
    return total_sugar


#Call sugar_for_cookie() and determine how many cups of sugar are needed for 20 batches of cookies.

print(sugar_for_cookies(20))


#It takes two sticks of butter to make a batch of cookies.  Create a function whose parameter is the number of batches of cookies you will be making and willd etermine how many containers of butter you need to buy (*Hint there are four sticks of butter in a container)

def butter_for_cookies(num_batches):
    total_butter = num_batches*2
    if total_butter%4 == 0:
        total_container = total_butter/4
    else: 
        total_container = total_butter//4 + 1
    return total_container


# Call butter_for_cookies() to determine how much butter is needed for 10 batches.

print(butter_for_cookies(10))


#Create a function called grocery_list_maker that uses the two functions you have made above to determine how much butter and sugar you need to buy. 

def grocery_list_maker(batches):
    sugar = sugar_for_cookies(batches)
    butter = butter_for_cookies(batches)
    print("You need to buy " + str(sugar) + " cups of sugar and " + str(butter) + " containers of butter")
    
    
# Call grocery_list_maker and determine how much sugar and butter is needed for 5 batches of cookies.

# This will check our grocery_list_maker() for five batches.
grocery_list_maker(5)