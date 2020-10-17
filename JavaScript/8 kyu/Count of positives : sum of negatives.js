function countPositivesSumNegatives(input) {
    var countPos = 0,
        sumNeg = 0,
        result = [];
    if (input != null) {
        for (let i = 0; i < input.length; i++)
            if (input[i] > 0)
                countPos++;
            else
                sumNeg += input[i];
        if (countPos != 0 || sumNeg != 0)
            result.push(countPos, sumNeg);
    }
    return result;
}