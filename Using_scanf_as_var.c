// Using scanf as variable
#include <stdio.h>
int main()
{
    int scanf;
    scanf("%d", &scanf); // Invalid Statement
    // Here as we declared scanf as a variable, built-in scanf function is replaced by an integer variable.
    // Calling an integer variable as a function is invalid.
    // So, the statement is invalid.
    printf("%d", scanf);
}