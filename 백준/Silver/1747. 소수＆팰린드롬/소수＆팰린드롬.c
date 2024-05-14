#include <stdio.h>
#include <string.h>

int Palindrome(int n);
int Prime(int n);

int main()
{
    int input;
    scanf("%d", &input);

    while (1)
    {
        if (Palindrome(input) == 1 && Prime(input) == 1)
        {
            printf("%d\n", input);
            break;
        }
        else 
            input++;
    }
    return 0;
}

int Palindrome(int n)
{
    char number[10];
    sprintf(number, "%d", n); 
    int last = strlen(number); 
    
    for (int i = 0;i < last/2;i++)
    {
        if (number[i] != number[last-1-i])
            return 0;
    }
    return 1;
}

int Prime(int n)
{
    int check = 0;

    if (n == 2) 
        return 1; 

    for (int i = 2;i < n;i++)
    {
        if (n % i == 0) 
        { 
            check = 0; 
            break; 
        }
        else
            check++;
    }
    if (check == 0) 
        return 0; 
    return 1;
}