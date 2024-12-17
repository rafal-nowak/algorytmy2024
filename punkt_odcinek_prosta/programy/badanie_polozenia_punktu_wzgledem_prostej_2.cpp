#include <iostream>
using namespace std;
int main()
{
int x, y, xA, yA, xB, yB;
cout<< „Podaj wspolrzedne x i y punktu”<<endl;
cin>>x>>y;
cout<<endl<< „Podaj xA i yA jednego z koncow odcinka”<<endl;
cin>>xA>>yA;
cout<<endl<< „Podaj xB i yB drugiego z koncow odcinka”<<endl;
cin>>xB>>yB;
if ((y-yA)*(xB-xA)-(x-xA)*(yB-yA) == 0) cout<<endl<< „Punkt nalezy do prostej”;
else cout<<endl<<„Punkt nie nalezy do prostej";
}