#This Class will check if there's data in the database it will not call the api, otherwise it will call the api and update the database
from API_DB_operations import API_DB
from Local_DB_operations import Local_DB
from Post import Post


class Update_LocalDB:


  #Constructor
  def __init__(self):
    self.Localdb = Local_DB()
    self.APIdb = API_DB()

  def update_all_posts(self):
      posts = self.Localdb.get_all_posts()
      if posts:
          return posts
      else:
          posts = self.APIdb.get_all_posts()
          for post in posts:
              newpost = Post(userId= post.get('userId'), id= post.get('id'), title= post.get('title'), body= post.get('body') )
              self.Localdb.insert_post(newpost)
          return posts