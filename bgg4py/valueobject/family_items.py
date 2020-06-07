from collections import OrderedDict
from typing import List, Optional, Union
from .bgg import Bgg


class Link(Bgg):
    type: str
    id: int
    value: str


class Item(Bgg):
    id: int
    type: str
    name: str
    description: Optional[str]
    thumbnail: Optional[str]
    image: Optional[str]
    links: Optional[List[Link]]


class FamilyItem(Bgg):
    items: List[Item]

    @classmethod
    def create(cls, items: Union[OrderedDict, List[OrderedDict]]):
        if type(items) == OrderedDict:
            lst = [items]
        else:
            lst = items

        _items = []
        for i in lst:
            _link = i.get("link")
            if type(_link) == OrderedDict:
                links = [_link]
            else:
                links = _link

            name = i.get("name")
            if type(name) == OrderedDict:
                name = name.get("@value")
            elif type(name) == list:
                name = name[0].get("@value")

            _links = [Link(type=j["@type"], id=j["@id"], value=j["@value"]) for j in links]
            _item = Item(
                id=int(i["@id"]),
                type=i["@type"],
                name=name,
                description=i.get("description"),
                thumbnail=i.get("thumbnail"),
                image=i.get("image"),
                links=_links,
            )
            _items.append(_item)
        return FamilyItem(items=_items)
