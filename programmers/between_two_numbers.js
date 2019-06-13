function solution(a, b) {
    let result = 0
    if(a > b){
        [a, b] = [b, a];
    }
    for(let i=a;i<=b;i++){
        result += i;
    }
    return result
}