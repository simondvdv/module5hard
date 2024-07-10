import keyboard
import time


class User:
    user_list = []

    def __init__(self, name, password, age=None):
        self.name = name
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.name

class Video:
    video_names_list = []
    video_list = []

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
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
        for i in User.user_list:
            if name == i.name:
                print(f'Пользователь {name} уже существует')
                return
        self.current_user = User(name, password, age)
        User.user_list.append(User(name, password, age))

    def log_out(self):
        self.current_user = None

    def add(self, *video_list):
        for i in video_list:
            if i.title not in Video.video_names_list:
                Video.video_list.append(i)
                Video.video_names_list.append(i.title)

    def get_videos(self, check_word):
        check_word = check_word.lower()
        founded_videos = []
        for i in Video.video_list:
            if check_word in i.title.lower():
                founded_videos.append(i.title)
        if len(founded_videos) == 0:
            return 'По вашему запросу ничего не найдено'
        return founded_videos

    def watch_video(self, videos_name):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for i in Video.video_list:
            if videos_name == i.title:
                if i.adult_mode is True and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                else:
                    while True:
                        print(i.time_now)
                        time.sleep(1)
                        i.time_now += 1
                        if i.time_now == i.duration + 1:
                            print('Конец видео')
                            break
                        if keyboard.is_pressed(' '):
                            break
            else:
                continue
        return


ur = UrTube(User.user_list, Video.video_list)
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
