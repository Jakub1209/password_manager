import pandas
from os.path import exists

# ---------------------------- CONSTANTS ------------------------------- #

DATA_FILE_PATH = "_internal/data/passwords.csv"

DATA_ROW_1 = "website"
DATA_ROW_2 = "email"
DATA_ROW_3 = "password"

# ---------------------------- CLASSES ------------------------------- #


class Database:
    def __init__(self):
        # initialize the variables
        self.data_index = 0
        self.data_list = []

        # if a file with the data exists, read the data and load it as a list of dictionaries
        if exists(DATA_FILE_PATH):
            self.data_read = pandas.read_csv(DATA_FILE_PATH)
            self.data_list = self.data_read.to_dict(orient="records")

        # if the file doesn't exist, create it
        else:
            file = open(DATA_FILE_PATH, mode="w")
            file.close()

    def add_new_data(self, input_1, input_2, input_3, overwrite_data=False):
        if overwrite_data:
            # overwrite the existing password with a new one
            self.data_list[self.data_index][DATA_ROW_3] = input_3
        else:
            # save the input data in a dictionary
            new_account_data = {
                DATA_ROW_1: input_1,
                DATA_ROW_2: input_2,
                DATA_ROW_3: input_3,
            }
            # append the data to the data_list
            self.data_list.append(new_account_data)

        # convert the database to a DataFrame and save it as a CSV file
        data_to_save = pandas.DataFrame(self.data_list)
        data_to_save.to_csv(DATA_FILE_PATH, index=False)

    def is_password_in_database(self, input_1, input_2):
        # if there is an entry in the database
        if len(self.data_list) > 0:
            # scan every data entry and save the index
            for index in range(0, len(self.data_list)):
                self.data_index = index
                # if the inputted email is linked with the inputted website, the account password is in the database
                if self.data_list[index][DATA_ROW_1] == input_1 and \
                        self.data_list[index][DATA_ROW_2] == input_2:
                    return True

    def get_password(self):
        return self.data_list[self.data_index][DATA_ROW_3]
