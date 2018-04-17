# 给定一个 32 位有符号整数，将整数中的数字进行反转。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
def reverse(x):
    # 测试t=-6294320，输出-234926
    a= list(str(x))
    a.reverse()
    if a[-1]=='-':
        s = -int(''.join(i for i in a[:-1]))
    else :
        s = int(''.join(i for i in a))
    if -2**31<=s<=2**31-1:
        return s
    else:return 0
	
# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
def twoSum(nums,target)
    c=list(range(0,len(nums)))
    for x in range(0,len(nums)) :
        for y in c[:x]+c[x+1:]:
            if nums[x]+nums[y] == target:
                return x,y
# 测试：nums = [2, 7, 11, 15], target = 9 输出[0, 1]
# 未解决问题：时间复杂度问题