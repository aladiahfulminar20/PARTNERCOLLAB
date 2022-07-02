#include <stdio.h>
#include <stdlib.h>

void output(char *list, char *agelist);

int main()
{
    char *name_pointer;
    char name[50];
    char *age_pointer;
    char age[3];

    printf("\nWhat is your name?: ");
    fgets(name, 50, stdin);
    printf("\nHow old are you?: ");
    fgets(age, 3, stdin);

    name_pointer = name;
    age_pointer = age;

    output(name_pointer, age_pointer);
}

void output(char *list, char *agelist)
{
    printf("\n%s", list);

    int age = atoi(agelist);

    printf("\n%d", age);
}