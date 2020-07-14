#include <iostream>

using namespace std ;

int main(){
  
  int choice :
  
  cout<<("WorldChange version beta test v0.1.2publicBETA \n");
  cout<<("choice :\n");
  cout<<("1 : Glass world\n");
  cout<<("2 : Black world\n");
  cout<<("3 : Mineral world\n");
  cout<<("4 : Pastel world ( wool world )\n");
  cout<<("5 : Exit\n");
  cout<<("YOUR CHOICE :"); 
  cin>>choice ;
  if (choice == 1){
    system("python3 glassWorld.py");
  }
  else if (choice == 2){
    system("python3 blackWorld.py");
  }
  else if (choice == 3){
    system("python3 mineralWorld.py");
  }
  else if (choice == 4){
    system("python3 pastelWorld.py");
  }
  else if (choice == 5){
    cout<<("okay, exiting...");
  }
  return 0; 

}
