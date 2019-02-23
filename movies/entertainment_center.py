# file creates final website with your list of movies below
import fresh_tomatoes

# contains class "media" to store your instances of movies
import media

# Creates new instance of movie: Toy Story
toy_story = media.Movie("Toy Story",  # title of the movie
                        # brief storyline
                        "A story of a boy and his toys that come to life",
                        # url for the movie's poster
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/"
                        "p17420_p_v8_ab.jpg",
                        # url for the movie's trailer on youtube
                        "https://www.youtube.com/watch?v=ZivIO58KISI")

# Creates new instance of movie: Avatar
avatar = media.Movie("Avatar",  # title of the movie
                     # brief storyline
                     "A marine on a alien planet",
                     # url for the movie's poster
                     "http://t0.gstatic.com/images?q=tbn:"
                     "ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-"
                     "jp",
                     # url for the movie's trailer on youtube
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Creates new instance of movie: Drishyam
drishyam = media.Movie("Drishyam",  # title of the movie
                       # brief storyline
                       "A man tries to save his family from the dark side of"
                       "the law after they commit an unexpected crime.",
                       # url for the movie's poster
                       "http://t1.gstatic.com/images?q=tbn:ANd"
                       "9GcTkMKFMrv9gfroA4CC9c9C_d8I1NrhiGgVhYGL7xMWO5oylqi4_",
                       # url for the movie's trailer on youtube
                       "https://www.youtube.com/watch?v=AuuX2j14NBg")

# Creates new instance of movie: Frozen
frozen = media.Movie("Frozen",  # title of the movie
                     # brief storyline
                     "When their kingdom becomes trapped in perpetual winter,"
                     "Anna and Kristoff try to find Anna's sister,"
                     " and break her icy spell.",
                     # url for the movie's poster
                     "http://ia.media-imdb.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl"
                     "5BanBnXkFtZTgwNjk3MTcyMDE@._V1_UY1200_CR90,0,630,1200_AL"
                     "_.jpg",
                     # url for the movie's trailer on youtube
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")

# Creates new instance of movie: Divergent
divergent = media.Movie("Divergent",  # title of the movie
                        # brief storyline
                        "In a world where people are divided into distinct"
                        "factions based on human virtues, Tris is warned she"
                        "is Divergent and will never fit into any one group.",
                        # url for the movie's poster
                        "http://resizing.flixster.com/v6RA8Fkkl7nspE8k005wzVC4"
                        "7Xw=/800x1200/v1.bTsxMTE3ODkxMDtqOzE3MTQ5OzIwNDg7ODA"
                        "wOzEyMDA",
                        # url for the movie's trailer on youtube
                        "https://www.youtube.com/watch?v=sutgWjz10sM")

# Creates new instance of movie: Kahani
kahani = media.Movie("Kahani",  # title of the movie
                     # brief storyline
                     "A pregnant woman's efforts to find her missing husband"
                     "make her the target of an assassin dispatched by his"
                     "secretive employers.",
                     # url for the movie's poster
                     "https://upload.wikimedia.org/wikipedia/en/thumb/8/85/"
                     "KahaaniPoster.jpg/220px-KahaaniPoster.jpg",
                     # url for the movie's trailer on youtube
                     "https://www.youtube.com/watch?v=j1wEeuAosNM")

# compiles all instances of new movies in an array
movies = [toy_story, avatar, drishyam, frozen, divergent, kahani]

# creates webpage
fresh_tomatoes.open_movies_page(movies)

