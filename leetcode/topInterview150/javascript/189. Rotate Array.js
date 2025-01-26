/**
leetcode TopInterview150
189. Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 */

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */

var rotate = function (nums, k) {
  /**
   * 일단 전체 배열을 한번 뒤집는다. 그리고 k값을 기준으로 0부터 k-1까지 뒤집고, k부터 나머지 배열을 전부를 뒤집어 준다.
   */
  const n = nums.length;
  k %= n; //k가 n보다 클경우를 생각해보자. k가 8이고 배열의 길이가 4이면 이는 결국 배열을 두번 돌린것과 다름이 없다. 그렇기에 k를 배열의 길이 n으로 나눈 나머지 값만큼의 회전이, k만큼 배열을 회전시킨것과 동일하다.

  // 배열의 갯수가 1이거나 k가 0이면 배열을 바꿀 필요가 없다.
  if (n == 1 || k == 0) return;

  // 부분적으로 배열들을 회전시키기 위한 함수
  const reversed = (arr, start, end) => {
    while (start < end) {
      [arr[start], arr[end]] = [arr[end], arr[start]];
      start++;
      end--;
    }
  };

  nums.reverse(); // 전체 배열 회전
  reversed(nums, 0, k - 1); //0부터 k-1까지 회전
  reversed(nums, k, n - 1); //k부터 나머지 값 회전
};

rotate([-1, -100, 3, 99], 2);
