from flask import Flask, request, abort
app = Flask(__name__)

from user_account_details import UserAccountDetails

@app.route('/')
def welcome():
    return 'Welcome to the Login page'

@app.route('/change_to_user/<str:user_name>/') #/change/
def perform_change_to_user(target_user_name, manager_name, manager_password):
    user_details = UserAccountDetails()

    return (user_details.change_to_user(user_name)))

@app.route('/change_to_manager/<str:user_name>') #/change/
def perform_change_to_user(user_name):
    user_details = UserAccountDetails()
    return (user_details.change_to_manager(user_name))

@app.route('change_name/<str:old_user_name>/<str:new_user_name>')
def perform_change_name(old_user_name, new_user_name):
    user_details = UserAccountDetails()
    return (user_details.perform_change_username(old_user_name, new_user_name))

@app.route('/create/<str:username>/<str:fname>/<str:lname>/int<dobyear>')
def perform_create_user(user_name, first_name, last_name, birth_year):
    new_user = UserAccountDetails()
    return (new_user.create_new_user(user_name, first_name, last_name, birth_year))

@app.route('/delete/<str:username>')
def perform_delete_user(user_name):
    del_user = UserAccountDetails()
    return (del_user.delete_new_user(user_name))


if __name__ == "__main__":
    app.run(debug= True, host = '0.0.0.0')

#LIST OF FUNCTIONS
# UserAccountDetails()
    # check_admin(self, user_name) # no need to use flask on this - called by other functions to confirm permission
    # change_access(self, user_name) - NEEDS FLASKING - split into change_to_user and change_to_manager
    # change_username(self, old_user_name, new_user_name) - NEEDS FLASKING
    # table_update(self, user_name) # changed to delete_new_user - NO NEED TO FLASK - OBSOLETE
    # delete_new_user(self, user_name) - NEEDS FLASKING
    # check_existence(self, user_name) - NO NEED TO FLASK
    # create_new_user(self,user_name,first_name,last_name,birth_year) - NEEDS FLASKING


# ## Completed from previous
# password_strength_prompt() # the same as check_policy - DEPENDENCY - NO NEED TO FLASK?

# UserPasswordDetails()
    # read_password_policy()
    # check_policy()
    # check_list()
    # check_user_details()
    # THE ABOVE FOUR DON'T NEED FLASKING
