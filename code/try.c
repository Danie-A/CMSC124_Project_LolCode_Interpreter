#include <stdio.h>

int main()
{
    int choice;

    printf("Enter a number between 1 and 3: ");
    scanf("%d", &choice);

    switch (choice)
    {
    case 1:
        printf("You entered one.\n");

    case 2:
        printf("You entered two.\n");
    case 3:
        printf("You entered three.\n");
    default:
        printf("Invalid choice.\n");
    }

    return 0;
}