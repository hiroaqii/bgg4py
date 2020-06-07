from collections import OrderedDict
from typing import List
from .bgg import Bgg


class Thread(Bgg):
    id: int
    subject: str
    author: str
    numarticles: int
    postdate: str
    lastpostdate: str


class Forum(Bgg):
    id: int
    title: str
    numthreads: int
    numposts: int
    lastpostdate: str
    noposting: int
    threads: List[Thread]

    @classmethod
    def create(cls, forum: OrderedDict):

        if type(forum["threads"]["thread"]) == list:
            lst = forum["threads"]["thread"]
        else:
            lst = [forum["threads"]["thread"]]

        threads = []
        for i in lst:
            thread = Thread(
                id=int(i["@id"]),
                subject=i["@subject"],
                author=i["@author"],
                numarticles=int(i["@numarticles"]),
                postdate=i["@postdate"],
                lastpostdate=i["@lastpostdate"],
            )
            threads.append(thread)

        return Forum(
            id=int(forum["@id"]),
            title=forum["@title"],
            numthreads=int(forum["@numthreads"]),
            numposts=int(forum["@numposts"]),
            lastpostdate=forum["@lastpostdate"],
            noposting=int(forum["@noposting"]),
            threads=threads,
        )
