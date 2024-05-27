from enum import EnumMeta


class MarkerBase():

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
