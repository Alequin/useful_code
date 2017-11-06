
def quick_sort(array):
    if(len(array) <= 1): return array
    pivot = array[-1]
    half1 = []
    half2 = []

    for index in range(0, len(array)-1):
        val = array[index]
        if(val <= pivot):
            half1.append(val)
        else:
            half2.append(val)

    return quick_sort(half1) + [pivot] + quick_sort(half2)

# TESTS ----------------------------------------------------
import unittest

class Test(unittest.TestCase):
    def test_basic_sort(self):
        expected = [3,3,5,5,51,83]
        result = quick_sort([83,3,5,51,5,3])
        self.assertEqual(result, expected)

    def test_sort_one_number(self):
        expected = [1]
        result = quick_sort([1])
        self.assertEqual(result, expected)

    def test_sort_two_numbers(self):
        expected = [1,2]
        result = quick_sort([2,1])
        self.assertEqual(result, expected)

    def test_sort_negative_numbers(self):
        expected = [-500,-5,-5,-4,-1,-1,2,2,3,6,1000]
        result = quick_sort([-5,2,-5,-1,-4,3,6,2,-1,-500,1000])
        self.assertEqual(result, expected)

unittest.main()
