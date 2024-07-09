class User:
    user_dict = {}
    user_list = []

    def __init__(self, name, password, age=None):
        self.name = name
        self.password = hash(password)
        self.age = age
        User.user_dict[self.name] = self.password
        User.user_list.append(self)

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
        User.user_dict[self.name] = self.password
        User.user_list.append(self)

    def __str__(self):
        return f'{self.users.keys()}'


user = User('Alex', 'qwer1234', 23)
user2 = User('Alexx', 'qwer14', 23)
print(user)
print(User.user_dict)
print(User.user_list)
urvideo = UrVideo(User.user_dict, Video.video_list)
urvideo.register('Den', '4321', 40)
print(User.user_dict)
print(User.user_list)
