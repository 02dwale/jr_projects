#include <cs50.h>
#include <stdio.h>

string uppercase(string x);
int counter(string x);
void compare(int x, int y);
int main(void)
{
    char again;
    do
    {
	    string w1 = get_string("Player 1 word: ");
	    string w2 = get_string("Player 2 word: ");
	    compare((counter(uppercase(w1))), (counter(uppercase(w2))));
	    again = get_char("Do you want play again? (y/n)\n");
    }
    while ( again == 'y' || again == 'Y' );
}







// Функция, которая преобразовывает буквы в заглавные буквы

string uppercase(string x)
{
    int i = 0;
    while (x[i] != '\0')
    {
        char l = x[i];
        if (l >= 97 && l <= 122)
	        l = l - 32;
	        x[i] = l;
        i++;
        
    } 
    return x;
}

// Функция, которая сравнивает буквы в слове с таблицей значения этих букв и возвращает сумму очков всего слова

int counter (string x)
{
    int i = 0;
    int sum = 0;
    int scrab[26] = {1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10};
    string alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    while (x[i] != '\0')
    {
    int j = 0;
    while (j < 25)
    {
        if (x[i] != alf[j])
        {
        j++;
        }
        else
        {
            sum = sum + scrab[j];
            break; 
        }

    }

    i++;
    }
    return sum; 
}

// Функция, которая сравнивает

void compare(int x, int y)
{
    printf ("----------\nPlayer 1 scores: %i\nPlayer 2 scores: %i\n-----------\n", x, y);
    if (x > y)
    printf("Player 1 wins!\n");
    else
    if (y > x)
    printf ("Player 2 wins!\n");
    else
    printf ("Draw!\n");
}