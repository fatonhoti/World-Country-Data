import json
import urllib.request

from bs4 import BeautifulSoup

from Country import Country

default_url = "https://www.geonames.org"
ALPHA2 = 0
ALPHA3 = 1
NUMERIC = 2
NAME = 4
CAPITAL = 5
AREA = 6
POPULATION = 7
CONTINENT = 8


def download(URL):
    with urllib.request.urlopen(URL) as response:
        return response.read()


def getLanguages(href):
    url = default_url + href
    document = BeautifulSoup(download(url), "html.parser")
    table = document.find_all("table")[1]
    languages_row = table.find_all("tr")[7]
    languages_data_cell = languages_row.find_all("td")[1]
    return str(languages_data_cell)[4:-5].strip()


def run():
    countries = []
    html_doc = download(default_url + "/countries/")
    soup = BeautifulSoup(html_doc, "html.parser")
    table = soup.find(id="countries")
    table_rows = table.find_all("tr")
    for tr in table_rows[1:]:
        tds = tr.find_all("td")
        name = tds[NAME].a.text
        alpha2 = tds[ALPHA2].text
        alpha3 = tds[ALPHA3].text
        numeric = tds[NUMERIC].text
        languages = getLanguages(tds[NAME].a.get("href"))
        capital = tds[CAPITAL].text
        area = tds[AREA].text
        population = tds[POPULATION].text
        continent = tds[CONTINENT].text
        countries.append(
            Country(
                name,
                alpha2,
                alpha3,
                numeric,
                capital,
                area,
                population,
                continent,
                languages,
            )
        )

    json_string = json.dumps(
        countries, default=lambda o: o.__dict__, sort_keys=True, indent=4
    )
    with open("countries.json", "w") as f:
        f.write(json_string)


if __name__ == "__main__":
    run()
