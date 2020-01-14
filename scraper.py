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
        self._markup = ""

    @staticmethod
    def parse(markup, parser="html.parser"):
        return BeautifulSoup(markup, parser)

    @staticmethod
    def get_mangas(soup, selectors, patterns, source, location):
        locator = {
            "latest": [
                Selector.HOME_LATEST_URL,
                Selector.HOME_LATEST_IMAGE_URL,
                Selector.HOME_LATEST_TITLE,
            ],
            "popular": [
                Selector.HOME_POPULAR_URL,
                Selector.HOME_POPULAR_IMAGE_URL,
                Selector.HOME_POPULAR_TITLE,
            ],
            "search": [
                Selector.SEARCHED_URL,
                Selector.SEARCHED_IMAGE_URL,
                Selector.SEARCHED_TITLE,
            ],
        }

        url_selector = selectors[locator[location][0]]
        image_url_selector = selectors[locator[location][1]]
        title_selector = selectors[locator[location][2]]

        url_tags = soup.select(url_selector)
        image_url_tags = soup.select(image_url_selector)
        title_tags = soup.select(title_selector)

        mangas = []
        for i in range(len(url_tags)):
            url = url_tags[i]["href"]
            title = title_tags[i].text.strip()

            if image_url_tags[i].name == "a":
                match = re.search(patterns[Pattern.MANGA_IMAGE_URL], str(image_url_tags[i]))
                image_url = match.groups()[0]

                if source not in image_url:
                    if not image_url[0] == '/':
                        image_url = '/' + image_url
                    image_url = source + image_url
            else:
                image_url = image_url_tags[i]["src"]

            manga = Manga(url, image_url, title)
            mangas.append(manga)

        return mangas

    @staticmethod
    def get_manga(soup, selectors, patterns, source):
        murl = soup.select(selectors[Selector.MANGA_URL])[0]["href"]
        mtitle = soup.select(selectors[Selector.MANGA_TITLE])[0].text.strip()
        mdescription = soup.select(selectors[Selector.MANGA_DESCRIPTION])[0].text
        mimage_url_tag = soup.select(selectors[Selector.MANGA_IMAGE_URL])[0]

        if mimage_url_tag.name == "a":
            match = re.search(PATTERNS[source][Pattern.MANGA_IMAGE_URL], str(mimage_url_tag))
            mimage_url = match.groups()[0]
            if source not in mimage_url:
                if not mimage_url[0] == '/':
                    mimage_url = '/' + mimage_url
                mimage_url = source + mimage_url
        else:
            mimage_url = soup.select(selectors[Selector.MANGA_IMAGE_URL])[0]["src"]

        chapters = []
        chapter_url_tags = soup.select(selectors[Selector.CHAPTER_URL])
        chapter_title_tags = soup.select(selectors[Selector.CHAPTER_TITLE])
        for i in range(len(chapter_url_tags)):
            curl = chapter_url_tags[i]["href"]
            ctitle = chapter_title_tags[i].text.strip()
            match = re.search(patterns[Pattern.CHAPTER_UID], ctitle)
            cuid = match.groups()[0]

            chapter = Chapter(cuid, curl, ctitle)
            chapters.append(chapter)

        info = Info(description=mdescription)
        return Manga(murl, mimage_url, mtitle, chapters=chapters, info=info)

    @property
    def manga(self):
        soup = self.parse(self.markup)
        return self.get_manga(soup, self.selectors, self.patterns, self.source)

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
    def latest(self):
        soup = self.parse(self.markup)
        return self.get_mangas(soup, self.selectors, self.patterns, self.source, "latest")

    @property
    def popular(self):
        soup = self.parse(self.markup)
        return self.get_mangas(soup, self.selectors, self.patterns, self.source, "popular")

    @property
    def search(self):
        soup = self.parse(self.markup)
        return self.get_mangas(soup, self.selectors, self.patterns, self.source, "search")

    @property
    def markup(self):
        return self._markup

    @markup.setter
    def markup(self, markup):
        self._markup = markup
