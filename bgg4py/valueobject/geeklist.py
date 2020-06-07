from typing import List, Optional
from collections import OrderedDict
from .bgg import Bgg


class Item(Bgg):
    id: int
    objecttype: str
    subtype: str
    objectid: int
    objectname: str
    username: str
    postdate: str
    editdate: str
    thumbs: int
    imageid: int
    body: Optional[str]

    @classmethod
    def create(cls, item: OrderedDict):
        _item = Item(
            id=Bgg.parse_int(item.get("@id")),
            objecttype=item.get("@objecttype"),
            subtype=item.get("@subtype"),
            objectid=item.get("@objectid"),
            objectname=item.get("@objectname"),
            username=item.get("@username"),
            postdate=item.get("@postdate"),
            editdate=item.get("@editdate"),
            thumbs=Bgg.parse_int(item.get("@thumbs")),
            imageid=Bgg.parse_int(item.get("@imageid")),
            body=item.get("body"),
        )

        return _item


class GeekList(Bgg):
    id: int
    postdate: str
    postdate_timestamp: int
    editdate: str
    editdate_timestamp: int
    thumbs: str
    numitems: str
    username: str
    title: str
    description: str
    item: List[Item]

    @classmethod
    def create(cls, geekList: OrderedDict):

        if type(geekList.get("item")) == OrderedDict:
            items = [geekList.get("item")]
        else:
            items = geekList.get("item")

        _items = [Item.create(item) for item in items]

        return GeekList(
            id=Bgg.parse_int(geekList.get("@id")),
            postdate=geekList.get("postdate"),
            postdate_timestamp=Bgg.parse_int(geekList.get("postdate_timestamp")),
            editdate=geekList.get("editdate"),
            editdate_timestamp=Bgg.parse_int(geekList.get("editdate_timestamp")),
            thumbs=Bgg.parse_int(geekList.get("thumbs")),
            numitems=Bgg.parse_int(geekList.get("numitems")),
            username=geekList.get("username"),
            title=geekList.get("title"),
            description=geekList.get("description"),
            item=_items,
        )
