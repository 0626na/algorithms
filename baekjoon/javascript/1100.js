const { rl } = require("./input.js");

const chess = [];

rl.on("line", (line) => {
    chess.push(line.split(""));
    if (chess.length === 8) rl.close();
});

rl.on("close", () => {
    let count = 0;
    chess.forEach((row, index) => {
        // (0,0)이 하얀색칸 이기때문에 row가 짝수일때는 col이 짝수인 칸이 하얀색
        if (index % 2 == 0)
            row.forEach((cell, col) => {
                if (col % 2 == 0 && cell === "F") count++;
            });
        // row가 홀수인 곳은 col이 홀수인 칸이 하얀색
        else if (index % 2 !== 0)
            row.forEach((cell, col) => {
                if (col % 2 !== 0 && cell === "F") count++;
            });
    });

    console.log(count);
});
