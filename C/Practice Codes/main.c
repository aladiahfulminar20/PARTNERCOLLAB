#include <stdio.h>
#include <stdlib.h>

int sum(int x, int y)
{
    return x + y;
}

int subtract(int x, int y)
{
    return x - y;
}

int multiply(int x, int y)
{
    return x * y;
}

int divide(int x, int y)
{
    return x / y;
}

int main()
{

    int selection;
    char op[2], a[10], b[10];

    printf("\n Choose your operation: \n");
    printf("\n 1. Add");
    printf("\n 2. Subtract");
    printf("\n 3. Multiply");
    printf("\n 4. Divide\n");

    fflush(stdin);
    printf("\n Enter the value of a: ");
    fgets(a, 10, stdin);
    fflush(stdin);
    printf("\n Enter the value of b: ");
    fgets(b, 10, stdin);
    fflush(stdin);

    int x = atoi(a);
    int y = atoi(b);

    while (1)
    {
        printf("\n Select operation (1-4): ");
        fgets(op, 2, stdin);
        selection = atoi(op);

        if (selection == 1)
        {
            printf("\n The sum of %d & %d is %d", x, y, sum(x, y));
            break;
        }
        else if (selection == 2)
        {
            printf("\n The difference of %d & %d is %d", x, y, subtract(x, y));
            break;
        }
        else if (selection == 3)
        {
            printf("\n The product of %d & %d is %d", x, y, multiply(x, y));
            break;
        }
        else if (selection == 4)
        {
            printf("\n The division of %d & %d is %d", x, y, divide(x, y));
            break;
        }
        else
        {
            printf("\n Invalid operation, such operation doesn't exist!");
        }
    }
}