# This is a simple Python script that will act as a cinima ticket pricer
 
def cinema_ticket():
    user = input("Please enter your age: ")
    Age = int(user)
    price = 0
   
    if Age < 0:
        print('Invalid age.')
        price = None
        return None
    elif Age < 13:
        print('Child ticket price is £5 ')
        price = 5  
    elif Age <= 17:
        print('Teen ticket price is £8 ')
        price = 8 
    elif Age <= 64:
        print('Adult ticket price is £12 ')
        price = 12
    else:
        print('Senior ticket price is £7 ')
        price = 7

# Now we have to see if they are eligible for a student ID discount
    student = input("Do you have a student ID? (yes/no): ").lower()
    if Age >= 18:
        return student
    if student == "yes" and Age >= 18:
        print('You are eligible for a student discount.')
        price -= 2
        print(f'Student discount is applied. Price is now £{price}')
    else:
        print('Not eligible for a student discount.')
    
    return price

cinema_ticket()
