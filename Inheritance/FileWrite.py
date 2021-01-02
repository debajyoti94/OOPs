''' In this code we will implement inheritance'''

import abc
import datetime

# creating an abstract class
class WriteFile(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, filename):
        self.filename = filename

    @abc.abstractmethod
    def write(self):
        return

class LogFile(WriteFile):

    def get_time(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    def write(self, input):
        with open(self.filename, 'a') as file_handle:
            time = self.get_time()
            file_handle.write(str(time)+"\t"+str(input)+'\n')

class DelimFile(WriteFile):

    def __init__(self, filename, delimiter):
        #inheriting the constructor from the parent class
        super(DelimFile, self).__init__(filename)
        self.delimiter = delimiter

    def write(self, input):
        # the line below works when the string itself does not contain a delimiter
        # write_to_file = self.delimiter.join(input)
        with open(self.filename, 'a') as file_handle:
            for item in input:
                if self.delimiter in item:
                    file_handle.write('\"'+str(item)+'\"'+self.delimiter)
                else:
                    file_handle.write(item + self.delimiter)
            # file_handle.write(write_to_file + '\n')
            file_handle.write('\n')