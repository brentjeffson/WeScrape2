from constants import SELECTORS, Selector, PATTERNS, Pattern
from bs4 import BeautifulSoup
import re

class Chapter:
    
    def __init__(self, uid, url, title, images=None):
        self._uid = uid
        self._url = url
        self._title = title
        self._images = images

    def __str__(self):
        return '({0}): {1} - {2}'.format(self.uid, self.title, self.url)

    @property
    def uid(self):
        return self._uid

    @property
    def url(self):
        return self._url

    @property
    def title(self):
        return self._title

    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, images):
        self._images = images

    @property
    def size(self):
        return len(self.images)


class Info:

    def __init__(self, status="", description="", authors=[], alternative_titles=[]):
        self._status = status
        self._description = description
        self._authors = authors
        self._alternative_titles = alternative_titles

    @property
    def status(self):
        return self._status
    
    @property
    def description(self):
        return self._description
    
    @property
    def authors(self):
        return self._authors
    
    @property
    def alternative_titles(self):
        return self._alternative_titles


class Manga:

    def __init__(self, url, image_url, title, chapters=None, info=None):
        self._url = url
        self._image_url = image_url
        self._title = title
        self._chapters = [] if chapters is None else chapters
        self._info = info

    def __str__(self):
        return f"{self.title}({self.size})"

    @property
    def url(self):
        return self._url

    @property
    def image_url(self):
        return self._image_url

    @property
    def title(self):
        return self._title

    @property
    def chapters(self):
        return self._chapters

    @chapters.setter
    def chapters(self, chapters):
        self._chapters = chapters

    @property
    def info(self):
        return self._info

    @property
    def size(self):
        return len(self.chapters)


class MangaScraper:

    def __init__(self, source):
        self._source = source        
        self._selectors = SELECTORS[self.source]
        self._patterns = PATTERNS[self.source]

        self._home = self.Home(self)
        self._search = self.Search(self)

    @staticmethod
    def parse(markup, parser="html.parser"):
        return BeautifulSoup(markup, parser)

    @staticmethod
    def get_mangas(soup, url_selector, image_url_selector, title_selector, image_pattern=None):
        url_tags = soup.select(url_selector)
        image_url_tags = soup.select(image_url_selector)
        title_tags = soup.select(title_selector)

        mangas = []
        for i in range(len(url_tags)):
            url = url_tags[i]["href"]
            title = title_tags[i].text.strip()

            if image_pattern is not None:
                image_url = str(image_url_tags[i])
                match = re.search(image_pattern, image_url)
                image_url = match.groups()[0]
            else:
                image_url = image_url_tags[i]["src"]

            manga = Manga(url, image_url, title)
            mangas.append(manga)

        return mangas

    def get_manga(self, markup):
        soup = self.parse(markup)

        murl = soup.select(self.selectors[Selector.MANGA_URL])[0]["href"]
        mtitle = soup.select(self.selectors[Selector.MANGA_TITLE])[0].text.strip()
        mdescription = soup.select(self.selectors[Selector.MANGA_DESCRIPTION])[0].text
        mimage_url_tag = soup.select(self.selectors[Selector.MANGA_IMAGE_URL])[0]

        if mimage_url_tag.name == "a":
            match = re.search(PATTERNS[self.source][Pattern.MANGA_IMAGE_URL], str(mimage_url_tag))
            mimage_url = match.groups()[0]
            if self.source not in mimage_url:
                if not mimage_url[0] == '/':
                    mimage_url = '/' + mimage_url
                mimage_url = self.source + mimage_url
        else:
            mimage_url = soup.select(self.selectors[Selector.MANGA_IMAGE_URL])[0]["src"]

        chapters = []
        chapter_url_tags = soup.select(self.selectors[Selector.CHAPTER_URL])
        chapter_title_tags = soup.select(self.selectors[Selector.CHAPTER_TITLE])
        for i in range(len(chapter_url_tags)):
            curl = chapter_url_tags[i]["href"]
            ctitle = chapter_title_tags[i].text.strip()
            match = re.search(self.patterns[Pattern.CHAPTER_UID], ctitle)
            cuid = match.groups()[0]

            chapter = Chapter(cuid, curl, ctitle)
            chapters.append(chapter)

        info = Info(description=mdescription)
        return Manga(murl, mimage_url, mtitle, chapters=chapters, info=info)

    @property
    def source(self):
        return self._source
    
    @source.setter
    def source(self, source):
        self._source = source

    @property
    def selectors(self):
        return self._selectors

    @property
    def patterns(self):
        return self._patterns

    @property
    def home(self):
        return self._home

    @property
    def search(self):
        return self._search

    class Home:

        def __init__(self, parent):
            self.parent = parent

        def get_latest_mangas(self, markup):
            soup = self.parent.parse(markup)

            image_pattern = self.parent.patterns[Pattern.MANGA_IMAGE_URL] if self.parent.source in PATTERNS else None

            return self.parent.get_mangas(
                soup, 
                self.parent.selectors[Selector.HOME_LATEST_URL],
                self.parent.selectors[Selector.HOME_LATEST_IMAGE_URL],
                self.parent.selectors[Selector.HOME_LATEST_TITLE],
                image_pattern,
            )

        def get_popular_mangas(self, markup):
            soup = self.parent.parse(markup)

            image_pattern = self.parent.patterns[Pattern.MANGA_IMAGE_URL] if self.parent.source in PATTERNS else None

            return self.parent.get_mangas(
                soup, 
                self.parent.selectors[Selector.HOME_POPULAR_URL],
                self.parent.selectors[Selector.HOME_POPULAR_IMAGE_URL],
                self.parent.selectors[Selector.HOME_POPULAR_TITLE],
                image_pattern
            )

    class Search:

        def __init__(self, parent):
            self.parent = parent

        def get_searched_mangas(self, markup):
            soup = self.parent.parse(markup)

            image_pattern = self.parent.patterns[Pattern.MANGA_IMAGE_URL] if self.parent.source in PATTERNS else None

            return self.parent.get_mangas(
                soup,
                self.parent.selectors[Selector.SEARCHED_URL],
                self.parent.selectors[Selector.SEARCHED_IMAGE_URL],
                self.parent.selectors[Selector.SEARCHED_TITLE],
                image_pattern
            )
