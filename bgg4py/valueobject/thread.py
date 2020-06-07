from collections import OrderedDict
from typing import Dict, List, Optional
from .bgg import Bgg


class Article(Bgg):
    id: int
    username: str
    link: str
    postdate: str
    editdate: str
    numedits: int
    subject: str
    body: str

    @classmethod
    def create(cls, article: OrderedDict):
        return Article(
            id=Bgg.parse_int(article.get("@id")),
            username=article.get("@username"),
            link=article.get("@link"),
            postdate=article.get("@postdate"),
            editdate=article.get("@editdate"),
            numedits=Bgg.parse_int(article.get("@numedits")),
            subject=article.get("subject"),
            body=article.get("body"),
        )


class Thread(Bgg):
    id: int
    numarticles: int
    link: str
    subject: str
    articles: List[Article]

    @classmethod
    def create(cls, thread: OrderedDict):

        articles = thread.get("articles", {}).get("article", [])
        _articles = [Article.create(article) for article in articles]

        return Thread(
            id=Bgg.parse_int(thread.get("@id")),
            numarticles=Bgg.parse_int(thread.get("@numarticles")),
            link=thread.get("@link"),
            subject=thread.get("subject"),
            articles=_articles,
        )
