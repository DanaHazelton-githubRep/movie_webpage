# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/m-1013629057

import webbrowser

class Movie():
    """ This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"] #class varible-constant so capital letters

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,VALID_RATINGS):
        # initialize instance of class Movie
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = VALID_RATINGS
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class Music():
    """ This class provides a way to store music related information"""

    def __init__(self,band_name,band_album,album_cover,song_preview):
        # initialize instance of class Music
        self.name = band_name
        self.band_album = band_album
        self.album_cover = album_cover
        self.song_preview = song_preview





##if __name__ == '__main__':
##	print 'This program is being run by itself'
##	
##else:
##	print 'I am being imported from another module'
##	        
# print (Movie.__module__)
# print (Movie.__doc__)
# print (Music.__name__)
#print (grown_ups.storyline)
