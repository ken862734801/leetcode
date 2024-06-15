/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  let count = {};
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] in count) {
      return true;
    } else {
      count[nums[i]] = i;
    }
  }
  return false;
};
