    
# Merge Sort problem  
nums1 = [2,0]
# nums1 = [1,2,3,0,0,0]
# nums1 = [-1,0,0,3,3,3,0,0,0]
m = 1
nums2 = [1]
# nums2 =  [2,5,6]
# nums2 = [1,2,2]
n = 1

# j= 0 

      
# for i in range(m + n):
#     if j < len(nums2):
#         if  nums1[i] < nums2[j] :
#             continue
#         elif nums1[i] > nums2[j]:
#             nums1.insert(i,nums2[j])
#             j = j + 1
#             if nums1[-1] == 0:
#                 del nums1[-1]
        
# nums1.sort()   
# del nums1[0:n]    
# print(nums1)


for i in range(n):
    nums1[m+i] = nums2[i]
nums1.sort()
# print(nums1)



# remove Elements 
# nums = [3,2,2,3]
# nums = [0,1,2,2,3,0,4,2]
nums = [1]
# val = 3
val = 1
k = 0 

i = 0
while i < len(nums)- 1:
    if nums[i] == val:
        nums.remove(nums[i])
        k = k + 1
        nums.append('_')
    else:
        i = i + 1

# print(k)
# print(nums)
# print(len(nums) - k)



# Remove duplicates

# nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1]
i = 0
j = 1

while i <= len(nums)- 1:
    if j == len(nums)- 1:
        i = i + 1
        if i != len(nums)- 1:
            j =  i + 1
    else:
        if nums[i] == nums[j]:
            nums.remove(nums[j])
        else:
            j = j + 1
# print(nums)


def factorial(num):
    if num == 0 or num == 1:
        return 1
    
    return num * (num - 1)

# print(factorial(10))


def count_combinations(n, r):
    return factorial(n) // factorial(r) * factorial(n-r)


# print(count_combinations(10,3))


def get_combinations(arr,r,start=0, comb_arr=[], combination_array=[]):
    if len(comb_arr) == r:
        print((tuple(comb_arr)))
        combination_array.append((tuple(comb_arr)))
        return 
    
    for i in range(start,len(arr)):
        get_combinations(arr,r, i+1,comb_arr+ [arr[i]], combination_array)
        
    return combination_array

def find_combinations(n,r):
    nums_list = [1,8,7,6,5,3,2,2]
    results = get_combinations(nums_list,r)
    return results
    
# print(find_combinations(10,3))



# Remove Duplicatewhich accurs more then twice
accurences = 0
i = 0
while i+1 <= len(nums) - 1:
    if nums[i] != nums[i+1]:
        accurences = 0
    else:
        accurences += 1
    if accurences >= 2:
        nums.remove(nums[i+1])
        # accurences = accurences - 1
    else:
        i = i + 1

# print(nums)


# Majority Elements

nums = [2,2,1,1,1,2,2,3,3,3,3,3,3,3]

count = {}
majorityElements = nums[0]

for num in nums:
    if num not in count.keys():
        count[num] = 1
    else:
        count[num] = count[num] + 1
        if count[num] > count[majorityElements]:
            majorityElements = num
            

# Rotated Array


nums = [1,2,3,4,5,6,7]
k = 3
i = 1

# while i <= k:
#     nums.insert(0,nums[-1])
#     del nums[-1]
#     i = i + 1

# for _ in range(k):
#     nums.insert(0,nums[-1])
#     del nums[-1]
deleted_elements = len(nums[:-k])
nums.extend(nums[:-k])
del nums[0:deleted_elements]
print(len(nums[:-k]))
# print(nums[:-k])
    
# print(nums)


# Longest common prefix

strs = ["flower","flow","flight"]

strs.sort()
common_prefix = ''
first_word, last_word = strs[0], strs[-1]

for i in range(len(first_word)):
    if first_word[i] != last_word[i]:
        break
    else:
        common_prefix = common_prefix + first_word[i]


print(common_prefix)

    
prefix = strs[0]
for s in strs[1:]:
    while not s.startswith(prefix) and prefix:
        prefix = prefix[:-1]

print(prefix)



# maxProfit

def maxProfit():
    prices = [2,1,2,1,0,1,2]
    buy = prices[0]
    profit = 0
    # for i in range(1, len(prices)):
    #     if prices[i] < buy:
    #         buy = prices[i]
    #     elif prices[i] - buy > profit:
    #         profit = prices[i] - buy
    
    for i in range(1,len(prices)):
        
        if max(prices[i:len(prices)]) - buy > profit:
            profit = max(prices[i:len(prices)]) - buy 
 
    return profit
    # print(max_profit)
    
print(maxProfit())

