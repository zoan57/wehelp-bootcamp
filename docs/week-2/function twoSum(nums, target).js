function twoSum(nums, target) {
    let numSecIndex = 0;
    for (let i = 0; i < nums.length; i++) {
        let numSec = target - nums[i];
        if (nums.includes(numSec)) {
            numSecIndex = nums.indexOf(numSec);
            if (i != numSecIndex) {
                return ([i, numSecIndex])
            }
        }
    }
}
let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9