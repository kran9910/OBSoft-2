# OBSoft-2

Post.py: Implements a class for the Post objects 

LocalSqlConnection.py: Implements a singleton class that connects to a local database and returns a cursor that you can use for querying.

Local_DB_Operations.py: Implements a class that is responsible for handling data for my objects in the local MySql Database. (insert new records, fetch records, etx...)
 
API_DB_Operations.py: Implements a class that is responsible for fetching data from the API

Update_LocalDB_using_API: Implements a class that the main class will call in order to fetch the objects. This class will check if there's data in the local database it will not call the api, otherwise it will call the api and update the database. 
