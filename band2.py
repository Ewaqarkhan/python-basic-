class Band:
    def __init__(self,band_name,music_genre):
        self.band_name=band_name
        self.music_genre=music_genre
        self.home_awards=0
        self.international_awards=0
    def describe_band(self):
        print("The name of the band",self.band_name)
        print("The music_genre is",self.music_genre)
    def is_active(self):
        print("The band is active")

    def set_home_awards(self,home_awards):
        self.home_awards=home_awards
    def set_international_awards(self,international_awards):
        self.international_awards=international_awards
class RockBand(Band):
    def __init__(self,band_name,music_genre,):
      super().__init__(band_name,music_genre)
      self.rock_consert_movemebts=[]
    def show_movements(self):
        for i in self.rock_consert_movemebts:
            print(i)
class Choir(Band):
    def __init__(self,band_name,music_genre,):
      super().__init__(band_name,music_genre)
      self.noone=12
    def display(self):
        print("the is method to displaychore")


choir=Choir("ring","tiktok")
choir.display()



