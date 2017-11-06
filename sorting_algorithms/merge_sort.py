
def merge_sort(array):
    length = len(array)
    if(length <= 1): return array
    if(length == 2): return compare_and_sort(array)

    half_point = int(length/2)
    half1 = array[0:half_point]
    half2 = array[half_point:]

    return merge(merge_sort(half1), merge_sort(half2))

def merge(half1, half2):
    pointer1 = 0
    half1_length = len(half1)
    pointer2 = 0
    half2_length = len(half2)
    results = []

    while(pointer1 < half1_length and pointer2 < half2_length):
        if(half1[pointer1] <= half2[pointer2]):
            results.append(half1[pointer1])
            pointer1+=1
        else:
            results.append(half2[pointer2])
            pointer2+=1

    if(pointer1 < half1_length): results = results + half1[pointer1:]
    if(pointer2 < half2_length): results = results + half2[pointer2:]

    return results

def compare_and_sort(array):
    if(array[0] > array[1]):
        temp = array[0]
        array[0] = array[1]
        array[1] = temp
    return array

# TESTS ----------------------------------------------------
import unittest

class Test(unittest.TestCase):
    def test_basic_sort(self):
        expected = [3,3,5,5,51,83]
        result = merge_sort([83,3,5,51,5,3])
        self.assertEqual(result, expected)

    def test_sort_one_number(self):
        expected = [1]
        result = merge_sort([1])
        self.assertEqual(result, expected)

    def test_sort_two_numbers(self):
        expected = [1,2]
        result = merge_sort([2,1])
        self.assertEqual(result, expected)

    def test_sort_negative_numbers(self):
        expected = [-500,-5,-5,-4,-1,-1,2,2,3,6,1000]
        result = merge_sort([-5,2,-5,-1,-4,3,6,2,-1,-500,1000])
        self.assertEqual(result, expected)

unittest.main()
