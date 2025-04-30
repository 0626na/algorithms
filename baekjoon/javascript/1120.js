const { rl } = require("./input.js");

const inputs = [];

rl.on("line", (line) => {
    inputs.push(line.split(" ")[0]);
    inputs.push(line.split(" ")[1]);
    rl.close();
});

rl.on("close", () => {
    const [left, right] = inputs;
    let diff = left.length;

    // 두 문자열의 길이가 동일하면 문자별로 다른부분만 찾아서 계산
    if (left.length === right.length) {
        for (let i = 0; i < left.length; i++) if (left[i] === right[i]) diff--;
    } else {
        // left 문자열이 right 문자열보다 짦을 경우, right 문자열을 left 문자열 길이만큼 나누면서 부분문자열을 탐색한다.
        for (let i = 0; i <= right.length - left.length; i++) {
            let temp = 0;
            left.split("").forEach((ch, index) => {
                if (ch !== right[i + index]) temp++;
            });

            // 부분 문자열 중에서 left와 일치하는 부분을 찾았을때
            if (temp === 0) {
                diff = 0;
                break;
            } else if (diff > temp) diff = temp;
        }
    }

    console.log(diff);
});
