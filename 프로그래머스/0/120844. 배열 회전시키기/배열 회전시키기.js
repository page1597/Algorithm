function solution(numbers, direction) {
  const total = [...numbers, ...numbers];
  if (direction === "right") {
    return total.slice(numbers.length - 1, -1);
  } else {
    return total.slice(1, numbers.length + 1);
  }
}