from enum import EnumMeta
from functools import total_ordering

@total_ordering
class BaseMarker(metaclass=EnumMeta):
    
    # enums already have an __eq__ dunder method, 
    # so only need to add one comparison
    def __lt__(self, other):
        if type(other) is type(self):
            return self.value < other.value
        return NotImplemented
    

    @classmethod
    def next(cls, step):
        return cls(step.value + 1)

    @classmethod
    def previous(cls, step):
        return cls(step.value - 1)

    @classmethod
    def first(cls):
        return cls(1)

    @classmethod
    def last(cls):
        return cls(len(cls))
    
    @classmethod
    def is_on(cls, marker: 'BaseMarker', is_on: 'BaseMarker'):
        return marker.value is is_on.value

    @staticmethod
    def is_between(marker: 'BaseMarker', start: 'BaseMarker', end: 'BaseMarker'):
        return start.value <= marker.value <= end.value

    @classmethod
    # Check if the given marker is at the specified marker or earlier.
    def is_at_or_before(cls, marker: 'BaseMarker', end: 'BaseMarker'):
        return marker.value <= end.value

    @classmethod
    # Check if the given marker is at the specified marker or later.
    def is_at_or_after(cls, marker: 'BaseMarker', start: 'BaseMarker'):
        return marker.value >= start.value
