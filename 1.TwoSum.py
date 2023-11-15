"""
Учитывая массив целых чисел nums и целое число target, вернуть индексы двух чисел так, чтобы их сумма составляла target.
Вы можете предположить, что каждый вход будет иметь ровно одно решение , и вы не можете использовать один и тот же элемент
дважды.
Вы можете вернуть ответ в любом порядке.
Пример 1:

Ввод: nums = [2,7,11,15], target = 9
  Выход: [0,1]
  Объяснение: Поскольку nums[0] + nums[1] == 9, мы возвращаем [0, 1].


Пример 2:

Ввод: nums = [3,2,4], target = 6
  Выход: [1,2]


Пример 3:

Ввод: nums = [3,3], target = 6
Выход: [0,1]
"""


# brute force
def twoSum(nums, target):
    """
       :type nums: List[int]
       :type target: int
       :rtype: List[int]
    """
    for curr_el in range(len(nums) - 1):
        for next_el in range(curr_el + 1, len(nums)):
            if nums[curr_el] + nums[next_el] == target:
                return [curr_el, next_el]