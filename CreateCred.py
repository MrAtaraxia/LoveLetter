# CreateCred.py
# Creates a credential file.
from cryptography.fernet import Fernet
import re
import ctypes
import time
import os
import sys


class Credentials:

    def __init__(self):
        self._username = ""
        self._key = ""
        self._password = ""
        self._key_file = 'key.key'
        self._time_of_exp = -1

    # ----------------------------------------
    # Getter setter for attributes
    # ----------------------------------------

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        while username == '':
            username = input('Enter a proper User name, blank is not accepted:')
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._key = Fernet.generate_key()
        f = Fernet(self._key)
        self._password = f.encrypt(password.encode()).decode()
        del f

    @property
    def expiry_time(self):
        return self._time_of_exp

    @expiry_time.setter
    def expiry_time(self, exp_time):
        if exp_time >= 2:
            self._time_of_exp = exp_time

    def create_cred(self):
        """
        This function is responsible for encrypting the password and create  key file for
        storing the key and create a credential file with user name and password
        """

        cred_filename = 'CredFile.ini'

        with open(cred_filename, 'w') as file_in:
            file_in.write("#Credential file:\nUsername={}\nPassword={}\nExpiry={}\n"
                          .format(self._username, self._password, self._time_of_exp))
            file_in.write("++" * 20)

            # If there exists an older key file, This will remove it.
        if os.path.exists(self._key_file):
            os.remove(self._key_file)

            # Open the Key.key file and place the key in it.
        # The key file is hidden.
        try:

            os_type = sys.platform
            if os_type == 'linux':
                self._key_file = '.' + self._key_file

            with open(self._key_file, 'w') as key_in:
                key_in.write(self._key.decode())
                # Hidding the key file.
                # The below code snippet finds out which current os the scrip is
                # running on and does the taks base on it.
                if os_type == 'win32':
                    ctypes.windll.kernel32.SetFileAttributesW(self._key_file, 2)
                else:
                    pass

        except PermissionError:
            os.remove(self._key_file)
            print("A Permission error occurred.\n Please re run the script")
            sys.exit()

        self._username = ""
        self._password = ""
        self._key = ""
        # self._key_file


def create_cred():
    # Creating an object for Credentials class
    creds = Credentials()

    # Accepting credentials
    creds.username = input("Enter UserName:")
    creds.password = input("Enter Password:")
    print("Enter the epiry time for key file in minutes, [default:Will never expire]")
    creds.expiry_time = int(input("Enter time:") or '-1')

    # calling the Credit
    creds.create_cred()
    print("**" * 20)
    print("Cred file created successfully at {}"
          .format(time.ctime()))

    if not (creds.expiry_time == -1):
        os.startfile('expire.py')

    print("**" * 20)


def retrieve_cred():
    cred_filename = 'CredFile.ini'
    # key_file = 'key.key'

    # key = ''

    with open('.key.key', 'r') as key_in:
        key = key_in.read().encode()

        # If you want the Cred file to be of one
    # time use uncomment the below line
    # os.remove(key_file)

    f = Fernet(key)
    with open(cred_filename, 'r') as cred_in:
        lines = cred_in.readlines()
        config = {}
        for line in lines:
            tuples = line.rstrip('\n').split('=', 1)
            if tuples[0] in ('Username ', 'Password '):
                config[tuples[0]] = tuples[1]

        passwd = f.decrypt(config['Password '].encode()).decode()
        print("Password:", passwd)


def main():
    while True:
        name = input("create or retrieve")
        if name == "create":
            create_cred()
            break
        elif name == "retrieve":
            retrieve_cred()
            break
        else:
            "That input is not valid, please try again."


if __name__ == "__main__":
    main()
