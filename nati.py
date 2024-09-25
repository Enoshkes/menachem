from dataclasses import dataclass
from operator import attrgetter

from returns.maybe import Maybe, Nothing, Some


@dataclass
class Person:
    id: int
    name: str

def get_id(person: Person) -> Maybe[int]:
    return Maybe.from_optional(person).map(attrgetter("id"))

def add_if_greater_than10(id: int) -> Maybe[int]:
    return  Nothing if id < 10 else Some(id + 100)

p = Person(id=40, name="enosh")

res = get_id(p).bind(add_if_greater_than10).value_or(0)

# Maybe.map (fn(t) -> r) -> Maybe(fn(t))
# Maybe.bind (fn(t) -> r) -> fn(t)

print(res)