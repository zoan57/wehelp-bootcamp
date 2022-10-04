function maxZeros(nums) {
    let count = 0;
    let result = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] == 1) { count = 0 } else {
            count++
            result = Math.max(result, count)
        }
    }
    console.log(result)
}
maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
maxZeros([1, 1, 1, 1, 1]); // 得到 0
maxZeros([0, 0, 0, 1, 1]) // 得到 3