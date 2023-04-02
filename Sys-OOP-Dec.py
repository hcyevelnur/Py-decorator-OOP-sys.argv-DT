class Movie:
    def __init__(self, name, director, year, genre, imdb):
        self.name = name
        self.director = director
        self.year = year
        self.genre = genre
        self.imdb = imdb

    def __str__(self):
        return f"{self.name} ({self.year})"

    def year_info(self):
        try:
            year = int(self.year)
        except ValueError:
            return "Invalid year"
        if year < 2000:
            return "Old"
        else:
            return "New"

    def rating_info(self):
        try:
            rating = float(self.imdb)
        except ValueError:
            return "Invalid rating"
        if rating < 6:
            return "E"
        elif 6 <= rating < 7:
            return "D"
        elif 7 <= rating < 8:
            return "C"
        elif 8 <= rating < 9:
            return "B"
        elif 9 <= rating <= 10:
            return "A"
        else:
            return "Invalid rating"


class Series(Movie):
    def __init__(self, name, director, year, genre, imdb, seasons, episodes):
        super().__init__(name, director, year, genre, imdb)
        self.seasons = seasons
        self.episodes = episodes

    def season_info(self):
        try:
            seasons = int(self.seasons)
        except ValueError:
            return "Invalid number of seasons"
        if seasons < 3:
            return "Short"
        else:
            return "Long"


movie1 = Movie("The Godfather", "Francis Ford Coppola", "1972", "Crime, Drama", "9.2")
print(movie1)  
print(movie1.year_info())
print(movie1.rating_info())

series1 = Series("Game of Thrones", "David Benioff, D. B. Weiss", "2011-2019", "Adventure, Drama, Fantasy", "9.3", "8", "73")
print(series1) 
print(series1.year_info())  
print(series1.rating_info())
print(series1.season_info()) 
