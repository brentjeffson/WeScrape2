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


def test_leviatanscans_get_manga():
    markup = Path(path.join(RESOURCE_PATH, "leviatanscans_item.html")).read_text(encoding="utf-8")

    scraper = MangaScraper(Source.LEVIATANSCANS)
    manga = scraper.get_manga(markup)
    for chapter in manga.chapters:
        print(chapter)


def test_leviatanscans_search_get_manga():
    markup = Path(path.join(RESOURCE_PATH, "leviatanscans_search.html")).read_text(encoding="utf-8")

    scraper = MangaScraper(Source.LEVIATANSCANS)
    mangas = scraper.search.get_searched_mangas(markup)
    for manga in mangas:
        print(manga)

def test_leviatanscans_home_latest_manga():
    markup = Path(path.join(RESOURCE_PATH, "leviatanscans_home.html")).read_text(encoding="utf-8")

    scraper = MangaScraper(Source.LEVIATANSCANS)
    mangas = scraper.home.get_latest_mangas(markup)
    for manga in mangas:
        print(manga)


if __name__ == "__main__":
    test_leviatanscans_home_latest_manga()


