class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def info(self):
        print(f"{self.title} ({self.year}) {self.author}. {self.pages} старонак.")

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @classmethod
    def from_string(cls, string):
        title, author, year, pages = string.split(",")
        return cls(title.strip(), author.strip(), int(year.strip()), int(pages.strip()))