import scrapper

url = 'https://medium.com'
user = url + '/@ocittwo'

content = scrapper.get(user)

name = content.find('h1').text
link = content.find_all('a')
web = link[4].text
following = link[5].text
followers = link[6].text

stories = content.find_all('div', class_='dg')
last_story = []

def get_link(story):
  item = story.find_all('a')
  return url + item[len(item) - 1].attrs['href']

for story in stories:
  last_story.append({
      'title': story.find('h1').text,
      'descs': story.find('p').text,
      'date': story.find(class_='u').find_all('span')[1].text,
      'link': get_link(story)
  })

user_data = {
  'name':name,
  'web': web,
  'following': following,
  'followers': followers,
  'last_story' : last_story
}

print(user_data)
