function landPerimeter(arr) {
  let perimeter = 0;
  for (let height = 0; height <= arr.length - 1; height++) {
    for (let width = 0; width <= arr[0].length - 1; width++) {
      if (arr[height][width] === "X") {
        //위아래 둘레 길이 구하기
        if (height === 0 || arr[height - 1][width] !== "X") perimeter++;
        if (height === arr.length - 1 || arr[height + 1][width] !== "X")
          perimeter++;

        //왼쪽 오른쪽 둘레길이 구하기
        if (width === 0 || arr[height][width - 1] !== "X") perimeter++;
        if (width === arr[0].length - 1 || arr[height][width + 1] !== "X")
          perimeter++;
      }
    }
  }

  return `Total land perimeter: ${perimeter}`;
}
