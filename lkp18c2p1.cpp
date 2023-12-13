#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_N 100

int main() {

    int n, m;
    scanf("%d%d", &n, &m);

    int i;
    int lines[MAX_N];
    for (i = 0; i < n; i++) {
        scanf("%d", &lines[i]);
    }

    for (i = 0; i < m; i++) {
        int j;
        int shortest = 0;
        for (j = 1; j < n; j++) {
            if (lines[j] < lines[shortest]) {
                shortest = j;
            }
        }
        printf("%d\n", lines[shortest]);
        lines[shortest]++;
    }

    return 0;
}