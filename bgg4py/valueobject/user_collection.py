from collections import OrderedDict
from typing import List, Optional
from .bgg import Bgg


class Status(Bgg):
    own: int
    prevowned: int
    fortrade: str
    want: int
    wanttoplay: int
    wanttobuy: int
    wishlist: int
    preordered: int
    lastmodified: str


class Item(Bgg):
    objecttype: str
    objectid: int
    collid: int
    name: str
    yearpublished: Optional[int]
    image: Optional[str]
    thumbnail: Optional[str]
    numplays: Optional[int]
    comment: Optional[str]
    status: Status


class UserCollection(Bgg):

    item_list: List[Item]

    @classmethod
    def create(cls, items: OrderedDict):
        item_list = []
        for item in items:
            sts = item["status"]
            status = Status(
                own=int(sts["@own"]),
                prevowned=int(sts["@prevowned"]),
                fortrade=int(sts["@fortrade"]),
                want=int(sts["@want"]),
                wanttoplay=int(sts["@wanttoplay"]),
                wanttobuy=int(sts["@wanttobuy"]),
                wishlist=int(sts["@wishlist"]),
                preordered=int(sts["@preordered"]),
                lastmodified=sts["@lastmodified"],
            )

            itm = Item(
                objecttype=item["@objecttype"],
                objectid=item["@objectid"],
                collid=item["@collid"],
                name=item["name"]["#text"],
                yearpublished=int(item["yearpublished"]) if item.get("yearpublished") else None,
                image=item.get("image"),
                thumbnail=item.get("thumbnail"),
                numplays=int(item["numplays"]) if item.get("numplays") else None,
                comment=item.get("comment"),
                status=status,
            )
            item_list.append(itm)

        return UserCollection(item_list=item_list)
