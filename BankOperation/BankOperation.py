''' A bank operagtion program where users eihter login or
 register for the first time.'''
import random
database = {}    #map account number to personal details


 #  Welcome message
def start():
    print("Welcome to Every body's Bank PLC ")
    
    isOptionValid = False
    while isOptionValid == False:

        haveAccount =int(input('Do you have an account with us?' '\nPlease enter 1 for yes, 2 for no\n'))
        if (haveAccount ==1):
            isOptionValid = True
            login()
        elif (haveAccount ==2):
            isOptionValid =True
            print('########   Register now   #######')
            register()
        else:
            print('Please enter a valid option')
 
def login():
    print('#######    Login    #######')
    isLoginSuccessful = False

    while isLoginSuccessful == False:
        accountNumberFromUser = int(input('Enter your account number\n'))
        password = input('Enter your password')

        for accountNumber, userDetails in database.items():
            if (accountNumber == accountNumberFromUser):
                if (userDetails[3] == password):
                    isLoginSuccessful = True

        print ('invalid account number or password!')
    bankOperations()

def register ():
    firstName = input('Please enter your first name\n')
    lastName = input('Please enter your last name\n')
    email = input('Please enter an existing email address\n')
    password = input('Please enter a five character passsword\n')
    confirmPassword = input('Repeat your choose password\n')
    len(password) != 5

    while len(password) != 5:
        
        password = input('Please enter a five character passsword\n')
        confirmPassword = input('Repeat your choose password\n')

        if (password == confirmPassword):
            len(password) >6 and len(password)<4

        else:
            print ('please confirm your passsword')
            break


    accountNumber = generateAccountNumb()
    database[accountNumber] =[firstName,lastName, email, password]
    print(database)
    print("Your account has been created")

    login()

def bankOperations():
    print("Welcome what activity do you want to perform?\n")
    print('These are the available options: ')
    print('\t1: Withdrawal')
    print('\t2: Cash Deposit')
    print('\t3: Complaint')
    selectedOption = int(input('Please select an option:\t'))
            

    if (selectedOption == 1):
        print('You selected %s' % selectedOption )
        withdrawal = int( input('How much would you like to withdraw?\n'))
        print('Take your cash')

    elif(selectedOption == 2):
        print('You  selected %s'% selectedOption )
        deposit = int(input('how much would you liked to deposit?\n'))
        print('Your current balance is %s' % deposit)


    elif(selectedOption == 3):
        print ('You selected %s' % selectedOption )
        complaint = input('What issue will you like to report\t')
        print("Thank you for contacting us")

    else:
        print('Invalid option')
 


def generateAccountNumb():
    #print('generating account number:')
    return random.randrange(0000000000, 9999999999)

start()
#print(register())

