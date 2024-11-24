class Facebook:
    def __init__ (self, username, password):
        self.username = username
        self.Password = password

    def post(self):
        print(f"{self.username} posting some content")   

    def follow(self, user2):
        print(f"{self.username} following {user2} ...")

    def share(self):
        print(f"{self.username} is sharing via Facebook Class")


class Tiktok:
    def __init__(self, username, Password):
        self.username = username
        self.Password = Password

    def make_reels(self):
        print(f"{self.username} making reels ...")

    def comment(self):
        print(f"{self.username} adding a comment")

    def share_screen(self):
        print(f"{self.username} sharing thier screen ...")   

    def add_music_to_profile(self):
        print(f"{self.username} adding music to profile...")


profile1 = Facebook("Kiran", "ask_any_doubt")

profile1.post()
profile1.follow("Python")
profile1.share()

Profile2 = Tiktok("Kiran","ask_any_doubt")

Profile2.make_reels()
Profile2.share_screen()
Profile2.add_music_to_profile()


            
