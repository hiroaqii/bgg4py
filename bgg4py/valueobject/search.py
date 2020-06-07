from collections import OrderedDict
from typing import List, Optional, Union
from .bgg import Bgg


class Item(Bgg):
    id: int
    type: str
    name: Optional[str]
    yearpublished: Optional[int]

    @classmethod
    def create(cls, itme: OrderedDict):
        _item = Item(
            id=Bgg.parse_int(itme.get("@id")),
            type=itme.get("@type"),
            name=Bgg.get_primary_name(itme.get("name")),
            yearpublished=Bgg.parse_int(itme.get("yearpublished", {}).get("@value")),
        )
        return _item


class Search(Bgg):
    items: List[Item]

    @classmethod
    def create(cls, items: Union[OrderedDict, List[OrderedDict]]):

        if items is None:
            return None

        if type(items) == OrderedDict:
            items = [items]

        _items = [Item.create(x) for x in items]
        return Search(items=_items)
