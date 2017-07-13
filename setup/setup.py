file = open("oksp/settings/conf.py","w")

comment = "\"\"\"\n";
file.write(comment)
file.write("Configuration file for settings\n")
file.write(comment)
print ("\n---------------------------------------\n")
print("We are by default going to allow all hosts to access the files, you can change this by updating the ALLOWED_HOSTS in oksp/settings/conf.py")
print("For other files, please enter the following fields")
print("\n")
SECRET_KEY 	= input("\nEnter A Secret Key  >> ")
DB_NAME 	= input("\nEnter Database Name >> ")
print("\nPlease Note that the user must have editing and creating tables access to this database")
DB_USERNAME = input("Enter UserName for the database >> ")
DB_PASSWORD = input("\nEnter Password for the User >> ")
print("\nWe used the default host_name and port, i.e. localhost:5432. You can change this at oksp/settings/conf.py")

string = """
SECRET_KEY = '"""+SECRET_KEY+"""'

ALLOWED_HOSTS = ['*']

DB_NAME = '"""+DB_NAME+"""'

DB_USERNAME = '"""+DB_USERNAME+"""'

DB_PASSWORD = '"""+DB_PASSWORD+"""'

DB_HOST_NAME = 'localhost'

DB_PORT = '5432'

ADMINS_EMAIL_LIST = [
    # ('Name', 'email@example.com'),
]
"""
file.write(string)
production = input("Do you want the server to be production server? (Y/n) >> ").upper()
if production=='Y':
	file.write("DJANGO_SETTINGS_MODULE = 'oksp.settings.production'")
file.close()
