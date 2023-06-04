import inspect
import types
import typing as t

from rapidfuzz import fuzz
from rapidfuzz import process

_IndexT = t.TypeVar("_IndexT", bound="Index")


class LibraryIndex:
    __slots__ = ("_cache", "_base_name", "_indexed")

    def __init__(self, outer: t.Any) -> None:
        self._base_name = outer.__name__
        self._cache = {}
        self._indexed = set()

        for name, item in inspect.getmembers(outer):
            if name.startswith("_") or name.endswith("_"):
                continue

            if isinstance(item, types.ModuleType) and item.__package__ == self._base_name:
                for name_, item_ in self._expand_module(item):
                    self._cache[name_] = item_
            else:
                self._cache[name] = item

    def _expand_module(self, item: t.Any) -> t.Iterator[t.Tuple[str, t.Any]]:
        base_str = item.__name__[len(self._base_name) + 1:]
        for name, item_ in inspect.getmembers(item):
            if name.startswith("_") or name.endswith("_"):
                continue
            yield f"{base_str}.{name}", item_

    @classmethod
    def generate_for(cls: t.Type[_IndexT], item: t.Any) -> _IndexT:
        return cls(item)
