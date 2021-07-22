"""
*  Execution:    python binary_search.py whitelist.txt < input.txt
*  Data files:   https://algs4.cs.princeton.edu/11model/tinyW.txt
*                https://algs4.cs.princeton.edu/11model/tinyT.txt
*                https://algs4.cs.princeton.edu/11model/largeW.txt
*                https://algs4.cs.princeton.edu/11model/largeT.txt
*
* % python3 binary_search.py files/tinyW.txt < files/tinyT.txt
*  50
*  99
*  13
*
* % python3 binary_search.py files/largeW.txt < files/largeT.txt | more
*  499569
*  984875
*  295754
*  207807
*  140925
*  161828
*  [367, 966 total values]
*
"""


class BinarySearch:
    """
    A class used to implement the binary search algorithm

    Methods
    -------
    rank(arr, key)
        takes an integer target and a sorted array of int values as arguments and returns
        the index of the target if it is present in the array, -1 otherwise.
    """

    def rank(self, arr: list[int], target: int) -> int:
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            # target is in arr[lo..hi] or not present.
            mid = (lo + hi) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


if __name__ == "__main__":
    import sys

    # read the integers from a file
    with open(sys.argv[1]) as f:
        whitelist = [int(i) for i in f]
    whitelist = sorted(whitelist)

    # read integer key from standard input; print if not in whitelist
    bs = BinarySearch()
    for line in sys.stdin:
        key = int(line)
        if bs.rank(whitelist, key) == -1:
            print(key)
