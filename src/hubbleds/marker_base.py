from enum import EnumMeta


class MarkerBase(metaclass=EnumMeta):

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
    # check if the current_step is inclusively within the start and end markers specified. If no end is specified, use the final marker.
    def incl_range(cls, component_state, start, end=None):
        if end is None:
            end = cls.last()
        return (component_state.current_step.value.value >= start.value and component_state.current_step.value.value <= end.value )
