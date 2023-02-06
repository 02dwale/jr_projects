#include <cs50.h>
#include <stdio.h>
#include <string.h>

#define MAX 9 //Максимальное количество кандидатов


//Задаем глобальную структуру (свзянные массивы) для кандидатов, структура имеет относящиеся друг к другу свойства - имя и количество голосов.
typedef struct
{
    string name;
    int vote;
}
candidates;

//Создаем массив с параметрами из структуры candidates размером MAX
candidates politicians[MAX];

//Прототипы функций
bool vote(string, int);
void selection(int);
void bubble(int);




int main(int argc, string argv[])
{
    //Проверка на корректность аргументов кмд
        if (argc < 2 || argc > MAX)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }
//Записываем имена кандидатов из массива argv[] в структуру
    int politicians_amount = argc - 1;
    for (int i = 0; i < politicians_amount; i++)
    {
        politicians[i].name = argv[i+1];
        printf("%s\n", politicians[i].name);

    }
//Голосуем за кандидатов
    int population = get_int("Vvedite kolichestvo izbirateley: ");
    for (int i = 0; i < population; i++)
    {
        printf("%i izbiratel: ", i+1);
        string name = get_string("Za kogo golos?\n");
        if (vote(name, politicians_amount) == true)
        printf("Valid vote\n");
        else
        printf("Invalid vote\n");

for (int j = 0; j < politicians_amount; j++)
{
    printf("%s with %i votes\n", politicians[j].name, politicians[j].vote);
}
    }
    printf("__________________\n");
//Проверка имени и передача голоса
string a = get_string("Select sorting method: selection/bubble\n");
if (strcmp(a, "selection"))
selection(politicians_amount);
else
bubble(politicians_amount);

return 0;
}





bool vote (string name, int politicians_amount) //Функция принимает на вход имя и засчитывает голос, если имя действительно, отклоняет если недействительно.
{
   int j = 0;
   while ( j < politicians_amount)
     {
        if ((strcmp(name, politicians[j].name)) == 0)
          {
           politicians[j].vote++;
           return true;
          }
        else
        j++;
     }
                return false;
            }



//Selection sorting


void selection(int politicians_amount)
{
for (int i = 0; i < politicians_amount-1; i++) //сортируем столько раз, какой длины наш массив но на 1 меньше)
{
    printf("iteration %i\n_____________\n\n", i);
    for (int f = 0; f < politicians_amount; f++)
{
    printf("%s with %i votes\n", politicians[f].name, politicians[f].vote);
}

    int x = i;
    for ( int j = i; j < politicians_amount-1; j++) //цикл сравнения для i ячейки
    {
        if (politicians[x].vote > politicians[j+1].vote)
        x = j+1; //номер самой маленькой ячейки
    }
    if (x != i ) //проверка на меньший член и перемещение, если меньший член не есть начальная ячейка
    {
    int sv = politicians[i].vote;
    string sn = politicians[i].name;

    printf("Меняем %i на %i \n", politicians[i].vote, politicians[x].vote); //Меняем местами x и i
    politicians[i].vote = politicians[x].vote;
    politicians[i].name = politicians[x].name;
    politicians[x].vote = sv;
    politicians[x].name = sn;





}
}
//Вывод результатов
    printf("Winners:\n");
    for (int i = 0; i < politicians_amount; i++)
    {
        if (politicians[i].vote == politicians[politicians_amount - 1].vote)
        {
            printf("%s with %i votes \n", politicians[i].name, politicians[i].vote);
        }

}
}

void bubble(int politicians_amount)
{
for (int i = 0; i < politicians_amount - 1; i++)
{
    for (int j = 0; j < politicians_amount - 1; j++)
    {
        if (politicians[j].vote > politicians[j+1].vote)
        {
            int x = politicians[j].vote;
            string z = politicians[j].name;
            politicians[j].vote = politicians[j+1].vote;
            politicians[j].name = politicians[j+1].name;
            politicians[j+1].vote = x;
            politicians[j+1].name = z;

        }
    }

}
    printf("Winners:\n");
    for (int i = 0; i < politicians_amount; i++)
    {
        if (politicians[i].vote == politicians[politicians_amount - 1].vote)
        {
            printf("%s with %i votes \n", politicians[i].name, politicians[i].vote);
        }


}
}