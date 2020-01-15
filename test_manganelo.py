from constants import Source
from scraper import MangaScraper

class TestFunctions:

    def test_online_search(self):
        scraper = MangaScraper(Source.MANGANELO)
        mangas = scraper.search_online("i am")
        manga = mangas[0]

        assert len(mangas) == 20
        assert manga.title == "Tales Of Demons And Gods"
        assert manga.url == "https://manganelo.com/manga/hyer5231574354229"
        assert manga.image_url == "https://avt.mkklcdnv3.com/avatar_225/464-tales_of_demons_and_gods.jpg"

