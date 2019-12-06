## 4. Median of Two Sorted Arrays

>Topic:There are two sorted arrays nums1 and nums2 of size m and n respectively.

>Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

>You may assume nums1 and nums2 cannot be both empty.

>Link:https://leetcode-cn.com/problems/median-of-two-sorted-arrays

> Example 1:
> nums1 = [1, 3]
> nums2 = [2]
> The median is 2.0

> Example 2:
> nums1 = [1, 2]
> nums2 = [3, 4]
> The median is (2 + 3)/2 = 2.5

### Train of Thought

From the topic ,we can say the overall run time complexity should be O(log (m+n)),which reminds me binary tree and dichotomization.
These Examples tell us the length of (m+n) could be odd or even.

1. 从题目中，时间复杂度要求是O(log(n+m))，提醒了可以选择二分法
2. 例子中展示了两种可能，(m+n)的长度可能是奇数，也可能是偶数

如果m+n是奇数，中位数的索引值 (m+n)/2+1 的数
如果m+n是偶数，中位数是索引值 (m+n)/2 和(m+n)/2+1 的和/2 的数

所以，根据题意，需要找到两个数组一同排序后，第(m+n)/2 和(m+n)/2+1个数


中位数mid = (m+n)/2 



