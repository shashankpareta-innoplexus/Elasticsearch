bin=$JDBC_IMPORTER_HOME/bin
lib=$JDBC_IMPORTER_HOME/lib
echo $bin
echo $lib
echo '{
"type" : "jdbc",
"jdbc" : {
"driver": "com.mysql.jdbc.Driver",
"url" : "jdbc:mysql://192.168.0.154/database_test",
"user" : "root",
"password" : "shashank1107",
"sql" : "select , id as _id from mytable",
"index" : "jdbc",
"type" : "mytype",
"sql.write" : "true",
"strategy":"standard",
"interval":"5",
"bulk_size": 100,
"max_bulk_requests": 30,
"bulk_timeout": "20s",
"flush_interval":"5s",
"elasticsearch" : {
             "cluster" : "shashank-cluster1",
             "host" : "192.168.0.154",
             "port" : 9200
        }
}
}' | java \
-cp "${lib}/*" \
-Dlog4j.configurationFile=${bin}/log4j2.xml \
org.xbib.tools.Runner \
org.xbib.tools.JDBCImporter
