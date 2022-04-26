class Country:
    def __init__(
        self,
        name,
        alpha2,
        alpha3,
        numeric,
        capital,
        area,
        population,
        continent,
        languages,
    ):
        self.name = name
        self.alpha2 = alpha2
        self.alpha3 = alpha3
        self.numeric = numeric
        self.capital = capital
        self.area = area
        self.population = population
        self.continent = continent
        self.languages = languages

    def __str__(self):
        return (
            self.name
            + ", "
            + self.alpha2
            + ", "
            + self.alpha3
            + ", "
            + self.numeric
            + ", "
            + self.capital
            + ", "
            + self.area
            + ", "
            + self.population
            + ", "
            + self.continent
            + ", "
            + self.languages
        )
