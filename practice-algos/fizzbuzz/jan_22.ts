function fizzBuzz(n: number): string[] {
    const answer: string[] = [];

    for (let i = 1; i <= n; i++) {
        let output = "";

        if (i % 3 === 0) {
            output += "Fizz";
        }

        if (i % 5 === 0) {
            output += "Buzz";
        }

        answer.push(output || i.toString())
    }

    return answer;
}

