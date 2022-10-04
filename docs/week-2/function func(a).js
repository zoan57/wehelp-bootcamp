function func(a) {
    let result = 0;
    return (b, c) => {
        result = b * c;
        result += a;
        console.log(result);
    }
}
//為什麼nesting只能用return??不能直接放個function就好，會變成undefined???
func(2)(3, 4); // 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5); // 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9); // 你補完的函式能印出 -3+(2*9) 的結果 15
// 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果