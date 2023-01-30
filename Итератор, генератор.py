import types
class FlatIterator:

 def __init__(self, list_of_list):
     self.list_of_list=list_of_list

 def __iter__(self):
     self.count=-1

     return self

 def __next__(self):

     a=self.list_of_list[0] + self.list_of_list[1] + self.list_of_list[2]
     self.count += 1
     if self.count==len(a):
        raise StopIteration
     a1 = a[self.count]
     return a1


def test_1():

 list_of_lists_1 = [
 ['a', 'b', 'c'],
 ['d', 'e', 'f', 'h', False],
[1, 2, None]
 ]

 for flat_iterator_item, check_item in zip(
 FlatIterator(list_of_lists_1),
['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
 ):
   assert flat_iterator_item == check_item
   assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__': test_1()




def flat_generator(list_of_lists):

    a = list_of_lists[0] + list_of_lists[1] + list_of_lists[2]
    for list in a:
        yield list


def test_2():

 list_of_lists_1 = [
 ['a', 'b', 'c'],
 ['d', 'e', 'f', 'h', False],
 [1, 2, None]
 ]

 for flat_iterator_item, check_item in zip(
 flat_generator(list_of_lists_1),
 ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
 ):

     
     assert flat_iterator_item == check_item
     assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

     assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)



if __name__ == '__main__':
 test_2()

