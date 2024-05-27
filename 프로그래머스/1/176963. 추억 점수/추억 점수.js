function solution(name, yearning, photo) {
    var answer = [];
    
    photo.forEach((names) => {
        let total = 0;
        for (let i = 0; i < names.length; i++) {
            for (let j = 0; j < name.length; j++)
                if (names[i] === name[j]) {
                    total += yearning[j];
                }
        }
        answer.push(total)
    })
    
    return answer;
}