import typing


def get_fibonacci_number(index: int) -> str:
    if index <= 0:
        return "does not exist :<"  # type: ignore
    m = 1
    if index == 1 or index == 2:
        return str(m)  # type: ignore
    else:
        art: typing.List[int] = [1, 1]
        for i in range(2, index):
            m = art[0]+art[1]
            art[0] = art[1]
            art[1] = m
    return str(m)  # type: ignore
