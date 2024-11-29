#include <stdio.h>

int main() {
    int max_range;

    printf("Enter a maximum number: ");
    scanf("%d", &max_range);

    int current = 0;

    while (current <= max_range) {
        if (current == 0) {
            printf("%d ", current);
        }

        current++;
    }

    return 0;
}