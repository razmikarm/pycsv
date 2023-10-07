from pycsv import read_csv, write_csv
from pprint import pprint as print


data = read_csv('data.csv')
print(data)

data['age'][1] = 50

write_csv(data, 'result.csv')
