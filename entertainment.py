import os
import media
import movie_website
os.chdir('C:/Users/admin/Documents/python idle files')
print(os.getcwd())
toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that came to life',
                        'https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_QL50_SY1000_SX670_AL_.jpg',
                        'https://www.youtube.com/watch?v=wmiIUN-7qhE')
#print(toy_story.storyline)
avatar = media.Movie('Avatar',
                     'A marine on a alien planet',
                     'https://m.media-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_QL50_.jpg',
                     'https://www.youtube.com/watch?v=6ziBFh3V1aM')
#avatar.show_trailer()
forest_gump = media.Movie('Forest Gump',
                          'Forrest Gump, a man with a low IQ, joins the army for service where he meets Dan and Bubba. However, he cannot stop thinking about his childhood sweetheart Jenny Curran, whose life is messed up.',
                          'https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg',
                          'https://www.youtube.com/watch?v=SgduyXzxwS8')

Dark_knight = media.Movie('The Dark Knight Rises',
                          'Bane, an imposing terrorist, attacks Gotham City and disrupts its eight-year-long period of peace. This forces Bruce Wayne to come out of hiding and don the cape and cowl of Batman again.',
                           'https://m.media-amazon.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_QL50_.jpg',
                           'https://www.youtube.com/watch?v=ay-Xg1oTeAs')

idiots = media.Movie('3 Idiots',
                       'Two friends are searching for their long lost companion. They revisit their college days and recall the memories of their friend who inspired them to think differently, even as the rest of the world called them "idiots".',
                       'https://m.media-amazon.com/images/M/MV5BNTkyOGVjMGEtNmQzZi00NzFlLTlhOWQtODYyMDc2ZGJmYzFhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_QL50_SY1000_CR0,0,694,1000_AL_.jpg',
                       'https://www.youtube.com/watch?v=K0eDlFX9GMc')

rang_de = media.Movie('Rang De Basanti',
                      'When Sue selects a few students to portray various Indian freedom fighters in her film, she unwittingly awakens their patriotism. The emotional and mental process turns them into rebels for a cause.',
                      'https://m.media-amazon.com/images/M/MV5BM2I3OGU1YmQtNjIyOC00OGYzLWFkOTgtOGIyMDVlNmE2M2VmXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_QL50_SY1000_SX700_AL_.jpg',
                      'https://www.youtube.com/watch?v=QHhnhqxB4E8')
movies = [toy_story,avatar,forest_gump,Dark_knight,idiots,rang_de]
movie_website.open_movies_page(movies)

