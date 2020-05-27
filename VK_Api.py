import requests
import json

class VkApiResponse():
    
    def __init__(self, member_id):
        self.id = member_id
        self.friends_response = 'https://api.vk.com/method/friends.get?user_id='
        self.albums_response = 'https://api.vk.com/method/photos.getAlbums?user_id='
        self.user_response = 'https://api.vk.com/method/users.get?user_id='
        self.token = '&v=5.52&access_token=6a1a49816a1a49816a1a49817e6a6870f466a1a6a1a498134d45eff5b6598a2a934fd7b'

    def get_users_list(self):
        friends = requests.get(self.friends_response + self.id + self.token)
        json_friends = json.loads(friends.content)
        for friend in json_friends['response']['items']:
            fr = requests.get(self.user_response + str(friend) + self.token)
            json_friend = json.loads(fr.content)
            first_name = json_friend['response'][0]['first_name']
            last_name = json_friend['response'][0]['last_name']
            print("Имя: " + first_name +  ", Фамилия: " + last_name)

    def get_albums_list(self):
        albums = requests.get(self.albums_response + self.id + self.token)
        json_albums = json.loads(albums.content)
        for album in json_albums["response"]["items"]:
        	print("Название альбома: " + album["title"] + ", Кол-во фото: " + str(album["size"]))

print("Введите id пользователя")
member_id = input()
main_class = VkApiResponse(member_id)
print("Список друзей: введите friends;" + "Список альбомов: введите albums")
resp = input()
if (resp == "friends"):
    main_class.get_users_list()
elif (resp == "albums"):
    main_class.get_albums_list()
else:
    print("Что-то пошло не так, попробуйте снова")
