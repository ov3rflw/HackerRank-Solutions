#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int nb1,nb2;
    float nb3,nb4;
    
    scanf("%d %d %f %f",&nb1, &nb2, &nb3, &nb4);
    
    printf("%d %d", nb1+nb2, nb1-nb2);
    printf("\n%.1f %.1f", nb3+nb4, nb3-nb4);
    
    return 0;
}
