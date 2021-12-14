// Using printf as a variable in C
#include <stdio.h>
int main()
{
    int printf = 20;
    printf("%d", printf);  
    // Here, as we declared printf as a variable, then built-in printf() will not work here
    // as printf is a variable of integer type, we cannot call it as a function
}