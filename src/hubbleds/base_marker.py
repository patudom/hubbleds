from enum import EnumMeta
from functools import total_ordering

@total_ordering
class BaseMarker(metaclass=EnumMeta):
    
    def __lt__(self, other):
        if type(other) is type(self):
            return self.value < other.value
        return NotImplemented

    def __gt__(self, other):
        if type(other) is type(self):
            return self.value > other.value
        return NotImplemented

    # We don't want to just do e.g. `not self.__lt__(other)` because __lt__ might return NotImplemented.
    # NotImplemented is truthy so `not NotImplemented` is False (with a `DeprecationWarning`)
    # but I think we want to actually return NotImplemented (for consistency with above)
    # and not a coerced boolean
    def __ge__(self, other):
        if type(other) is type(self):
            return self.value >= other.value
        return NotImplemented

    def __le__(self, other):
        if type(other) is type(self):
            return self.value <= other.value
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
    
    def is_between(self, start: 'BaseMarker', end: 'BaseMarker'):
        return start.value <= self.value <= end.value

    @classmethod
    # Check if the given marker is at the specified marker or earlier.
    def is_at_or_before(cls, marker: 'BaseMarker', end: 'BaseMarker'):
        return marker.value <= end.value
