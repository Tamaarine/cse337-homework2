import pytest
import sys, os
sys.path.insert(1, os.getcwd())
from src.movieAnalyzer import pd, get_movies_interval, get_rating_popularity_stats, get_actor_movies_release_year_range, get_actor_median_rating, get_directors_median_reviews, get_movies_data

class TestMovieAnalyzer:
    def setup_method(self):
        self.df = get_movies_data()
    
    def test_get_movie_interval1(self):
        ret = get_movies_interval(1992, 1993)
        
        exp = pd.Series(["Schindler's List", 'Reservoir Dogs', 'Unforgiven', 'Jurassic Park', 'In the Name of the Father', 'Groundhog Day'],
                        index=[5, 88, 131, 141, 177, 205], name="Title")
        
        assert ret.equals(exp)
        assert ret.name == exp.name
    
    def test_get_movie_interval2(self):
        ret = get_movies_interval(2000, 2000)

        exp = pd.Series(['Gladiator', 'Memento', 'Requiem for a Dream', 'Snatch'],
                        index=[36, 52, 81, 113], name="Title")
        
        assert ret.equals(exp)
        assert ret.name == exp.name
    
    def test_get_movie_interval3(self):
        ret = get_movies_interval(2020, 2020)
        
        exp = pd.Series(['Hamilton', 'The Father'],
                        index=[115, 126], name="Title")
        
        assert ret.equals(exp)
        assert ret.name == exp.name
    
    def test_get_movie_interval4(self):
        ret = get_movies_interval(2023, 2023)
        
        exp = pd.Series([], name="Title", dtype=object)
        
        assert ret.equals(exp)
        assert ret.name == exp.name
    
    def test_get_movie_interval5(self):
        with pytest.raises(ValueError):
            ret = get_movies_interval(2025, 2020)
        
    def test_get_stat1(self):
        assert get_rating_popularity_stats("Popularity Index", "count") == "207.00"
    
    def test_get_stat2(self):
        assert get_rating_popularity_stats("Popularity Index", "min") == "3.00"
    
    def test_get_stat3(self):
        assert get_rating_popularity_stats("Popularity Index", "max") == "4940.00"
    
    def test_get_stat4(self):
        assert get_rating_popularity_stats("Popularity Index", "mean") == "1091.92"
    
    def test_get_stat5(self):
        assert get_rating_popularity_stats("Popularity Index", "median") == "673.00"
    
    def test_get_stat6(self):
        assert get_rating_popularity_stats("Rating", "count") == "207.00"
    
    def test_get_stat7(self):
        assert get_rating_popularity_stats("Rating", "min") == "8.10"
    
    def test_get_stat8(self):
        assert get_rating_popularity_stats("Rating", "max") == "9.30"
    
    def test_get_stat9(self):
        assert get_rating_popularity_stats("Rating", "mean") == "8.34"
    
    def test_get_stat10(self):
        assert get_rating_popularity_stats("Rating", "median") == "8.30"
    
    def test_get_stat11(self):
        assert get_rating_popularity_stats("Ratingx", "median") == "Invalid index or type"
    
    def test_get_stat12(self):
        assert get_rating_popularity_stats("Rating", "hehe") == "Invalid index or type"
    
    def test_get_stat13(self):
        assert get_rating_popularity_stats("Ratingx", "hehe") == "Invalid index or type"
    
    def test_get_actor_movies1(self):
        ret = get_actor_movies_release_year_range("Tom Hanks", 2010, 2010)
        
        exp = pd.Series([2010], index=["Toy Story 3"])
        
        assert ret.equals(exp)
        
    def test_get_actor_movies2(self):
        ret = get_actor_movies_release_year_range("Tom Hanks", 2010)
        
        exp = pd.Series([1994, 1998, 1999, 1995, 2010, 2002], index=["Forrest Gump", "Saving Private Ryan", "The Green Mile", "Toy Story", "Toy Story 3", "Catch Me If You Can"])

        assert ret.equals(exp)
    
    def test_get_actor_movies3(self):
        ret = get_actor_movies_release_year_range("Tom Hanks", 2022, 2011)
        
        exp = pd.Series([], dtype="int64")
        
        assert ret.equals(exp)
    
    def test_get_actor_movies4(self):
        ret = get_actor_movies_release_year_range("Jürgen Prochnow", 1999)
        
        exp = pd.Series([1981], index=["The Boat"])

        assert ret.equals(exp)
    
    def test_get_actor_movies5(self):
        with pytest.raises(ValueError):
            ret = get_actor_movies_release_year_range("Tom Hanks", 2011, 2022)
    
    def test_get_actor_movies6(self):
        ret = get_actor_movies_release_year_range("a", 1999)
        
        exp = pd.Series([], dtype="int64")

        assert ret.equals(exp)
      
    def test_get_actor_median_rating1(self):
        assert get_actor_median_rating("Dean-Charles Chapman") == 8.2
    
    def test_get_actor_median_rating2(self):
        assert get_actor_median_rating("Lin-Manuel Miranda") == 8.3
    
    def test_get_actor_median_rating3(self):
        with pytest.raises(ValueError):
            get_actor_median_rating("")
    
    def test_get_actor_median_rating4(self):
        with pytest.raises(TypeError):
            get_actor_median_rating(1)
    
    def test_get_actor_median_rating5(self):
        assert get_actor_median_rating("Ricky Lu") == None
    
    def test_get_actor_median_rating6(self):
        assert get_actor_median_rating("a") == None
    
    def test_get_directors_median_reviews(self):
        exp = pd.Series([0.19, 0.124, 0.397, 1.05, 1.05, 0.243, 0.179, 0.502, 0.468, 0.714, 0.819, 1.1, 0.17, 0.239, 1.7, 0.679, 0.575, \
        0.822, 0.195, 0.149, 0.678, 0.827, 1.6, 0.254, 0.238, 0.855, 0.726, 0.432, 0.076, 0.154, 0.95, 0.746, 0.385, 0.14, 1.2, \
        0.448, 1.95, 0.164, 0.466, 1.3, 0.978, 0.259, 0.257, 0.66, 0.946, 0.708, 0.62, 0.385, 0.183, 1.3, 0.27, 0.849, 0.557, \
        1.1, 0.747, 0.173, 0.732, 0.414, 0.565, 0.124, 0.973, 0.863, 0.242, 0.679, 1.4, 0.233, 0.13, 0.208, 1.9, 0.654, \
        0.413, 1.1, 0.976, 0.256, 0.495, 1.1, 0.055, 0.754, 0.336, 0.563, 0.64, 0.988, 0.693, 0.086, 0.185, 0.352, \
        0.409, 0.839, 0.437, 0.567, 0.575, 0.891, 0.471, 1.8, 0.739, 1.4, 0.39, 0.281, 1.0, 0.861, 0.397, 0.313, \
        1.6, 0.682, 1.0, 0.567, 0.695, 0.83, 0.616, 0.336, 0.144, 0.464, 0.239, 0.077, 0.657, 0.691, 0.951, \
        0.353, 0.535, 0.09, 0.323, 1.2, 0.463, 1.1, 0.353, 0.79, 0.237, 0.248], index = ['Aamir Khan', 'Akira Kurosawa', 'Alfred Hitchcock', \
        'Andrew Stanton', 'Anthony Russo', 'Asghar Farhadi', 'Billy Wilder', 'Bob Persichetti', \
        'Bong Joon Ho', 'Brad Bird', 'Brian De Palma', 'Bryan Singer', 'Carol Reed', 'Charles Chaplin', 'Christopher Nolan', \
        'Clint Eastwood', 'Curtis Hanson', 'Damien Chazelle', 'Damián Szifron', 'Dan Kwan', 'Danny Boyle', 'Darren Aronofsky',\
        'David Fincher', 'David Lean', 'David Lynch', 'David Yates', 'Dean DeBlois', 'Denis Villeneuve', 'Elem Klimov' \
        , 'Elia Kazan', 'Ethan Coen', 'Fernando Meirelles', 'Florian Henckel von Donnersmarck', 'Florian Zeller', \
        'Francis Ford Coppola', 'Frank Capra', 'Frank Darabont', 'Fritz Lang', "Gavin O'Connor", 'George Lucas', \
        'George Miller', 'George Roy Hill', 'Giuseppe Tornatore', 'Guillermo del Toro', 'Gus Van Sant', 'Guy Ritchie', \
        'Harold Ramis', 'Hayao Miyazaki', 'Ingmar Bergman', 'Irvin Kershner', 'Isao Takahata', 'James Cameron', \
        'James Mangold', 'James McTeigue', 'Jean-Pierre Jeunet', 'Jim Sheridan', 'Joel Coen', 'John Carpenter', \
        'John G. Avildsen', 'John Huston', 'John Lasseter', 'John McTiernan', 'John Sturges', 'Jon Watts', \
        'Jonathan Demme', 'Joseph Kosinski', 'Joseph L. Mankiewicz', 'Juan José Campanella', 'Lana Wachowski', \
        'Lee Unkrich', 'Lenny Abrahamson', 'Luc Besson', 'M. Night Shyamalan', 'Makoto Shinkai', 'Martin McDonagh', \
        'Martin Scorsese', 'Masaki Kobayashi', 'Mel Gibson', 'Michael Cimino', 'Michael Curtiz', 'Michael Mann', \
        'Michel Gondry', 'Milos Forman', 'Nadine Labaki', 'Nitesh Tiwari', 'Oliver Hirschbiegel', 'Oliver Stone', \
        'Olivier Nakache', 'Orson Welles', 'Park Chan-wook', 'Paul Thomas Anderson', 'Pete Docter', 'Peter Farrelly', \
        'Peter Jackson', 'Peter Weir', 'Quentin Tarantino', 'Rajkumar Hirani', 'Richard Linklater', 'Richard Marquand', \
        'Ridley Scott', 'Rob Reiner', 'Robert Mulligan', 'Robert Zemeckis', 'Roberto Benigni', 'Roger Allers', \
        'Roman Polanski', 'Ron Howard', 'Sam Mendes', 'Sean Penn', 'Sergio Leone', 'Sergio Pablos', 'Sidney Lumet',\
        'Stanley Donen', 'Stanley Kramer', 'Stanley Kubrick', 'Steve McQueen', 'Steven Spielberg', 'Terry George', \
        'Terry Gilliam', 'Thomas Kail', 'Thomas Vinterberg', 'Todd Phillips', 'Tom McCarthy', 'Tony Kaye', \
        'Victor Fleming', 'Wes Anderson', 'William Wyler', 'Wolfgang Petersen'])
        
        assert get_directors_median_reviews().round(3).equals(exp)