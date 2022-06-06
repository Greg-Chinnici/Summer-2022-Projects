#include <iostream>
#include <map>
#include <cmath>
using namespace::std;

int main() {
    int sideLen;// only works with odd numbers
    cout << "Enter a side length (odd): " ;
    cin >> sideLen;
  
int gridSize = sideLen * sideLen;
int grid[gridSize];
for (int index = 0 ; index < gridSize ; index++){
    grid[index] = 0;
};


//for light level refrence later
map<int,char> LightLevelDict; //light to dark
// .:-=+*#%@
LightLevelDict[0] = '_';//cant use a "space" " " as a char, turns into zero width char
LightLevelDict[1] = '.';
LightLevelDict[2] = ':';
LightLevelDict[3] = '-';
LightLevelDict[4] = '=';
LightLevelDict[5] = '+';
LightLevelDict[6] = '*';
LightLevelDict[7] = '#';
LightLevelDict[8] = '%';
LightLevelDict[9] = '@';


//check for reach poit if  the connect are less, if so then make it 1 one then the current spot
//TODO:: figure out how to check each idex starting with the high numbers (obviously)
int highPoint = gridSize/2; //direct center, can be randomized later when I figure out the bound issues,
// also want to make mutiple highpoints, could just run another iteration on the same grid before a print, will have to rewor the int changer
//the added highpoints will be randomized with a top 80% bais to the max height
int maxHeight;// only works with odd numbers
    cout << "Enter a max height (under 10): " ;
    cin >> maxHeight;
grid[highPoint] = maxHeight;

//could eventually override with a random number, but this is more control 
int NorthSlope = 1;
int SouthSlope = 1;
int WestSlope = 1;
int EastSlope = 1;

//check if the number is higher
if (grid[highPoint + sideLen] < grid[highPoint]){
grid[highPoint + sideLen] = grid[highPoint] - NorthSlope; //down 1
}
if (grid[highPoint - sideLen] < grid[highPoint]){
grid[highPoint - sideLen] = grid[highPoint] - SouthSlope; //up 1
}
if (grid[highPoint + 1] < grid[highPoint]){
grid[highPoint + 1] = grid[highPoint] - WestSlope; //right 1 
}
if (grid[highPoint - 1] < grid[highPoint]){
grid[highPoint - 1] = grid[highPoint] - EastSlope; // left 1
}


//make all negatives into a zero
for (int index = 0 ; index < gridSize ; index++){
    if (grid[index] < 0){
        grid[index] = 0;
    }
}

bool boolSeeValues = false;
    cout << "Do you want to see inside the machine (y/n): " ;
    char seeValues;
    cin >> seeValues;
    if (seeValues == 'y'){
        boolSeeValues = true;
    }

//print grid numbers
if (boolSeeValues){
for (int index = 0 ; index < gridSize ; index++){

    cout << grid[index] << " ";
    if ((index + 1) % sideLen == 0){
        cout << endl;
    }
}
cout << endl << endl;
}
//print light levels aka height
for (int index = 0 ; index < gridSize ; index++){
    int lightLevel = grid[index];
    cout << LightLevelDict[lightLevel] << " ";
    if ((index + 1) % sideLen == 0){
        cout << endl;
    }
}


}

/*
take in the index of the current place
check each spot that is directly connecting 
1234321
2345432
3456543
4567654
3456543
2345432
1234321

. : - = - : . 
: - = + = - : 
- = + * + = - 
= + * # * + = 
- = + * + = - 
: - = + = - : 
. : - = - : . 
*/

//code for centered falloff
/*
#include <iostream>
#include <map>
using namespace::std;

int main() {
  int  gridSize = 49;
int grid[49]{
        1,2,3,4,3,2,1,
        2,3,4,5,4,3,2,
        3,4,5,6,5,4,3,
        4,5,6,7,6,5,4,
        3,4,5,6,5,4,3,
        2,3,4,5,4,3,2,
        1,2,3,4,3,2,1
        };


//for light level refrence later
   map<int,char> LightLevelDict; //light to dark
// .:-=+*#%@
LightLevelDict[0] = ' ';
LightLevelDict[1] = '.';
LightLevelDict[2] = ':';
LightLevelDict[3] = '-';
LightLevelDict[4] = '=';
LightLevelDict[5] = '+';
LightLevelDict[6] = '*';
LightLevelDict[7] = '#';
LightLevelDict[8] = '%';
LightLevelDict[9] = '@';

for (int index = 0 ; index < 49 ; index++){
    int lightLevel = grid[index];
    cout << LightLevelDict[lightLevel] << " ";
    if ((index + 1) % 7 == 0){
                cout << endl;
            }
}

}
*/
