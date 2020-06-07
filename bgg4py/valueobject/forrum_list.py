from collections import OrderedDict
from typing import List, Union
from .bgg import Bgg


class Forum(Bgg):
    id: int
    groupid: int
    title: str
    noposting: int
    description: str
    numthreads: int
    numposts: int
    lastpostdate: str


class ForumList(Bgg):
    type: str
    id: int
    forums: List[Forum]

    @classmethod
    def create(cls, forums: OrderedDict):
        if type(forums["forum"]) == OrderedDict:
            # TODO
            lst = forums["forum"]
        else:
            lst = forums["forum"]

        ret = []
        for i in lst:
            forum = Forum(
                id=int(i["@id"]),
                groupid=int(i["@groupid"]),
                title=i["@title"],
                noposting=int(i["@noposting"]),
                description=i["@description"],
                numthreads=int(i["@numthreads"]),
                numposts=int(i["@numposts"]),
                lastpostdate=i["@lastpostdate"],
            )
            ret.append(forum)

        return ForumList(type=forums["@type"], id=int(forums["@id"]), forums=ret)
