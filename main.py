from API_DB_operations import API_DB
from Post import Post
from Local_DB_operations import Local_DB
from Update_LocalDB_using_API import Update_LocalDB

local_DB = Local_DB()
API_db = API_DB()
update_db = Update_LocalDB()

#Executing random data handling operations on the API
APIPosts = API_db.get_all_posts()
randomPost = API_db.get_post_by_id("1")
print("API Posts : ")
print(APIPosts)
print("Post with ID 1 from the API : ")
print(randomPost)

#testing the update of the Local Database using the API call
local_DB.delete_all_post()
allPosts = update_db.update_all_posts()
print("Posts added from the API to the local DB: ")
print(allPosts)

#Executing random data handling operations on the local database
newPost = Post("kamil","101","dummy title","The only thing I know is that I know nothing")
local_DB.insert_post(newPost)
getNewPostByID = local_DB.get_post_by_id('101')
getNewPostByTitle = local_DB.get_post_by_title('dummy title')
print("New Locally added post: ")
print(getNewPostByID)
print("New Locally added post: ")
print(getNewPostByTitle)
localPosts = local_DB.get_all_posts()
print("All Local Posts :")
print(localPosts)
local_DB.delete_post_by_id("101")



