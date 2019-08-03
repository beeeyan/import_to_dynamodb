aws dynamodb put-item --table-name importtest --item '{ "id" : { "S" : "001" }, "name" : { "S" : "Java" }, "years" : { "N" : "1" } }'
aws dynamodb put-item --table-name importtest --item '{ "id" : { "S" : "003" }, "name" : { "S" : "JavaScript" }, "years" : { "N" : "1" }, "note" : { "S" : "I use jQuery" } }'
aws dynamodb put-item --table-name importtest --item '{ "id" : { "S" : "002" }, "name" : { "S" : "Python" }, "years" : { "N" : "1" } }'
