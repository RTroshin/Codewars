function countPositivesSumNegatives(input) {
    let countPos = 0,
        sumNeg = 0;
    if (input != null) {
        for (let i = 0; i < input.length; i++)
            if (input[i] > 0)
                countPos++;
            else
                sumNeg += input[i];
        if (countPos != 0 || sumNeg != 0)
            return [countPos, sumNeg];
    }
    return [];
}
