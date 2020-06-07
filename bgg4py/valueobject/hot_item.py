from collections import OrderedDict
from typing import List, Optional, Union
from .bgg import Bgg


class Item(Bgg):
    id: int
    rank: int
    name: str
    yearpublished: Optional[int]
    thumbnail: str

    @classmethod
    def create(cls, item: OrderedDict):
        _item = Item(
            id=Bgg.parse_int(item.get("@id")),
            rank=Bgg.parse_int(item.get("@rank")),
            name=Bgg.get_primary_name(item.get("name")),
            yearpublished=Bgg.dict_value_to_int(item.get("yearpublished")),
            thumbnail=item.get("thumbnail", {}).get("@value"),
        )
        return _item


class HotItem(Bgg):

    items: List[Item]

    @classmethod
    def create(cls, items: Union[OrderedDict, List[OrderedDict]]):

        if type(items) == OrderedDict:
            items = [items]

        _items = [Item.create(item) for item in items]

        return HotItem(items=_items)
