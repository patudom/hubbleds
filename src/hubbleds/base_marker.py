from enum import EnumMeta


class BaseMarker(metaclass=EnumMeta):

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
