from uuid import UUID


import dataclasses
import typing as ty

from docarray import dataclass
from docarray.typing import Image, Text

@dataclass
class RenguRecord:

    _id: UUID
    _desc: Text | None

@dataclass
class Work(RenguRecord):

    title = _desc

@dataclass
class Fragment(RenguRecord):

    title = _desc


