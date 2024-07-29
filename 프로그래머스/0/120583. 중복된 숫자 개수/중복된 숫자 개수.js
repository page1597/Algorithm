function solution(array, n) {
    let answer = 0;
    answer = array.filter((v) => v === n).length;
    return answer;
}