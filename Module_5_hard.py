import time

class User:

    def __init__(self, nickname, password, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

class Video:

    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname != nickname and hash(user.password) != hash(password):
                return
            else:
                self.current_user = user


    def register(self, nickname, password, age):
        for user in self.users:
            if nickname in user.nickname:
                print(f'Пользователь {nickname} уже существует')
                return


        user = User(nickname, password, age)
        self.users.append(user)
        self.current_user = user

    def log_out(self, current_user):
        self.current_user = None


    def add(self, *args):
        if args not in self.videos:
            for film in args:
                self.videos.append(film)

    def get_videos(self, text):
        list_search = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_search.append(video.title)
        return list_search

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста, покиньте страницу")
                    return
                for i in range(video.duration):
                    print(f"{i}")
                    time.sleep(1)
                video.time_now = 0
                print('Конец видео')


ur = UrTube()
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
ur.watch_video('Для чего девушкам парень прoграммист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')


# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')