from pathlib import Path
from os import path

from constants import Source
from scraper import MangaScraper

RESOURCE_PATH = path.join(path.dirname(__file__), "res")


def test_get_popular_mangas():
    markup = Path(path.join(RESOURCE_PATH, "manga_home.html")).read_text(encoding="utf-8")

    scraper = MangaScraper(Source.MANGAKAKALOT)
    mangas = scraper.home.get_popular_mangas(markup)
    print(len(mangas))
    

if __name__ == "__main__":
    test_get_popular_mangas()


