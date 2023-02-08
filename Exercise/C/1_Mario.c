//  Программа, которая строит симметричные половины пирамиды с промежутком внутри высотой от 1 до 8 блоков

#include <stdio.h>
#include <cs50.h>

int main (void)
{
    // Ввод высоты пирамиды
    int h;
    char a;
    do
    {
    do
    {
        h = get_int("Height: ");
    }
    while(h < 1 || h > 8);
    // Строим пирамиду i - высота текущая, h - высота общая, s - пробелы, b -блоки
    for (int i = h; i > 0; i--) //Цикл текущего уровня
    {
        for (int s = i - 1; s>0; s--) //Цикл расставления пробелов
        {
            printf(" ");
        }
        for (int j = 0; j<2; j++) //Цикл повторения решеток 
        {
            for (int b = h - i + 1; b > 0; b--) //Цикл расставления решеток 
            {
                printf("#");
            }
            printf("  ");
        }
        printf("\n");
    }
    a = get_char("Do you want play again? y/n\n"); 
    }
    while (a == 'y'|| a == 'Y');
}