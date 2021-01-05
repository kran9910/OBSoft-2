#Class that implements methods responsible for handling Post objects in the local DB
from LocalSqlConnection import Connection

class Local_DB:
#Method that inserts the post in the local database
  def insert_post(self,post):
      connection = Connection()
      insert_stmt = (
          "INSERT INTO POST(userID, id, title, body)"
          "VALUES (%s, %s, %s, %s)"
      )
      data = (post.userId, post.id, post.title, post.body)
      try:
          #Executing the SQL command
          connection.cursor.execute(insert_stmt,data)
          # Commit your changes in the database
          connection.conn.commit()

      except:
          # Rolling back in case of error
          connection.conn.rollback()

#Method that fetches the post in the local database using its title
  def get_post_by_title(self,title):
      connection = Connection()
      retrieve_stmt = "SELECT * from Post WHERE title LIKE %s"
      data = (title,)
      try:
          #Executing the SQL command
          connection.cursor.execute(retrieve_stmt,data)
          # Fetching all rows from the result table
          result = connection.cursor.fetchall()
      except:
          # Rolling back in case of error
          connection.conn.rollback()
      return result

#Method that fetches the post in the local database using its id
  def get_post_by_id(self,id):
      connection = Connection()
      retrieve_stmt = "SELECT * from Post WHERE id LIKE %s"
      data = (id,)
      try:
          #Executing the SQL command
          connection.cursor.execute(retrieve_stmt,data)
          # Fetching all rows from the result table
          result = connection.cursor.fetchall()
      except:
          # Rolling back in case of error
          connection.conn.rollback()
      return result

#Method that fetches all the post in the local database
  def get_all_posts(self):
      connection = Connection()
      retrieve_stmt = '''SELECT * from Post'''
      try:
          #Executing the SQL command
          connection.cursor.execute(retrieve_stmt)
          # Fetching all rows from the result table
          result = connection.cursor.fetchall()
      except:
          # Rolling back in case of error
          connection.conn.rollback()
      return result

#Method that deletes the post in the local database using its title
  def delete_post_by_title(self,title):
      connection = Connection()
      delete_stmt = "DELETE from Post WHERE title LIKE %s"
      data = (title,)
      try:
          #Executing the SQL command
          connection.cursor.execute(delete_stmt,data)
          # Commit your changes in the database
          connection.conn.commit()
      except:
          # Rolling back in case of error
          connection.conn.rollback()

#Method that fetches the post in the local database using its id
  def delete_post_by_id(self,id):
      connection = Connection()
      delete_stmt = "DELETE from Post WHERE id LIKE %s"
      data = (id,)
      try:
          #Executing the SQL command
          connection.cursor.execute(delete_stmt,data)
          # Commit your changes in the database
          connection.conn.commit()
      except:
          # Rolling back in case of error
          connection.conn.rollback()

#Method that deletes all posts in the local database
  def delete_all_post(self):
      connection = Connection()
      delete_stmt = "DELETE from Post"
      try:
          #Executing the SQL command
          connection.cursor.execute(delete_stmt)
          # Commit your changes in the database
          connection.conn.commit()
      except:
          # Rolling back in case of error
          connection.conn.rollback()
