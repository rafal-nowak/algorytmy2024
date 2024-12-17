#include <iostream>
using namespace std;
int main()
{
int a, b, x, y;
cout<< "Podaj a i b równania prostej"<<endl;
cin>>a>>b;
cout<<endl<< "Podaj x i y punktu A"<<endl;
cin>>x>>y;
if (y==a*x+b) cout<<endl<< "Punkt nalezy do prostej";
else cout<<endl<<"Punkt nie nalezy do prostej";
}