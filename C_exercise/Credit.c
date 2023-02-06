#include <stdio.h>
#include <cs50.h>

int main(void)
{
    char a;
    
    do
    {
        printf("____________\n");
        int nechet = 0;
        int chet = 0;
        int f = 0; 
        int d = 0;
        int j = 0;
        unsigned long n = get_long("Card nubmer: ");
        //proverit caty na proizoditelya
        while (n > 0)
        {
        j++;
        //printf("j = %i\n",j);

        d = n % 10;
        n = n / 10;

        if (n < 100 && n > 10)
            f = n;
        //printf ("d = %i\nn = %li\n",d,n);
        
        if (j % 2 == 0)
        {   
            if (d*2 > 10)
                {
                    chet = 1 + chet + ((d*2)%10);
                    //printf("chet = %i, +>10\n", chet);  
                }
                
            else
                {
                    chet = chet + (d*2);
                    //printf("chet = %i +<10\n", chet);  
                }
            
        } 
        else
             {
                 nechet = nechet + d;
                 //printf("nechet = %i\n",nechet);
             }
             //printf("_________\n");
             
        }
        if (j < 13 || j > 16)
            printf("Card number doesn't correct. ");
        else 
        {
            if ((nechet + chet)%10 == 0)
            {
                printf("Status: VALID\n");
            if (f == 34 || f == 37)
            printf ("Card: American Express\n");
        else if (f > 50 && f < 56)
            printf ("Card: MasterCard\n");
        else if (f > 39 && f < 50)
            printf ("Card: Visa\n");
        else
        {
            printf ("Undefined card\n");
        }
            printf("____________\n");
            
            }
            else
            printf("Status: INVALID\n");
        }
        
    
        
        
        
    a = get_char("Do you want input card number again? (y/n)\n");
    
    }
    
   while (a == 'y' || a == 'Y');
}