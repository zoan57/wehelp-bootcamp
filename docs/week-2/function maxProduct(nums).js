function maxProduct(nums) {
    let length = nums.length;
    nums.sort();
    let negMax = nums[0] * nums[1];
    let posMax = nums[length - 1] * nums[length - 2];
    if (negMax > posMax) { console.log(negMax) } else { console.log(posMax) }

}
maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([10, -20, 0, -3]) // 得到 60
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0 或 -0
maxProduct([5, -1, -2, 0]) // 得到 2
maxProduct([-5, -2]) // 得到 10