int main() {
    int a = 0;
    for (int i = 0; i < 10; i++) {
        if (i % 2 == 0) {
            a += i;
        }
    }
    return a;
}