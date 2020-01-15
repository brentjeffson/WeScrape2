class Source:
    MANGAKAKALOT = 'https://mangakakalot.com'
    LEVIATANSCANS = 'https://leviatanscans.com'
    MANGANELO = "https://manganelo.com"

class Selector:
    MANGA_URL = 0
    MANGA_IMAGE_URL = 1
    MANGA_TITLE = 2
    MANGA_DESCRIPTION = 3

    CHAPTER_URL = 4
    CHAPTER_TITLE = 5
    CHAPTER_IMAGES = 6

    SEARCHED_URL = 7
    SEARCHED_IMAGE_URL = 8
    SEARCHED_TITLE = 9

    HOME_LATEST_URL = 10
    HOME_LATEST_IMAGE_URL = 11
    HOME_LATEST_TITLE = 12

    HOME_POPULAR_URL = 13
    HOME_POPULAR_IMAGE_URL = 14
    HOME_POPULAR_TITLE = 15


class Pattern:
    MANGA_IMAGE_URL = 0
    CHAPTER_UID = 1

APIS = {
    Source.MANGAKAKALOT: "/search",
    Source.LEVIATANSCANS: "/comics",
    Source.MANGANELO: "/search",
}

REQUIRED_PARAMETERS = {
    Source.LEVIATANSCANS: {"author": "a", "keyword": "query"}
}

PATTERNS = {
    Source.MANGAKAKALOT: {
        Pattern.CHAPTER_UID: r".+[\s\-_]{1}([0-9a-zA-Z.]+)",
    },
    Source.LEVIATANSCANS: {
        Pattern.MANGA_IMAGE_URL: r"\((.+)\)",
        Pattern.CHAPTER_UID: r".+[\s\-_]{1}([0-9a-zA-Z.]+)",
    },
    Source.MANGANELO: {
        Pattern.CHAPTER_UID: r"[\s\-:]*([0-9.]+)[\s\-:]*",
    },
}

KEYWORD_REPLACEMENT = {
    Source.MANGAKAKALOT: "_",
    Source.MANGANELO: "_",
}

SELECTORS = {
    Source.MANGANELO: {
        Selector.MANGA_URL: "div.panel-breadcrumb > a:last-child",
        Selector.MANGA_IMAGE_URL: "div.story-info-left img",
        Selector.MANGA_TITLE: "div.story-info-right > h1",
        Selector.MANGA_DESCRIPTION: "div.panel-story-info-description",
        Selector.CHAPTER_URL: "ul.row-content-chapter > li > a",
        Selector.CHAPTER_TITLE: "ul.row-content-chapter > li > a",
        Selector.CHAPTER_IMAGES: "div.container-chapter-reader img",
        Selector.SEARCHED_URL: "div.search-story-item > a",
        Selector.SEARCHED_IMAGE_URL: "div.search-story-item img.img-loading",
        Selector.SEARCHED_TITLE: "div.search-story-item > div.item-right >  h3 > a",
        Selector.HOME_LATEST_URL: "div.content-homepage-item > div.content-homepage-item-right h3 > a",
        Selector.HOME_LATEST_IMAGE_URL: "div.content-homepage-item a > img.img-loading",
        Selector.HOME_LATEST_TITLE: "div.content-homepage-item > div.content-homepage-item-right h3 > a",
        Selector.HOME_POPULAR_URL: "div > div.item > div > h3 > a",
        Selector.HOME_POPULAR_IMAGE_URL: "div.item > img.img-loading",
        Selector.HOME_POPULAR_TITLE: "div > div.item > div > h3 > a",
    },
    Source.MANGAKAKALOT: {
        Selector.MANGA_URL: "link[rel=\"alternate\"]",
        Selector.MANGA_IMAGE_URL: "div.manga-info-pic > img",
        Selector.MANGA_TITLE: ".manga-info-text > li > h1",
        Selector.MANGA_DESCRIPTION: "div#noidungm",
        Selector.CHAPTER_URL: "div.chapter-list > div.row > span > a",
        Selector.CHAPTER_TITLE: "div.chapter-list > div.row > span > a",
        Selector.CHAPTER_IMAGES: "div.vung-doc img",
        Selector.SEARCHED_URL: "h3.story_name > a",
        Selector.SEARCHED_IMAGE_URL: "div.story_item > a > img",
        Selector.SEARCHED_TITLE: "h3.story_name > a",
        Selector.HOME_LATEST_URL: "div.itemupdate > ul > li > h3 > a",
        Selector.HOME_LATEST_IMAGE_URL: "div.itemupdate > a > img",
        Selector.HOME_LATEST_TITLE: "div.itemupdate > ul > li > h3 > a",
        Selector.HOME_POPULAR_URL: "div.slide-caption > h3 > a",
        Selector.HOME_POPULAR_IMAGE_URL: "div.item > img",
        Selector.HOME_POPULAR_TITLE: "div.slide-caption > h3 > a",
    },
    Source.LEVIATANSCANS: {
        Selector.MANGA_URL: "a.media-content",
        Selector.MANGA_IMAGE_URL: "a.media-content",
        Selector.MANGA_TITLE: "div.d-flex > div.heading > h5",
        Selector.MANGA_DESCRIPTION: "div.row > div:nth-of-type(2)",
        Selector.CHAPTER_URL: "div.list div.flex > a:nth-of-type(1)",
        Selector.CHAPTER_TITLE: "div.list div.flex > a:nth-of-type(1)",
        Selector.CHAPTER_IMAGES: "div.vung-doc img",
        Selector.SEARCHED_URL: "div.media.media-comic-card + div.list-content a.list-title",
        Selector.SEARCHED_IMAGE_URL: "div.media.media-comic-card > a",
        Selector.SEARCHED_TITLE: "div.list-content > div.list-body > a",
        Selector.HOME_LATEST_URL: "div.list-body > a",
        Selector.HOME_LATEST_IMAGE_URL: "div.media.media-comic-card > a",
        Selector.HOME_LATEST_TITLE: "div.list-body > a",
        Selector.HOME_POPULAR_URL: "div.list-body > a",
        Selector.HOME_POPULAR_IMAGE_URL: "div.media.media-comic-card > a",
        Selector.HOME_POPULAR_TITLE: "div.list-body > a",
    },
}
