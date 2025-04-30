const { rl } = require("./input");

let n = null;
const inputs = [];

rl.on("line", (line) => {
    if (!n) n = Number(line);
    else {
        inputs.push(line);
        if (inputs.length === n) rl.close();
    }
});

rl.on("close", () => {
    const arr = [...new Set(inputs)]; // 중복된 단어 제거
    let count = 0;
    //str이 검사하는 문자열
    for (str of arr) {
        let notHead = true; // 검사하는 str이 접두사X가 아닌지 판별
        for (str2 of arr) {
            if (str === str2 || str.length >= str2.length) continue; //같거나 길이가 짦은 문자열은 패스
            // str 길이 만큼 잘라서 해당 부분이 str과 일치하는지를 확인
            if (str === str2.slice(0, str.length)) {
                notHead = false; //일치하면 false 처리하고 break
                break;
            }
        }
        // notHead가 true면 자신을 접두사로 쓰는 단어가 없다고 판단
        if (notHead) count++;
    }

    console.log(count);
});
