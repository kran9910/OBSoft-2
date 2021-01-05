#Class that implements the methods responsible for fetching post objects from the API
import requests
import json

class API_DB:
    # Fetch all posts in the API
    def get_all_posts(self):
        request = requests.get(
            str('https://jsonplaceholder.typicode.com/posts'),
        )
        posts = request.json()
        return posts

    # Fecth a post from the API using its id
    def get_post_by_id(self,post_id):
        url = 'https://jsonplaceholder.typicode.com/posts/' + str(post_id)
        request = requests.get(
            str(url),
        )
        post = request.json()
        return post


