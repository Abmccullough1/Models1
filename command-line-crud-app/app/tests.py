from django.test import TestCase
from app import models



class TestMovies(TestCase):
    def test_add_movie(self):
        movie = models.add_movie(
            "Batman",
            "1989",
            "Batman",
        )

        self.assertEqual(movie.id, 1)
        self.assertEqual(movie.name, "Batman")
        self.assertEqual(movie.release_date, "1989")
        self.assertEqual(movie.main_character, "Batman")

    def test_view_all(self):
        Movies_Data = [
            {
                "name":"Batman",
                "release_date": 1989,
                "main_character":"Batman"
            },
            {
                "name":"Dumb and dumber",
                "release_date": 1994,
                "main_character":"Harry and Lloyd"
            },
            {
                "name":"Megamind",
                "release_date":2010,
                "main_character":"Megamind"
            },
            {
                "name":"Good Burger",
                "release_date": 1997,
                "main_character":"Ed and Dexter"
            }
            
        ]
        for Movie_Data in Movies_Data:
            models.add_movie(
                Movie_Data["name"],
                Movie_Data["release_date"],
                Movie_Data["main_character"]
            )
        movies = models.view_All()

        self.assertEqual(len(movies),len(Movies_Data))

        Movies_Data = sorted(Movies_Data, key=lambda c: c["name"])
        movies = sorted(movies, key=lambda c: c.name)

        for data,movie in zip(Movies_Data,movies):
            self.assertEqual(data["name"], movie.name)
            self.assertEqual(data["release_date"], movie.release_date)
            self.assertEqual(data["main_character"], movie.main_character)


    def test_search_by_name(self):
        Movies_Data = [
            {
                "name":"Batman",
                "release_date": 1989,
                "main_character":"Batman"
            },
            {
                "name":"Dumb and dumber",
                "release_date": 1994,
                "main_character":"Harry and Lloyd"
            },
            {
                "name":"Megamind",
                "release_date":2010,
                "main_character":"Megamind"
            },
            {
                "name":"Good Burger",
                "release_date": 1997,
                "main_character":"Ed and Dexter"
            }
            
        ]
        for Movie_Data in Movies_Data:
            models.add_movie(
                Movie_Data["name"],
                Movie_Data["release_date"],
                Movie_Data["main_character"]
            )
        self.assertIsNone(models.view_by_movie_name("Superman"))

        movie = models.view_by_movie_name("Megamind")

        self.assertIsNotNone(movie)
        self.assertEqual(movie.release_date, 2010)

    def test_update_release(self):
        Movies_Data = [
            {
                "name":"Batman",
                "release_date": 1989,
                "main_character":"Batman"
            },
            {
                "name":"Dumb and dumber",
                "release_date": 1992,
                "main_character":"Harry and Lloyd"
            },
            {
                "name":"Megamind",
                "release_date":2010,
                "main_character":"Megamind"
            },
            {
                "name":"Good Burger",
                "release_date": 1997,
                "main_character":"Ed and Dexter"
            }
            
        ]
        for Movie_Data in Movies_Data:
            models.add_movie(
                Movie_Data["name"],
                Movie_Data["release_date"],
                Movie_Data["main_character"]
            )
        models.update_release("Dumb and dumber", 1994)

        self.assertEqual(
            models.view_by_movie_name("Dumb and dumber").release_date, 1994
        )
    def test_delete_movie(self):
        Movies_Data = [
            {
                "name":"Batman",
                "release_date": 1989,
                "main_character":"Batman"
            },
            {
                "name":"Dumb and dumber",
                "release_date": 1994,
                "main_character":"Harry and Lloyd"
            },
            {
                "name":"Megamind",
                "release_date":2010,
                "main_character":"Megamind"
            },
            {
                "name":"Good Burger",
                "release_date": 1997,
                "main_character":"Ed and Dexter"
            }
            
        ]
        for Movie_Data in Movies_Data:
            models.add_movie(
                Movie_Data["name"],
                Movie_Data["release_date"],
                Movie_Data["main_character"]
            )
        models.delete_movie("Batman")

        self.assertEqual(len(models.view_All()), 3)
    def test_view_by_date(self):
        Movies_Data = [
            {
                "name":"Batman",
                "release_date": 1989,
                "main_character":"Batman"
            },
            {
                "name":"Dumb and dumber",
                "release_date": 1994,
                "main_character":"Harry and Lloyd"
            },
            {
                "name":"Megamind",
                "release_date":2010,
                "main_character":"Megamind"
            },
            {
                "name":"Good Burger",
                "release_date": 1997,
                "main_character":"Ed and Dexter"
            }
            
        ]
        for Movie_Data in Movies_Data:
            models.add_movie(
                Movie_Data["name"],
                Movie_Data["release_date"],
                Movie_Data["main_character"]
            )
        self.assertEqual(len(models.view_by_date(1989)), 1)