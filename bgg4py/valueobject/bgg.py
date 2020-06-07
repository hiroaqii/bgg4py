from collections import OrderedDict
from typing import List, Optional, Union
from pydantic import BaseModel


class Bgg(BaseModel):
    @classmethod
    def parse_int(cls, s: str) -> Optional[int]:
        try:
            n = int(s)
            return n
        except:
            return None

    @classmethod
    def dict_value_to_int(cls, s: Optional[OrderedDict]) -> Optional[int]:
        if s is None:
            return None
        else:
            return cls.parse_int(s.get("@value"))

    @classmethod
    def get_primary_name(cls, name: Union[OrderedDict, List]) -> str:

        if type(name) == OrderedDict:
            return name["@value"]

        for x in name:
            if x.get("@type") == "primary":
                return x["@value"]
