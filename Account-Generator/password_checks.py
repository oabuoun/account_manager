import configparser
from mysql.connector import connect, Error
import string
import random
#from password_policy import policy

class UserPasswordDetails():

    def generate_password(self):

            # reading through the password policy and looping through to extract necessary values to check and generates the password
            policy_checklist = self.read_password_policy()
            max_length = policy_checklist[5]
            allowed_characters = list(policy_checklist[6])

            # Generating the password using random and string modules
            password = ""
            for character in range(max_length):

                random_character = random.randint(1,4)

                if random_character == 1:
                    password += random.choice(allowed_characters)
                elif random_character == 2:
                    password += random.choice(string.ascii_lowercase)
                elif random_character == 3:
                    password += random.choice(string.ascii_uppercase)
                else:
                    password += random.choice(string.digits)
            #print(password) testing
            return password


    def check_list(self, password):
        with connect(host="63.35.225.165", user="root", password="my_secret_password", database="pw_user_db") as connection:
        # checks password against passwords in common_passwords.txt. Returns True if password is not in file, False if found.Written by KW
        # sql_password = getpass("Please input your SQL database password: ")
            with connection.cursor()as cursor:

                command = "SELECT * FROM `common_passwords` WHERE `password` = '{}';".format(password)

                cursor.execute(command)
                cursor.fetchall()
                #print(cursor.rowcount)
                #print(password)
                num_occurences = cursor.rowcount
                # print("num_occurences assigned")
                cursor.close()
            #print(num_occurences) Tests
            if num_occurences > 0:
                #print("In DB")
                return False
            elif num_occurences == 0:
                #print("Not in DB")
                return True



    def check_policy(self, password):
        # reads password policy, checks if password complies with requirements. Returns True if yes, False if not. Written by KW
        policy_list = self.read_password_policy()
        # print(policy_list)
        # now have a list defining password policy
        num_specials = policy_list[0]
        num_lowercase = policy_list[1]
        num_uppercase = policy_list[2]
        num_numbers = policy_list[3]
        min_length = policy_list[4]
        max_length = policy_list[5]
        allowed_specials = policy_list[6]

        count_specials = 0
        count_lower = 0
        count_upper = 0
        count_numbers = 0

        if len(password) < min_length or len(password) > max_length:
            # not compliant if too short or too long
            print("Too short")
            return False

        for letter in password:
            # check each letter to see if special, lower, upper, or number. Count each of these
            if letter.isdigit():
                count_numbers += 1
            elif letter.isupper():
                count_upper += 1
            elif letter.islower():
                count_lower += 1
            elif letter in allowed_specials:
                count_specials += 1
            else:
                # return false if part of password is not in any allowed category
                print("illegal character")
                return False
        #print(count_specials)
        # now have a count of all the lower, upper, special characters and numbers
        if count_upper >= num_uppercase and count_lower >= num_lowercase and count_specials >= num_specials and count_numbers >= num_numbers:
            print("Returning True")
            return True
        else:
            return False


    def check_user_details(self, user_firstname, user_lastname, user_birthyear, password):
        # checks if the password contains the user name or year of birth. Outputs True if no user details in the password. Written by KW
        if user_firstname in password:
            #print("First")
            return False
        elif user_lastname in password:
            #print("last")
            return False
        elif user_birthyear in password:
            #print("birth")
            return False
        else:
            #print("USer OK")
            return True
    def read_password_policy(self):
        # reads in password policy, returns variables as a list. Written by KW
        # password_policy = open('password_policy.txt', 'r')
        policy = configparser.ConfigParser()
        policy.read('password_policy.txt')
        num_specials = policy.getint('Policy', 'num_specials')
        num_lowercase = policy.getint('Policy', 'num_lowercase')
        num_uppercase = policy.getint('Policy', 'num_uppercase')
        num_numbers = policy.getint('Policy', 'num_numbers')
        min_length = policy.getint('Policy', 'min_length')
        max_length = policy.getint('Policy', 'max_length')
        allowed_specials = policy.get('Policy', 'allowed_specials')

        return [int(num_specials), int(num_lowercase), int(num_uppercase), int(num_numbers), int(min_length),
                int(max_length), allowed_specials]

# Testing functions


#print(UserPasswordDetails().generate_password()) #Works, no errors
#UserPasswordDetails().check_list("password") # Works, but sql errors due to server
#print(UserPasswordDetails().check_policy("5432ytsKHF++y4")) # no errors check password according to policy.txt file
#print(UserPasswordDetails().check_user_details("1997","FirstName","LastName", "1997")) # Works, prints False if it is a bad password
#print(UserPasswordDetails().read_password_policy())# Works, no errors and can be called in other internal functions
