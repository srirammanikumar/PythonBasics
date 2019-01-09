def gen246():
    print("generating 2")
    yield 2
    print("generating 4")
    yield 4
    print("generating 6")
    yield 6


def take(count, iterable):
    """Returns the first n items from a iterable
    :param count: n
    :param iterable:
    :return:
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)


def distinct(iterable):
    """ returns unique values
    :param iterable:
    :yields unique elements in order from param
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)  # you can do this after yield because the item value is still available during next run


def run_distinct():
    items = [1, 2, 2, 4, 1, 24, 5]
    for item in distinct(items):
        print(item)


def run_pipeline():
    items = [1, 2, 2, 4, 1, 24, 5]
    for item in take(3, distinct(
            items)):
        """as generators are lazy evaluators, it will first go into execution of take, and when it hits the iterable, 
        it goes into distinct to get the iterable"""
        print(item)


if __name__ == '__main__':
    run_take()
    print("--------------")
    run_distinct()
    print("--------------")
    run_pipeline()
