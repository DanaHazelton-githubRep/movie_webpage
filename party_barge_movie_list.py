#!/usr/bin/env python

# In this file, the instances of the class Movie are defined.

# After running this code, open the file partybarge_movies.html to
# see moive webpage!


import fresh_tomatos
import media


gladiator = media.Movie(
  "Gladiator",
  "When a Roman general is betrayed and his family murdered by an emperor's" 
  "corrupt son, he comes to Rome as a gladiator to seek revenge.",
  "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
  "www.youtube.com/watch?v=AxQajgTyLcM",
  "R")

happy_gilmore = media.Movie(
  "Happy Gilmore",
  "A rejected hockey player puts his skills to the golf course to save his "
  "grandmother's house.",
  "https://upload.wikimedia.org/wikipedia/en/b/be/Happygilmoreposter.jpg",
  "https://www.youtube.com/watch?v=-6sT7MSJ4GE",
  "PG")

grown_ups = media.Movie(
  "Grown Ups",
  "After their high school basketball coach passes away, five good friends and"
  "former teammates reunite for a Fourth of July holiday weekend.",
  "https://upload.wikimedia.org/wikipedia/en/f/fe/Grownupsmovie.jpg",
  "https://www.youtube.com/watch?v=e01NVCveGkg",
              "PG")

step_brothers = media.Movie("Step Brothers",
  "Two aimless middle-aged losers still living at home are forced against their"
  " will to become room-mates when their parents marry.",
  "https://upload.wikimedia.org/wikipedia/en/thumb/d/d9/StepbrothersMP08.jpg/220px-StepbrothersMP08.jpg",
  "https://www.youtube.com/watch?v=V6Z7PEvedHQ",
  "R")

_300 = media.Movie(
  "300",
 "King Leonidas of Sparta and a force of 300 men fight the Persians at "
 "Thermopylae in 480 B.C.",
 "https://upload.wikimedia.org/wikipedia/en/5/5c/300poster.jpg",
 "www.youtube.com/watch?v=WkG34G6a59M",
 "R")

smokey_and_the_bandit=media.Movie(
  "Smokey and the Bandit",
  "The Bandit is hired on to run a tractor trailer full of beer over county "
  "lines in hot pursuit by a pesky sheriff.",
  "http://www.bandittransamclub.com/Smokey-And-The-Bandit-Poster-1.jpg",
  "https://www.youtube.com/watch?v=IzMpOvKxXdM",
  "R")

shinnig = media.Movie(
  "The Shining",
  "A family heads to an isolated hotel for the winter where an evil and "
  "spiritual presence influences the father into violence,while his psychic son"
  " sees horrific forebodings from the past and of the future.",
  "http://www.slashanddine.com/wp-content/uploads/2011/12/The-Shining.jpg",
  "https://www.youtube.com/watch?v=5Cb3ik6zP2I",
  "R")

halloween = media.Movie(
  "Halloween",
  "On Halloween night of 1963, 6-year old Michael Myers stabbed his sister to"
  " death. After sitting in a mental hospital for 15 years, Myers escapes and"
  " returns to Haddonfield to kill.",
  "https://images.moviepilot.com/images/c_limit,q_auto,w_710/ynz4sydvly8xaybce87k/halloween-poster.jpg",
  "https://www.youtube.com/watch?v=xHuOtLTQ_1I",
  "R")

nightmare_on_elm_street = media.Movie(
  "Nightmare on Elm Street",
  "Several people are hunted by a cruel serial killer who kills his victims in"
  " their dreams. When the survivors are trying to find the reason for being "
  "chosen, the murderer won't lose any chance to kill them as soon as they fall"
  " asleep.",
  "https://upload.wikimedia.org/wikipedia/en/e/ee/A_Nightmare_on_Elm_Street_2010_poster.jpg",
  "https://www.youtube.com/watch?v=KzfdyjnPLJk",
  "R")


#create a list of movies to pass on to fresh_tomatos.py to create html doc.
movies = [gladiator,happy_gilmore,grown_ups,step_brothers,_300,
          smokey_and_the_bandit,shinnig,halloween,nightmare_on_elm_street]



fresh_tomatos.open_movies_page(movies)




