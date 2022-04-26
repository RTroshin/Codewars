#include <stdio.h>

int input_number(int*);
const char *even_or_odd(int);

int main(void)
{
    int number, rc;
    
    printf("Input number: ");
    rc = input_number(&number);

    if (!rc)
        printf("Number is %s\n", even_or_odd(number));

    return rc;
}

int input_number(int *number)
{
    int rc;
    
    rc = scanf("%d", number);
    if (!rc)
    {
        printf("Error! Incorrect enter\n");
        return 1;
    }

    return 0;
}

const char *even_or_odd(int number)
{
    return number % 2 ? "Odd" : "Even";
}
