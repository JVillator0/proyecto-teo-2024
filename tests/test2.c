#include <stdio.h>

int main() {
    int value = 10;

    if (value > 0) {
        printf("The number is positive.\n");

        if (value % 2 == 0) {
            printf("And it is an even number.\n");
        } else {
            printf("And it is an odd number.\n");
        }
    }

    if (value < 0) {
        printf("The number is negative.\n");
    } else {
        printf("The number is zero.\n");
    }

    return 0;
}