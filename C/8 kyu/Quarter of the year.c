#include <stdio.h>

int input_month(int*);
int quarter_of(int);

int main(void)
{
    int month;
    int rc;
    
    printf("Input month: ");
    rc = input_month(&month);
    if (rc)
        return 1;

    printf("It is %d quarter of the year\n", quarter_of(month));
    
    return 0;
}

int input_month(int *month)
{
    int rc;
    
    rc = scanf("%d", month);
    if (!rc)
    {
        printf("Error! Incorrect enter\n");
        return 1;
    }
    else if (*month < 1 || *month > 12)
    {
        printf("Error! Incorrect value\n");
        return 2;
    }
    else
        return 0;
}

int quarter_of(int month)
{
    return (month + 2) / 3;
}
