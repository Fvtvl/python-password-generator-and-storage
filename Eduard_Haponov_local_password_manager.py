# Importing necessary modules
import os 
import csv
from cryptography.fernet import Fernet 

class PasswordManager:
    def __init__(self):
        #initializing class variables
        self.key = None  # Variable to store encryption key
        self.password_dict = {}  # Dictionary to store passwords

    #create key for ecndrypt password
    def create_key(self, path):
        self.key = Fernet.generate_key()  
        with open(path, 'wb') as f: 
            f.write(self.key)  
    #load key for ecndrypt password
    def load_key(self, path):
        with open(path, 'rb') as f:  
            self.key = f.read()  

    def save_passwords_to_object(self, folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".csv"): 
                file_path = os.path.join(folder_path, filename) 
                with open(file_path, 'r', newline='') as csvfile: 
                    reader = csv.reader(csvfile) 
                    next(reader)  # Skipping the header row
                    passwords = []  
                    for idx, row in enumerate(reader, start=1):  
                        #encrypting each password in the row and formatting it
                        password_items = [f"{{position: \"{idx}\", password: \"{self.encrypt_password(password)}\"}}" for password in row]
                        #joining encrypted passwords into a single string and adding to the list
                        passwords.append("{" + ','.join(password_items) + "}")
                self.password_dict[filename] = ''.join(passwords)  #adding encrypted passwords to dictionary
        print(self.password_dict)  
    #function for encrypt a password using the encryption key
    def encrypt_password(self, password):
        
        cipher_suite = Fernet(self.key)  
        encrypted_password = cipher_suite.encrypt(password.encode()).decode() 
        return encrypted_password  

def main():
    folder_path = "E:\\Documents\\JS\\py-password-generator"  
    pm = PasswordManager()  
    pm.load_key("Eduard_Haponov_mykey.key")  
    pm.save_passwords_to_object(folder_path)  

if __name__ == "__main__":
    main() 
