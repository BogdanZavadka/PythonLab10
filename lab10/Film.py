class Film:
    def __init__(self, name: str, year: int, duration_in_minutes: int, genre: str, studio: str):
        self.name = name
        self.year = year
        self.durations_in_minutes = duration_in_minutes
        self.genre = genre
        self. studio = studio

    def __str__(self):
        return f'Name: {self.name}, year: {self.year}, duration in minutes: {self.durations_in_minutes},' \
               f' genre: {self.genre}, studio: {self.studio}'
