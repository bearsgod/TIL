#include<iostream>
#include<string.h>
#include<string>

using namespace std;

int main ()
{
    int n;
    cin >> n;
    for(int i = 0; i<n; i++)
    {
        int k;
        cin >> k;
        int c = k*8;
        char s[c];
        cin.getline(s,c);
        char* tok1 = strtok(s," ");
        cout<<s;
        while(tok1!=NULL)
        {
            int f[k];
            for(int j = 0;j<k;j++)
            {
                int tok1;
                f[j]=tok1;
                cout<<f[j];
            }
        }
    }
    return 0;
}