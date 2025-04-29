/**
 * 로직 작성
 * 맨 처음 문자열을 pattern으로 설정한다.
 * 이후부터는 문자열을 pattern과 문자 하나하나 비교한다.
 * 비교가 끝나고 나면 배열인 pattern을 string으로 변환하여 출력한다.
 */

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const inputs = [];
let num = null; //맨 첫줄에서 입력받는 n
let pattern = null; // 각 string 값들을 비교하여 최종적으로 나올 패턴

rl.on("line", (line) => {
    // 맨처음에 입력 갯수인 숫자 n을 입력받는다.
    if (!num) num = Number(line);
    else {
        // n 만큼의 string 값을 입력받는다.
        inputs.push(line);
        if (inputs.length === num) rl.close();
    }
});

rl.on("close", () => {
    for (let str of inputs) {
        // 첫번째 string 값은 그대로 pattern으로 입력한다.
        if (!pattern) {
            pattern = str.split("");
            continue;
        }
        pattern = pattern.map((item, index) => {
            // 이미 이전에 일치하지 않는 문자가 나온경우
            if (item === "?") return item;
            // 패턴의 문자와 검사하는 문자가 서로 동일한 경우
            if (item === str[index]) return item;
            // 패턴의 문자와 검서하는 문자가 다른 경우
            if (item !== str[index]) return "?";
        });
    }

    console.log(pattern.join(""));
});
