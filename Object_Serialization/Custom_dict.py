import pickle

class MyCustomException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return "This is a custom exception message. {}".format(self.message)
        else:
            return "This is a standard error message from MyCustomException"

class ConfigDict(dict):

    def __init__(self, filename):
        self._filename = filename

        try:
            with open(self._filename, 'rb') as file_handle:  #IF FILE DOES NOT EXIST RAISE AN EXCEPTION
                dict_dump = pickle.load(file_handle)
                for key in dict_dump:
                    dict.__setitem__(self, key, dict_dump[key])

        except FileNotFoundError:
            raise FileNotFoundError("File {} does not exist.".format(self._filename))

    def __setitem__(self, key, value):
        # here we have to add the functionality of writing to a file
        # each line has a delimiter '=' sign
        # first scan through the file and see if the key exists, if yes then overwrite, else rewrite
        dict.__setitem__(self,key, value)
        with open(self._filename, 'wb') as file_handle:
            pickle.dump(self, file_handle)

    def __getitem__(self, item):
        # simply use the dictionary method and use the self dictionary to obtain the value
        # IF KEY DOES NOT EXIST
        if not item in self:
            raise MyCustomException(self.keys())
        return dict.__getitem__(self, item)