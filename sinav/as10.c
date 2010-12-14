#include <stdio.h>

int main(void) {
	int x=5, y=7;
	int i;

	// s1a
	y += x + y > 10;
	printf("y = %d\n", y);

	// s1b
	for (i=0; i < 5; i++)
		printf("%c", 'a' + i);

	printf("\n");

	// s1c
	i = 99;
	while (i-- > 100) ;

	printf("i = %d \n", i);

	return 0;
}
