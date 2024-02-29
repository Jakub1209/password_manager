from random import shuffle, choice


class PasswordGenerator:

    def __init__(self):
        # initialize all the variables
        self.key = ""
        self.password_length = 0
        self.generated_password = []
        self.all_characters = {
            "special_characters": "~`!@#$%^&*()_+-={}[]:|;',./<>?",
            "letters": "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM",
            "digits": "1234567890",
        }

    def generate_password(self, password_length=15):
        # reset all values of the variables
        self.password_length = password_length
        self.generated_password = []

        # add characters to the self.generated_password list
        self.add_characters(self.generated_password)

        # shuffle the list for extra randomness
        shuffle(self.generated_password)
        # join the list together to receive a string
        return ''.join(self.generated_password)

    def add_characters(self, password_characters_list):
        # this if block ensures, that there are equal amounts of different character categories in the password
        if self.key == "special_characters":
            self.key = "letters"
        elif self.key == "letters":
            self.key = "digits"
        else:
            self.key = "special_characters"

        # if the length of the password is insufficient, call this function again to add another character to the list
        if len(self.generated_password) < self.password_length:
            password_characters_list += choice(self.all_characters[self.key])
            self.add_characters(password_characters_list)
