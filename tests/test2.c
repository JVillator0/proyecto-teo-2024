int main() {
    int x = 0, y = 10;

    if (x < y) {
        x = x + 1;
    } else {
        y = y - 1;
    }

    while (x < y) {
        x = x + 2;
    }

    return 0;
}
