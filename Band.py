class Band:
    def __init__(self,band_name,music_genre):
        self.band_name=band_name
        self.music_genre=music_genre
    def describe_band(self):
        print("The name of the band",self.band_name)
        print("The music_genre is",self.music_genre)
    def is_active(self):
        print("The band is active")
band=Band("any","song")
band1=Band("ring","tiktok")
band2=Band("hi","facebook")
band1.describe_band()
band1.is_active()
band2.describe_band()
band2.is_active()
band.describe_band()
band.is_active()



