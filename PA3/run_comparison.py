"""
CS 240
Linked/skip lists PA

Professor Lam
October 2014
"""

import array_set
import linked_list
import skip_set

import random
import time

def format_time(elapsed):
    return "%.4f s"%elapsed

def run_tests(count):
    print("\n=== " + str(count) + " ITEMS ===")

    # generate item lists
    to_add = {random.randrange(count) for _ in range(count)}
    to_test = {random.randrange(count) for _ in range(count)}
    to_remove = {random.randrange(count) for _ in range(count//2)}

    # figure out what the final list should look like
    correct = set(to_add)
    for n in to_remove:
        if n in correct:
            correct.remove(n)

    #print("TO ADD:    " + str(to_add))
    #print("TO REMOVE: " + str(to_remove))
    #print("TO TEST:   " + str(to_test))
    #print("FINAL:     " + str(correct))

    # try each data structure
    print()
    for data in [array_set.Set(),
                 linked_list.LinkedList(),
                 skip_set.SortedSet()]:
        print(str(type(data)))

        # add some values
        start = time.time()
        for v in to_add:
            data.add(v)
        print("add:    " + format_time(time.time() - start))

        # remove some values
        start = time.time()
        for v in to_remove:
            try:
                data.remove(v)
            except KeyError:
                pass
        print("remove: " + format_time(time.time() - start))

        # find some values
        start = time.time()
        for v in to_test:
            if (v in data) != (v in correct):
                print("ERROR: missing value: " + str(v) + " " + str(v in data) +
                        " " + str(v in correct))
                print(repr(data))
        print("search: " + format_time(time.time() - start))

        print()


def main():

    # run_tests(10)     # for debugging purposes

    for count in [100, 1000, 10000]:
        run_tests(count)

if __name__ == "__main__":
    main()

