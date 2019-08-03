import pandas as pd
import math
import sys
import datetime

if len(sys.argv) < 2:
    table_name = 'importtest'
else:
    table_name = sys.argv[1]

now_date = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
template = 'aws dynamodb put-item --table-name ' + table_name + ' --item'
csv_input = pd.read_csv(table_name + '.csv', dtype="str")

for index, row in csv_input.iterrows():
    item_content = ''
    for i in range(len(row)):
        if type(row[i]) is str:
            item_content = item_content + '"' + row.index[i].split(' ')[0] + '" : { "' + row.index[i].split(' ')[1].strip('\(''\)') + '" : "' + str(row[i]) + '" }, '
    item_content = ' \'{ ' + item_content.rstrip(', ') + ' }\''
    print(str(index+1) + ' line')
    with open(table_name + '_import_' + now_date +'.sh', 'a') as f:
        f.write(template + item_content + '\n')