# CPE 202 Lab 1a
from typing import Optional
from typing import List

# Maybe_List (Optional[List]) is either
# Python List
# or
# None

# Maybe_integer (Optional[int]) is either
# integer
# or
# None

# Maybe_List -> Maybe_integer
def max_list_iter(int_list: Optional[List]) -> Optional[int]:
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError

   if len(int_list) == 0:
      return None

   for number in range(len(int_list)):
      maximum = 0
      new_max = int_list[number]

      if new_max > maximum:
         maximum = new_max

   return maximum

# Maybe_List -> Maybe_List
def reverse_list(int_list: Optional[List]) -> Optional[List]:
   """reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError
   empty = []
   for i in range(len(int_list) + 1):
      empty.append(int_list[-i])
   empty.remove(int_list[0])
   return empty

# Maybe_List -> None
def reverse_list_mutate(int_list: Optional[List]) -> None:
   """reverses a list of numbers, modifying the input list, returns None
   If list is None, raises ValueError"""
   new_lst = int_list[::-1]
   return new_lst

