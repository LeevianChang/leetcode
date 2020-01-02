## 46. 全排列

给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

> Link：https://leetcode-cn.com/problems/permutations

### Train of Thought
使用回溯的方法，因为取的数字不能重复，所以可以使用`nums[:i]+nums[i+1:]`