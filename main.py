import keyboard
class User:
    user_dict = {}
    user_list = []

    def __init__(self, name, password, age=None):
        self.name = name
        self.password = hash(password)
        self.age = age
        if self.name not in User.user_dict.keys():
            User.user_dict[self.name] = self.password
            User.user_list.append(self)
        else:
            print('Такой пользователь уже есть')

    def __str__(self):
        return f'name: {self.name}\npassword: {self.password}\nage: {self.age}'


class Video:
    video_list = []

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        if title not in Video.video_list:
            Video.video_list.append(title)


class UrVideo:
    def __init__(self, users, videos, current_user=None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        if nickname not in self.users.keys():
            print('Такого пользователя нет')
            return
        if self.users[nickname] == hash(password):
            self.current_user = nickname

    def register(self, name, password, age=None):
        self.name = name
        self.password = hash(password)
        self.age = age
        if self.name not in User.user_dict.keys():
            User.user_dict[self.name] = self.password
            User.user_list.append(self)
            self.current_user = name
        else:
            print('Такой пользователь уже есть')

    def log_out(self):
        self.current_user = None

    def add(self, *video_list):
        for i in video_list:
            if i not in Video.video_list:
                Video.video_list.append(i)

    def get_videos(self, check_word):
        check_word = check_word.lower()
        founded_videos = []
        for i in Video.video_list:
            if check_word in i.lower().split(' '):
                founded_videos.append(i)
        if len(founded_videos) == 0:
            print('По вашему запросу ничего не найдено')
        else:
            print('По вашему запросу есть следующие видео:')
            j = 1
            for i in founded_videos:
                print(f'{j}. {i}')
                j += 1

    def watch_video(self):
        pass

    def __str__(self):
        return f'{self.users.keys()}'


user = User('Alex', 'qwer1234', 23)
user2 = User('Alexx', 'qwer14', 23)
print(user)
print(User.user_dict)
print(User.user_list)
urvideo = UrVideo(User.user_dict, Video.video_list)
print(urvideo.current_user)
urvideo.register('Den', '4321', 40)
print(User.user_dict)
print(User.user_list)
user3 = User('Alex', 'qwer1234', 23)
print(User.user_dict)
print(User.user_list)
urvideo.register('Den', '4321', 40)
print(User.user_dict)
print(User.user_list)
print(urvideo.current_user)
urvideo.log_out()
print(urvideo.current_user)
video1 = Video('qwe', 0, 0, False)
urvideo.add('123', 'qwe', 'qwt1q')
print(Video.video_list)
urvideo.add('123', 'husky', 'Qwe tewtw', '321 123')
print(Video.video_list)
print('qwe' in 'rwqfe qewdwe qwe sdecse'.split(' '))
urvideo.get_videos('vwtb')
urvideo.get_videos('qwe')


import time

sec = 0

while True:
    print(sec)
    time.sleep(1)
    sec += 1
    if sec == 5:
        break
    if keyboard.is_pressed(' '):
        break
