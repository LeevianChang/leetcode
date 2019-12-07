## 1. Two Sum

>Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

> Link：https://leetcode-cn.com/problems/two-sum


## Train of Thought

题目想要找到两个数字的和是目标数字，可以想到使用一个map结构（字典结构），map结构可以在O(1)的时间复杂度进行查找某个数值
