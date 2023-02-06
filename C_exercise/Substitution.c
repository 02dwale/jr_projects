#include <stdio.h>
#include <cs50.h>

int key_count(string x);
void crypto(string argv);

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        if (key_count(argv[1]) == 0)
        {
            printf("Key is valid.\n");
            crypto(argv[1]);
                return 0;

        }

        
        else
        {
            switch (key_count(argv[1]))
            {
               case 1:
               printf("Your key must constit only one fo each letter of alphabet!\n");
               break;
               case 2:
               printf("Your key must costist only alphabet characters!\n");
               break;
               case 3:
               printf("Your key must constit of 26 symbols!\n");
               break;
            }
            return 1; 
        }
    }
    else 
    {
        printf("Error. Too many or too less arguments in command line.\n");
        return 1;
    }
}



// Функция, которая определяет размер массива введенного шифра
int key_count (string k)
{
    int count[26];
    for (int i = 0; i < 26; i++ ){
        count[i] = 0; }
    int r = 0; 
    int j = 0;
    string alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    while (k[j] != '\0' && r == 0)  // пока массив не кончился и нет сообщения об ошибке
    {
 
        if ((k[j] >= 65 && k[j] <= 90) || (k[j] >= 97 && k[j] <= 122))  // проверяем что это буква 
        { 
                 for (int i = 0; i < 26; i++) // какое количество раз встречается буква
                 {
                      if ((k[j] == alp[i]) || (k[j] == alp[i] + 32)) {
                      count[i]++;
                      break; }
                 }
            
        }
        else
        {
            r = 2;
        }
        j++;  // проверяем следующий элемент массива
    }
    for (int i = 0; i < 26; i++) {
    if ( count[i] != 1) {
        r = 1;
        break; 
    }}

    if ((j != 26) && ((r != 1) && (r != 2)))
    r = 3;
    return r;
}

//Функция, которая преобразует сообщение в шифр с помощью ключа (на вход ключ)
void crypto (string argv)
{
            char key[52];
            string key1 = argv;
            
            string mes = get_string("Write your message: ");
            string alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
            for (int i = 0; i < 26; i++)
            {
                key[i] = key1[i];
            }
            for (int l = 0; l < 26; l++){
            key[26+l]= key[l]+32; //добавляем в массив ключа строчные буквы
            }
                int j = 0; 
                int k = 0;
                while (mes[j] != '\0'){
                    if ((mes[j] >= 65 && mes[j] <= 90) || ((mes[j] >= 97) && (mes[j] <= 122))) //если не буква, то пропускаем
                    {
                    if ( mes[j] == alph[k]) {   //проверяем что за буква в сообщении и меняем их на шифрованную и проверяем следующую
                        mes[j] = key[k];
                        k = 0; 
                        j++;}
                    else
                    k++;
                    }
                    else{
                    j++;}
                     }
                    printf("Cryptotext: %s\n", mes);
}