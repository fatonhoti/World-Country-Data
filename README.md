# 🗺️World-Country-Data-Scraper
This is a simple script that collects country information from [geonames.org/countries](https://www.geonames.org/countries/) using the Python library [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and generates a nicely formatted JSON file of it.

```
[
    ...
    {
        "alpha2": "XK",
        "alpha3": "XKX",
        "area": "10,908.0",
        "capital": "Pristina",
        "continent": "EU",
        "languages": "Albanian (sq), Serbian (sr)",
        "name": "Kosovo",
        "numeric": "0",
        "population": "1,845,300"
    },
    {
        "alpha2": "YE",
        "alpha3": "YEM",
        "area": "527,970.0",
        "capital": "Sanaa",
        "continent": "AS",
        "languages": "Arabic (ar-YE)",
        "name": "Yemen",
        "numeric": "887",
        "population": "28,498,687"
    },
    ...
]
```
To use simply install the required Python libraries by running `pip install -r requirements.txt` and then run the script `python main.py`.
