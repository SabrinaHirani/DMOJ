#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_N 100000

typedef struct snowflake_node {
    int snowflake[6];
    struct snowflake_node *next;
} snowflake_node;

int code(int snowflake[]) {
    return (snowflake[0] + snowflake[1] + snowflake[2] + snowflake[3] + snowflake[4] + snowflake[5])%MAX_N;
}

int identical_left(int snowflake1[], int snowflake2[], int start) {
    int i;
    for (i = 0; i < 6; i++) {
        int x = start-i;
        if (x < 0) {
            x += 6;
        }
        if (snowflake1[i] != snowflake2[x]) {
            return 0;
        }
    }
    return 1;
}

int identical_right(int snowflake1[], int snowflake2[], int start) {
    int i;
    for (i = 0; i < 6; i++) {
        int x = start+i;
        if (x >= 6) {
            x -= 6;
        }
        if (snowflake1[i] != snowflake2[x]) {
            return 0;
        }
    }
    return 1;
}

int are_identical(int snowflake1[], int snowflake2[]) {
    int i;
    for (i = 0; i < 6; i++) {
        if (identical_left(snowflake1, snowflake2, i)) {
            return 1;
        }
        if (identical_right(snowflake1, snowflake2, i)) {
            return 1;
        }
    }
    return 0;
}

void identify_identical(snowflake_node *snowflakes[]) {
    snowflake_node *node1, *node2;
    int i;
    for (i = 0; i < MAX_N; i++) {
        node1 = snowflakes[i];
        while (node1 != NULL) {
            node2 = node1->next;
            while (node2 != NULL) {
                if (are_identical(node1->snowflake, node2->snowflake)) {
                    printf("Twin snowflakes found.\n");
                    return;
                }
                node2 = node2->next;
            }
            node1 = node1->next;
        }
    }
    printf("No two snowflakes are alike.\n");
}

int main() {

    int n;
    scanf("%d", &n);

    static snowflake_node *snowflakes[MAX_N] = {NULL};
    snowflake_node *snow;
    int i, j;
    for (i = 0; i < n; i++) {
        snow = (snowflake_node*)malloc(sizeof(snowflake_node));
        if (snow == NULL) {
            fprintf(stderr, "malloc error\n");
            exit(1);
        }
        for (j = 0; j < 6; j++) {
            scanf("%d", &snow->snowflake[j]);
        }
        int snowflake_code = code(snow->snowflake);
        snow->next = snowflakes[snowflake_code];
        snowflakes[snowflake_code] = snow;
    }

    identify_identical(snowflakes);
    return 0;
}
