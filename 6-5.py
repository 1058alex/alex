# TODO Дан список чисел, необходимо его развернуть без использования метода revese и
#  функции reversed, а так же дополнительного списка и среза

nums = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(nums) // 2):
    nums[i], nums[~i] = nums[~i], nums[i]
print(nums)
