class Blog:
  def __init__(self, title, photo, name,date,content):
    self.title = title
    self.photo = photo
    self.name = name
    self.date = date
    self.content = content

blog1= Blog(title='python bisics', photo='https://images.pexels.com/photos/837140/pexels-photo-837140.jpeg', 
name='Yasser',date='10-06-2019',content='Hello How r u ?')

blog2= Blog(title='python bisics', photo='https://images.pexels.com/photos/837140/pexels-photo-837140.jpeg', 
name='Mohammed',date='11-16-1979',content='Hello How r u ?')

blog3= Blog(title='python bisics', photo='https://images.pexels.com/photos/837140/pexels-photo-837140.jpeg', 
name='Sara',date='10-06-2019',content='Hi ')


print(blog1.name)
print(blog2.date)
print(blog3.content)


blogs=[blog1,blog2,blog3]
blogs[2].name='Ali'
blogs.remove(blogs[0])
print(blog3.name)
