#include <stdio.h>
int main()
{
    int main = 10;
    printf("%d", main); // This is valid, here after calling our function we are using main as a variable.
    main(); // This is invalid because, after we are declaring main as a variable of integer type,
    // an integer variable cannot be called as a function.
    return 0;
}