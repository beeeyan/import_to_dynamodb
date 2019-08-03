import pandas as pd
import math
import sys
import datetime

if len(sys.argv) < 2:
    old_table_name = 'importtest'
    new_table_name = old_table_name
elif len(sys.argv) == 2:
    old_table_name = sys.argv[1]
    new_table_name = old_table_name
else:
    old_table_name = sys.argv[1]
    new_table_name = sys.argv[2]


now_date = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
template = 'aws dynamodb put-item --table-name ' + new_table_name + ' --item'
csv_input = pd.read_csv(old_table_name + '.csv', dtype="str")

for index, row in csv_input.iterrows():
    item_content = ''
    for i in range(len(row)):
        if type(row[i]) is str:
            item_content = item_content + '"' + row.index[i].split(' ')[0] + '" : { "' + row.index[i].split(' ')[1].strip('\(''\)') + '" : "' + str(row[i]) + '" }, '
    item_content = ' \'{ ' + item_content.rstrip(', ') + ' }\''
    print(str(index+1) + ' line')
    with open(new_table_name + '_import_' + now_date +'.sh', 'a') as f:
        f.write(template + item_content + '\n')