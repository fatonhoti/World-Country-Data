import json
import threading
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


def fetch(*args):
    countries = args[0]
    result = args[1]
    me = args[2]
    cs = []
    for tr in countries:
        tds = tr.find_all("td")
        name = tds[NAME].a.text
        print("=> Currently fetching data for: " + name)
        alpha2 = tds[ALPHA2].text
        alpha3 = tds[ALPHA3].text
        numeric = tds[NUMERIC].text
        languages = getLanguages(tds[NAME].a.get("href"))
        capital = tds[CAPITAL].text
        area = tds[AREA].text
        population = tds[POPULATION].text
        continent = tds[CONTINENT].text
        cs.append(
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
    print(f"{me} done!")
    result.append(cs)


def run():
    countries = []
    html_doc = download(default_url + "/countries/")
    soup = BeautifulSoup(html_doc, "html.parser")
    table = soup.find(id="countries")
    table_rows = table.find_all("tr")

    split = (len(table_rows) - 1) // 2
    t1 = table_rows[1:split]
    t2 = table_rows[split:]
    r1 = threading.Thread(target=fetch, args=(t1, countries, "Worker 1"))
    r2 = threading.Thread(target=fetch, args=(t2, countries, "Worker 2"))
    r1.start()
    r2.start()
    r1.join()
    r2.join()
    countries = countries[0] + countries[1]

    # Generate the JSON file
    json_string = json.dumps(
        countries, default=lambda o: o.__dict__, sort_keys=True, indent=4
    )
    with open("countries.json", "w") as f:
        f.write(json_string)

    print("\n\n=> All done! :)")


if __name__ == "__main__":
    run()
