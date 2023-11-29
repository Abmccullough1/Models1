from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.TextField()
    release_date = models.IntegerField()
    main_character = models.TextField()


def add_movie(name,release_date,main_character):
    movie = Movies(name=name,release_date=release_date,main_character=main_character)
    movie.save()
    return movie



def view_All():
    movie = Movies.objects.all()
    return movie

def view_by_date(release_date):
    movie = Movies.objects.filter(release_date=release_date)
    return movie


def view_by_movie_name(movie_name):
    try:
        movie = Movies.objects.get(name=movie_name)
        return movie
    except:
        return None

def update_release(movie_name, new_release):
     movie = Movies.objects.get(name=movie_name)
     movie.release_date = new_release
     movie.save()
     return movie

def delete_movie(movie_name):
    movie = Movies.objects.get(name=movie_name)
    movie.delete()
    return movie