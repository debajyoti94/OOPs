
from Custom_dict import ConfigDict


obj = ConfigDict('config_file.txt')

# print(obj['sql_query'])

obj['sql_query'] = 'select * from table'