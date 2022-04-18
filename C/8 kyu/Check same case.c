#include <stdio.h>
#include <ctype.h>

int input_symbols(char*, char*);
int same_case(char, char);

int main(void)
{
    char a, b;
    int rc;
    
    printf("Input symbols: ");
    rc = input_symbol(&a, &b);

    if (!rc)
        printf("Result: %d\n", same_case(a, b));
    
    return rc;
}

int input_symbols(char *a, char *b)
{
    int rc;
    
    rc = scanf("%c%c", a, b);
    if (!rc)
    {
        printf("Error! Incorrect enter\n");
        return 1;
    }

    return 0;
}

int same_case(char a, char b)
{
    if (!isalpha(a) || !isalpha(b))
        return -1;
    else if ((islower(a) && islower(b)) || (isupper(a) && isupper(b)))
        return 1;
    else
        return 0;
}