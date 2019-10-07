class Post:
    def __init__(self, id, photo_url, name, body):
        self.id = id
        self.photo_url = photo_url
        self.name = name
        self.body = body

posts =[]
class PostStore:
    def get_all(self):
      return posts

    def add(self, post):
        posts.append(post)

    def get_by_id(self, id):
        for post in posts:
          if post.id == id:
            return post
        
    def update(self, id, fields):
      for post in posts:
        if post.id == id:       
          post.name=fields[0]
          post.body=fields[1]

    def delete(self, id):
      for post in posts:
        if post.id == id:        
          posts.remove(post)



post1 = Post(id=1,
             photo_url='https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=50&w=50',
             name='Sara',
             body='Lorem Ipsum')
post2 = Post(id=2,
             photo_url='https://images.pexels.com/photos/736716/pexels-photo-736716.jpeg?auto=compress&cs=tinysrgb&dpr=1&h=100&w=100',
             name='John',
             body='Lorem Ipsum')

store = PostStore()
print('__1__')
store.get_all()
store.add(post1)
print('__2__')
store.get_all()
store.add(post2)
print('__3__')
store.get_all()
print(store.get_all()[0].name)
print(store.get_by_id(2).body)
updatefilelds = ['name','Ali']
store.update(1,updatefilelds)
print(store.get_all()[0].name)
print(store.get_all())