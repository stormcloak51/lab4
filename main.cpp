#include <iostream>
using namespace std;

int main() {
  double a, b, c;
  cin >> a >> b >> c;

  double mx = a;
  if (b > mx) mx = b;
  if (c > mx) mx = c;

  cout << "Максимум: " << mx << endl;
  return 0;
}

  
