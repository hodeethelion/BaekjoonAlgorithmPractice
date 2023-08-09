const fs = require("fs");
const input = fs.readFileSync("dev/stdin").toString().trim().split("\n");
let graph = input.slice(1).map((e) => [...e.split("")]);
const [row,col] = input[0].split(" ").map(Number);

const dr = [0, 0, 1, -1];
const dc = [-1, 1, 0, 0];
let visited = [];

for (let j = 0; j < col; j++) {
  let sample = new Array(row).fill(0);
  visited.push(sample);
}

// visited 처리 색 처리 더하기 처리 밖에서
// 1. 어떤 색인지 다 찾아 그런 다음에 더해
const bfs = ([start_c, start_r]) => {
  let count = 0;
  const color = graph[start_c][start_r];
  let queueNext = [[start_c, start_r]];
  // 당연히 방문안햇을 거야
  while (queueNext.length != 0) {
    const [cur_c, cur_r] = queueNext.shift();
    if (visited[cur_c][cur_r] == 1) {
      continue;
    }
    visited[cur_c][cur_r] = 1;
    count++;
    for (let i = 0; i < 4; i++) {
      const next_col = cur_c + dc[i];
      const next_row = cur_r + dr[i];
      if (
        next_col >= 0 && // 안에 들어오고
        next_row >= 0 &&
        next_col < col &&
        next_row < row &&
        graph[next_col][next_row] == color &&
        visited[next_col][next_row] == 0 // 아직 방문 안했을 때
      ) {
        queueNext.push([next_col, next_row]);
        // console.log([next_col, next_row]);
      }
    }
  }
  return [count, color];
};

// ####test####
// const [count, color] = bfs([0, 0]);
// console.log(count, color)
// console.log(visited)

let [white, blue] = [0, 0];
for (let r = 0; r < row; r++) {
  for (let c = 0; c < col; c++) {
    // console.log('error', c,r)
    if (visited[c][r] == 0) {
      const [count, color] = bfs([c, r]);
      if (color == "W") {
        white += count ** 2;
        // console.log(white)
      } else {
        blue += count ** 2;
        // console.log(blue)
      }
    }
  }
}
console.log(white, blue);
