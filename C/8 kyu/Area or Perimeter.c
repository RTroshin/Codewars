#include <stdio.h>

int input_side(int*);
int area_or_perimeter(int, int);

int main(void)
{
    int l, w;
    int rc;
    
    printf("Input side for rectangle: ");
    rc = input_side(&l);
    if (rc)
        return 1;
    rc = input_side(&w);
    if (rc)
        return 1;
    
    if (l == w)
        printf("Area of rectangle is %d\n", area_or_perimeter(l, w));
    else
        printf("Perimeter of rectangle is %d\n", area_or_perimeter(l, w));
    
    return 0;
}

int input_side(int *side)
{
    int rc;
    
    rc = scanf("%d", side);
    if (!rc)
    {
        printf("Error! Incorrect enter\n");
        return 1;
    }
    else
        return 0;
}

int area_or_perimeter(int l , int w)
{
    if (l == w)
        return l * w;
    else
        return 2 * (l + w);
}
