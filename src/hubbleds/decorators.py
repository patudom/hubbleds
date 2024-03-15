import functools
import solara


def _computed_property(_func=None, *, pointer=None, reference=None):
    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = solara.lab.computed(lambda: func(*args, **kwargs))
            # print(value())

            # if value():
            #     pointer.set(reference[func.__name__])

            # return value

            if pointer is not None and reference is not None:
                if value():
                    pointer.set(reference[func.__name__])

            return value()

        return wrapper

    if _func is None:
        return decorator

    return decorator(_func)


def computed_property(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return solara.lab.computed(lambda: func(*args, **kwargs))

    return wrapper


if __name__ == "__main__":
    import enum

    class TestStates(enum.Enum):
        one = enum.auto()
        two = enum.auto()

    a = solara.reactive(10)
    b = solara.reactive(20)

    print(f"{TestStates.one.name}")

    current_state = solara.Reactive(TestStates.one)

    print(current_state.value)

    @computed_property  # (pointer=current_state, reference=TestStates)
    # @solara.lab.computed
    def two():
        return a.value < b.value

    three = solara.lab.computed(lambda: a.value > b.value)

    def _four():
        return a.value == b.value

    four = solara.lab.computed(lambda: _four())

    print(two())
    print(three)
    print(four)
    print(current_state.value)
