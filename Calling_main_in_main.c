#include <stdio.h>
int main()
{
    printf("calling\n"); // Prints Infinite times.
    main();  // Main is calling recursively without any break point.
    // Same as Recursion without break value.
    // Infinite Loop.
    return 0;
}