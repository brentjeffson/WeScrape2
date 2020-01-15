from constants import Source
from scraper import MangaScraper
from pathlib import Path
from os import path
import requests

RESOURCE_PATH = path.join(path.dirname(__file__), "res")

def resource(filename):
    return path.join(RESOURCE_PATH, filename)

class TestFunctions:
    def test_online_search(self):
        scraper = MangaScraper(Source.MANGANELO)
        mangas = scraper.search_online("i am")
        manga = mangas[0]

        assert len(mangas) == 20
        assert manga.title == "Tales Of Demons And Gods"
        assert manga.url == "https://manganelo.com/manga/hyer5231574354229"
        assert manga.image_url == "https://avt.mkklcdnv3.com/avatar_225/464-tales_of_demons_and_gods.jpg"

    def test_getting_information_from_manga_item(self):
        markup = Path(resource("manganelo_item.html")).read_text(encoding="utf-8")
        scraper = MangaScraper(Source.MANGANELO)
        scraper.markup = markup
        
        manga = scraper.manga

        assert manga.size == 435
        assert manga.title == "Tales Of Demons And Gods"
        assert manga.image_url == "https://avt.mkklcdnv3.com/avatar_225/464-tales_of_demons_and_gods.jpg"
        
        chapter_275_5 = manga.chapters[0]
        assert chapter_275_5.title == "Chapter 275.5"
        assert chapter_275_5.uid == "275.5"
        assert chapter_275_5.url == "https://manganelo.com/chapter/hyer5231574354229/chapter_275.5"

        chapter_257 = manga.chapters[1]
        assert chapter_257.title == "Chapter 257"
        assert chapter_257.uid == "257"
        assert chapter_257.url == "https://manganelo.com/chapter/hyer5231574354229/chapter_257"

    def test_getting_popular_mangas(self):
        markup = Path(resource("manganelo_home.html")).read_text(encoding="utf-8")
        scraper = MangaScraper(Source.MANGANELO)
        scraper.markup = markup
        
        mangas = scraper.popular
        manga = mangas[0]

        print(manga.url)
        print(manga.title)
        print(manga.image_url)

        assert len(mangas) == 25
        assert manga.url == "https://manganelo.com/manga/hyer5231574354229"
        assert manga.title == "Tales Of Demons And Gods"
        assert manga.image_url == "https://avt.mkklcdnv3.com/avatar_225/464-tales_of_demons_and_gods.jpg"

    def test_getting_latest_mangas(self):
        markup = Path(resource("manganelo_home.html")).read_text(encoding="utf-8")
        scraper = MangaScraper(Source.MANGANELO)
        scraper.markup = markup
        
        mangas = scraper.latest
        manga = mangas[0]

        assert len(mangas) == 56
        assert manga.url == "https://manganelo.com/manga/gr921840"
        assert manga.title == "Eromanga-Sensei: Yamada Elf-Daisensei No Koi Suru Junshin Gohan"
        assert manga.image_url == "https://www.upsieutoc.com/images/2020/01/15/186d0005283f8449e.jpg"