bin=/home/shashank.pareta/Documents/MyElasticSearch/Learning/elasticsearch-jdbc-2.3.3.0/bin
lib=/home/shashank.pareta/Documents/MyElasticSearch/Learning/elasticsearch-jdbc-2.3.3.0/lib
echo $bin
echo $lib
echo '{
"type" : "jdbc",
"jdbc" : {
"driver": "com.mysql.jdbc.Driver",
"url" : "jdbc:mysql://localhost:3306/database_test",
"user" : "root",
"password" : "shashank1107",
"sql" : "select , id as _id from mytable;",
"index" : "jdbc",
"type" : "mytype",
"sql.write" : "true",
"strategy":"standard",
"interval":"5",
"bulk_size": 100,
"max_bulk_requests": 30,
"bulk_timeout": "10s",
"flush_interval":"5s"
}
}' | java \
-cp "${lib}/*" \
-Dlog4j.configurationFile=${bin}/log4j2.xml \
org.xbib.tools.Runner \
org.xbib.tools.JDBCImporter
