
# include <stdio.h>
# include<stdlib.h>
# include<string.h>



int sum_twointegers(int a, int b)
{
	int c = a + b;
	return c;
}



int char_matching(char a, char b[])
{
	int n = strlen(b);
	int N = 0;

	for (int i = 0; i < n; i++)
	{
		if (a == b[i])
		{
			N++;
		}
	}
	return N;
}

int test()
{

	/*
	* Printing test: show a single integer or char
	*/
	int a = 1;
	char b[] = "cde";

	printf("The test output is a = % d!\n", a);
	printf("The character is b=%s\n", b);


	/*
	* Test: print a string either one by one or by string
	*/


	char str1[] = "abc";

	int m = strlen(str1);
	printf("print a string!\n");
	printf("str1=:");
	for (int i = 0; i < m; i++)
	{
		printf("%c", str1[i]);
	}
	printf("\n");
	printf("reprint str1=%s\n", str1);


	/*
	* Print a list of integers
	*/

	int str2[] = { 1, 2, 3, 4 };
	int N = sizeof(str2) / sizeof(str2[0]);
	printf("str2=");
	for (int j = 0; j < N; j++)
	{
		printf("%d", str2[j]);
	}

	printf("\n");

	for (int j = 0; j < N; j++)
	{
		printf("%d", *(str2 + j));
		printf("\t");
	}
	printf("\n");


	int x = 3;
	int y = 101;
	int z = sum_twointegers(x, y);

	printf("The sum of x=%d and y=%d is z=%d.\n", x, y, z);


	char u = ' ';
	char w[] = "Happy Thansgiving!";

	int N_m = char_matching(u, w); // The number of matched chars
	printf("The number of matched charaters is N_m=%d.\n", N_m);



	/* Bitwise operation: https://www.tutorialspoint.com/cprogramming/c_bitwise_operators.htm
	*/

	int s1 = 3;
	int s2 = 5;

	int s3 = s2 << 1;
	printf("s3=%d\n", s3);

	int s4 = s1 & s2;
	printf("s4=s1&s2=%d\n", s4);

	int s5 = s1 | s2;
	printf("s4=s1&s2=%d\n", s5);

	int s6 = s1 ^ s2;
	printf("s4=s1 xor s2=%d\n", s6);


	return -1;

}

struct student
{
	char name[50];
	int age;
	struct student* next;
};

int display(struct student* s);

/*
void main()
{
	struct student s1;

	printf("enter the name:");
	// read string input from the user until \n is entered
	// \n is discarded
	//scanf("%[^\n]%*c", s1.name);
	scanf_s("%[^\n]%*c", s1.name, (unsigned)_countof(s1.name));


	printf("enter the age:");
	//scanf("%d", &s1.age);
	scanf_s("%d", &s1.age,1);
	display(s1);
}
*/

int main()
{
	/* Initialize a pointer to a structure, we need allocate memory at first
	*/
	struct student* s1 = (struct student*)malloc(sizeof * s1);

	struct student* s2 = (struct student*)malloc(sizeof * s2);

	/* After allocating
	*/


	printf("Input the first student:\n");
	printf("enter the name:");
	// read string input from the user until \n is entered
	// \n is discarded
	/* Scanf vs Scanf_s
	* Scanf: may overflow
	* Scanf_s: avoid overflow if the input has a longer size
	*/
	//scanf("%[^\n]%*c", s1.name);
	scanf_s("%[^\n]%*c", s1->name, (unsigned)_countof(s1->name));


	printf("enter the age:");
	//scanf("%d", &s1.age);
	scanf_s("%d", &s1->age);



	printf("Input the second student:\n");
	printf("enter the name:");
	// read string input from the user until \n is entered
	// \n is discarded
	/* Scanf vs Scanf_s
	* Scanf: may overflow
	* Scanf_s: avoid overflow if the input has a longer size
	*/
	//scanf("%[^\n]%*c", s1.name);
	scanf_s("%[^\n]%*c", s2->name, (unsigned)_countof(s2->name));


	printf("enter the age:");
	//scanf("%d", &s1.age);
	scanf_s("%d", &s2->age);


	display(s1);

	s1->next = s2;

	display(s1);

	return 0;
}

int display(struct student* s)
{
	while (s != NULL)
	{
		printf("Student's name: %s\n", s->name);
		printf("Student's age:%d\n", s->age);
		s = s->next;
	}
	return -1;
}