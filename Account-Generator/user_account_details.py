from mysql.connector import connect, Error
from password_checks import UserPasswordDetails


class UserAccountDetails():
    # pw_user_db, user_info, username, FirstName, LastName, BirthYear, password, Manager
    # host=52.214.153.42
    def check_admin(self, user_name, user_password):  # check if the admin value is true

        with connect(host="63.35.225.165", user="root", password="my_secret_password", database="pw_user_db") as connection:

            with connection.cursor() as cursor:

                command = "SELECT * FROM `user_info` WHERE `username`= '{}' AND `password`='{}' AND `Manager` = 1;".format(
                    user_name, user_password)

                cursor.execute(command)
                cursor.fetchall()
                num_occurences = cursor.rowcount
                # print("num_occurences assigned")
                cursor.close()

                if num_occurences > 0:
                    return True
                elif num_occurences == 0:
                    return False

    def check_existence(self, user_name):  # checks if a user exists in a database

        with connect(host="63.35.225.165", user="root", password="my_secret_password", database="pw_user_db") as connection:

            with connection.cursor()as cursor:
                command = "SELECT * FROM `user_info` WHERE `username`= '{}';".format(user_name)
                cursor.execute(command)
                cursor.fetchall()
                num_occurences = cursor.rowcount
                # print("num_occurences assigned")
                cursor.close()

                if num_occurences > 0:
                    return True  # if it exists it will return True
                else:
                    return False  # if doesnt exists will return False

    def create_new_user(self, user_name, first_name, last_name, birth_year, password):  # creates user details
        # check_admin()
        # birth_year = int(birth_year)
        with connect(host="63.35.225.165", user="root", password="my_secret_password", database="pw_user_db") as connection:

            if self.check_existence(user_name):
                return "{} already exists.".format(user_name)

            elif not UserPasswordDetails().check_list(password) or not UserPasswordDetails().check_policy(
                    password) or not UserPasswordDetails().check_user_details(first_name, last_name, birth_year, password):
                password = UserPasswordDetails().generate_password()
                with connection.cursor()as cursor:
                    command = "INSERT INTO `user_info`(`username`, `FirstName`, `LastName`, `BirthYear`, `password`, `Manager`) VALUES ('[{}]', '[{}]', '[{}]', '{}', '[{}]', NULL);".format(
                        user_name, first_name, last_name, birth_year, password)
                    cursor.execute(command)
                    cursor.close()
                    return "Your password is weak."

            else:
                with connection.cursor()as cursor:
                    command = "INSERT INTO `user_info`(`username`, `FirstName`, `LastName`, `BirthYear`, `password`, `Manager`) VALUES ('[{}]', '[{}]', '[{}]', '{}', '[{}]', NULL);".format(
                        user_name, first_name, last_name, birth_year, password)
                    cursor.execute(command)
                    cursor.close()
                    return "You have been successfully added to the database system."

    def change_to_manager(self, user_name, manager_name,
                          manager_password):  # changes the value of user role back to manager role
        with connect(host="63.35.225.165", user="root", password="my_secret_password", database="pw_user_db") as connection:

            if self.check_admin(manager_name, manager_password):
                if self.check_existence(user_name):
                    with connection.cursor()as cursor:
                        command = "UPDATE `user_info` SET `Manager`= '1' WHERE `username` = '{}';".format(user_name)
                        cursor.execute(command)
                        cursor.close()
                        return "The account has been changed to admin status."
                else:
                    return "The user doesn't exist"
            else:
                return "You require an admin level account to change from user to admin status."

    def change_to_user(self, user_name, manager_name,
                       manager_password):  # changes the value of manager role back to user role
        with connect(host="63.35.225.165", user="root", password="my_secret_password", database="pw_user_db") as connection:

            if self.check_admin(manager_name, manager_password):
                if self.check_existence(user_name):
                    with connection.cursor()as cursor:
                        command = "UPDATE `user_info` SET `Manager`=NULL WHERE `username` = '{}';".format(user_name)
                        cursor.execute(command)
                        cursor.close()
                        return "The account has been changed to user"

            else:
                return "You require an admin level account to update user status."

    def change_username(self, old_user_name, new_user_name, manager_name,
                        manager_password):  # only if the user is an admin, allows to change the user name
        with connect(host="63.35.225.165", user="root", password="my_secret_password", database="pw_user_db") as connection:
            if self.check_admin(manager_name, manager_password):
                if self.check_existence(old_user_name):
                    if not self.check_existence(new_user_name):
                        with connection.cursor()as cursor:

                            command = "UPDATE `user_info` SET `username` = '{}' WHERE `username` = '{}';".format(
                                new_user_name, old_user_name)
                            cursor.execute(command)
                            cursor.close()
                            return "{} has been changed to {}".format(old_user_name, new_user_name)
                    else:
                        return "The new user already exists in the database"
                else:
                    return "The user doesn't exist"
            else:
                return "You require an admin level account to update a username."

    def delete_user(self, user_name, manager_name, manager_password):  # deletes user details
        with connect(host="63.35.225.165", user="root", password="my_secret_password", database="pw_user_db") as connection:

            if self.check_admin(manager_name, manager_password):
                if self.check_existence(user_name):
                    with connection.cursor()as cursor:
                        command = "DELETE FROM `user_info` WHERE `username`= '{}';".format(user_name)
                        cursor.execute(command)
                        cursor.close()
                        return "The account {} has been deleted from the database".format(user_name)
                else:
                    return "The user you are trying to delete isn't on the database"
            else:
                return "You require an admin level account to delete user details."

# File Test

# print(UserAccountDetails().delete_user("user", "admin", "admin")) #Works, Used a test DB to delete an entry
# print(UserAccountDetails().change_to_user("tyree", "admin", "admin")) #Works, returns the right strings depends on the input
#print(UserAccountDetails().create_new_user("test_username","test_firstname","test_lastname", "1997", "7$!5I6c2-F1r7m1S")) #Works, if accort already exists will infom user, if password is weak will generate new pass inserts to DB
# print(UserAccountDetails().check_admin("gvuut", "admin"))#Works, returns True if admin details are correct
# print(UserAccountDetails().change_username("test_user", "New_user", "admin", "admin"))#Works, doesnt let the new username change if it's already in uses, only lets you change name if you have admin details
# print(UserAccountDetails().change_to_manager("hfsah", "admin", "admin"))#Works, Only works if you have admin details and the username is in the database
# print(UserAccountDetails().check_existence("tgvwhd"))#Works, Check is a username is in teh database
