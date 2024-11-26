int main() {
    int a = 5;
    float b;

    if (a > 3) {
        b = a + 2.5; // Operación válida
        char c = 'z';

        if (c == 'z') {
            a = c; // Error semántico: asignación de char a int
        }
    }

    return 0;
}
