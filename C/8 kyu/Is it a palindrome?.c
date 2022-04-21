#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

int input_str(char*);
bool is_palindrome(const char*);

int main(void)
{
    char *str_in;
    int rc;
    
    printf("Input string: ");
    rc = input_str(&str_in);

    if (!rc)
    {
        if (is_palindrome(str_in))
            printf("It is a palindrome\n");
        else
            printf("It is not a palindrome\n");
    }

    return rc;
}

int input_str(char *str_in)
{
    int rc;
    
    rc = scanf("%s", str_in);
    if (!rc)
    {
        printf("Error! Incorrect enter\n");
        return 1;
    }

    return 0;
}

bool is_palindrome(const char *str_in) {
    if (!(str_in + 1))
        return true;

    for (int i = 0, j = strlen(str_in) - 1; str_in[i]; ++i, --j)
        if (!(tolower(str_in[i]) == tolower(str_in[j])))
            return false;

    return true;
}