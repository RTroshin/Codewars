#include <stdio.h>

int input_number(long*);
long odd_count(long);

int main(void)
{
    long n;
    int rc;
    
    printf("Input number: ");
    rc = input_number(&n);

    if (!rc)
        printf("Amount Odd numbers below n is %ld\n", odd_count(n));
    
    return rc;
}

int input_number(long *n)
{
    int rc;
    
    rc = scanf("%ld", n);
    if (!rc)
    {
        printf("Error! Incorrect enter\n");
        return 1;
    }
    else if (*n < 0)
    {
        printf("Error! Incorrect value\n");
        return 2;
    }

    return 0;
}

long odd_count(long n) {
    return n / 2;
}