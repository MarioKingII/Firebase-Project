import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore, auth 


firebaseConfig = """ ---------->>>>>>>>>> INSERT CONFIGURATION FOR SDK """


firebase = pyrebase.initialize_app(firebaseConfig)
authization = firebase.auth()
#This is the key!
cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {'storageBucket': """------>>> INSERT HERE <<<--------"""})

db = firestore.client() 

Logging = input("Do you have an account? Y/N?") 
#create an username and password. 
if Logging.lower() == "n": 
    username = input("Enter your email as your Username: ")
    password = input("Create your new Password: ")
    user = auth.create_user(email = username ,password =  password)
    print("User created sucessfully")
    login = authization.sign_in_with_email_and_password(username ,  password) # this created a token which is unique to the user 
# Validate username and password.
else:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    login = authization.sign_in_with_email_and_password(username ,  password)



LoggedIn = True
#Creates the loop
while LoggedIn: 

    option = input(f"\nWhat would you like to do?\n1. Add a new contact \n2. Update an existing contact\n3. Delete an existing contact \n4. Exit")
    #Creates a new contact
    if option == "1": 
        option_1 = input("Do you want to add a person (1) or a business (2) or create a new category (3)")
        
        #Creates a new contact in the people collection
        if option_1 == "1": 
            first_name = input("Enter first name: ")
            last_name = input("Enter Last name: ")
            Name = (first_name +" "+ last_name)
            Key = input("what is the phone number : ")
            PhoneNumber = Key
            Address = input("Enter address: ")
            Email = input("Enter Email: ")
            db.collection('People').document(Key).set({"Name": Name, "Phone_number": PhoneNumber, "Email" : Email , "Address" : Address })
        
        #Creates a new contact in the business collection
        elif option_1 == "2": 
            Name = input("Enter Business Name: ")
            Key = input("what is the phone number : ")
            PhoneNumber = Key
            Address = input("Enter address: ")
            Email = input("Enter Email: ")
            FaxNumber = input("Enter Fax Number: ")
            db.collection('Business').document(Key).set({"Business Name" : Name, "Phone_number": PhoneNumber, "Email" : Email , "Address" : Address, "Fax Number" : FaxNumber })
        
        # Create a collection 
        elif option_1 == "3": 
            collection_name = input("Enter the category's name? : ")
            Name = input("Enter Name: ")
            Key = input("what is the phone number : ")
            PhoneNumber = Key
            Address = input("Enter address: ")
            Email = input("Enter Email: ")
            FaxNumber = input("Enter Fax Number: ")
            db.collection(collection_name).document(Key).set({"Name" : Name, "Phone_number": PhoneNumber, "Email" : Email , "Address" : Address, "Fax Number" : FaxNumber })

    #Updates a contact    
    elif option == "2": 
        collection_name = input("Enter the category's name? : ")
        Key = input("what is the phone number : ")
        Name = input("Enter new Name: ")
        PhoneNumber = input("what is the new phone number : ")
        Address = input("Enter new address: ")
        Email = input("Enter new Email: ")
        db.collection(collection_name).document(Key).update({"Name" : Name, "Phone_number": PhoneNumber, "Email" : Email , "Address" : Address })

    # Deletes a contact
    elif option == "3":   
        collection_name = input("Enter the category's name? : ")
        Key = input("what is the phone number : ")
        db.collection(collection_name).document(Key).delete()

    # Exit the application 
    elif option == "4": # Exit the application 
        LoggedIn = False
        print("You have been successfully logged out") 

    # In case the user makes a wrong selection
    else: 
        print("\nYou have entered a wrong selection!\n")
        print("Please enter a valid option")