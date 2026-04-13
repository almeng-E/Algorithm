#include <stdio.h>

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
        
    int arr[3] = {a, b, c};
    for (int i=0; i<3; ++i){
        if (arr[i] > arr[2]){
            int tmp = arr[2];
            arr[2] = arr[i];
            arr[i] = tmp;
        }
    }
    for (int i=0; i<3; ++i){
        if (arr[i] < arr[0]){
            int tmp = arr[0];
            arr[0] = arr[i];
            arr[i] = tmp;
        }
    }

    printf("%d %d %d", arr[0], arr[1], arr[2]);
    
    return 0;
}