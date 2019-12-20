## 16. 3Sum Closest
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

>Link：https://leetcode-cn.com/problems/3sum-closest


## Train of Thought

* 排序
* 循环遍历，作为mid值
* 左指证为left，右指针为right，分别从两端遍历到mid
* 记录三者和与target的差，如果比之前的少，则保存。如果三者的和大于target，则移动right，否则移动left
