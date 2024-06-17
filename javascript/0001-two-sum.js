/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let indices = {};
  for (let i = 0; i < nums.length; i++) {
    let diff = target - nums[i];
    if (diff in indices) {
      return [i, indices[diff]];
    } else {
      indices[nums[i]] = i;
    }
  }
};
