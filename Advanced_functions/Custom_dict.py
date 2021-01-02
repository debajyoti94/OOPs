
class ConfigDict(dict):

    def __init__(self, filename):
        self._filename = filename
        with open(self._filename, 'r') as file_handle:
            for line in file_handle.readlines():
                print(line)
                key_value_list = [x for x in line.split('=')]
                dict.__setitem__(self, key_value_list[0], key_value_list[1])
                # print(line)
            # dict.__getitem__()

    def __setitem__(self, key, value):
        # here we have to add the functionality of writing to a file
        # each line has a delimiter '=' sign
        # first scan through the file and see if the key exists, if yes then overwrite, else rewrite
        dict.__setitem__(self,key, value)
        with open(self._filename, 'w') as file_handle:
            for key, value in self.items():
                file_handle.write(key+'='+value+'\n')

    def __getitem__(self, item):
        # simply use the dictionary method and use the self dictionary to obtain the value

        return dict.__getitem__(self, item)