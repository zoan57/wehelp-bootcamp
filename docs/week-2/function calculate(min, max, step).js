function calculate(min, max, step) {
    let arr = [];
    let sum = 0
    for (let i = min; i <= max; i += step) {
        arr.push(i);
        sum += i
    }
    console.log(sum);
}
calculate(1, 3, 1); // 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2); // 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2); // 你的程式要能夠計算 -1+1，最後印出 0