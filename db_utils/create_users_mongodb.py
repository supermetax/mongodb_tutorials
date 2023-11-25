from user_operations import create_user

'''
Function : To create a bulk number of users in the DB
'''
def create_10_users():
    # Call the create_user function to add 10 records
    for i in range(1, 11):
        email = f'user{i}@example.com'
        password = f'securepassword{i}'
        create_user(email, password)

    print("10 records added successfully.")

'''
Function : To create a user in the DB based on the given user id and password
'''
def create_user_by_credentials(email, password):
    # Call the create_user function to add a single record
    create_user(email, password)
    #print("User added successfully.")

'''
Function : Main 
'''
if __name__ == "__main__":
    # Call the functions
    # create_10_users()

    # Example usage for creating a single user
    create_user_by_credentials('user70@example.com', 'securepassword70')
