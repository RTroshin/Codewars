function numberToPower(number, power) {
    for (let i = 1, n = number; i < power; ++i)
        number *= n

    return power > 0 ? number : 1
}
