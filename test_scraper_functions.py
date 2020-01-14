from pathlib import Path
from os import path

from constants import Source
from scraper import MangaScraper

RESOURCE_PATH = path.join(path.dirname(__file__), "res")

class TestFunctions:

    def test_get_popular_mangas(self):
        markup = Path(path.join(RESOURCE_PATH, "manga_home.html")).read_text(encoding="utf-8")

        scraper = MangaScraper(Source.MANGAKAKALOT)
        scraper.markup = markup
        mangas = scraper.popular
        print(len(mangas))


    def test_leviatanscans_get_manga(self):
        markup = Path(path.join(RESOURCE_PATH, "leviatanscans_item.html")).read_text(encoding="utf-8")

        scraper = MangaScraper(Source.LEVIATANSCANS)
        scraper.markup = markup
        manga = scraper.manga
        for chapter in manga.chapters:
            print(chapter)


    def test_leviatanscans_search_get_manga(self):
        markup = Path(path.join(RESOURCE_PATH, "leviatanscans_search.html")).read_text(encoding="utf-8")

        scraper = MangaScraper(Source.LEVIATANSCANS)
        scraper.markup = markup
        mangas = scraper.search
        for manga in mangas:
            print(manga)


    def test_leviatanscans_home_latest_manga(self):
        markup = Path(path.join(RESOURCE_PATH, "leviatanscans_home.html")).read_text(encoding="utf-8")

        scraper = MangaScraper(Source.LEVIATANSCANS)
        scraper.markup = markup
        mangas = scraper.latest
        for manga in mangas:
            print(manga)


if __name__ == "__main__":
    TestFunctions().test_leviatanscans_home_latest_manga()


