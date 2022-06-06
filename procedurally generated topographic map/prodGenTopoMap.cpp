#include <iostream>
#include <map>
#include <cmath>
using namespace::std;

//this can be modifed to be a noise map generator, just using doubles in range(0,1)
//TODO:: generate the cascading numbers, the translating is done
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


//could just loop throught the whole thing then add index to a list once they are processed, 9 -> 0 then 0 -> gridSize

//check for reach poit if  the connect are less, if so then make it 1 one then the current spot
//TODO:: figure out how to check each idex starting with the high numbers (obviously)
int highPoint = gridSize/2; //direct center, can be randomized later when I figure out the bound issues,
// also want to make mutiple highpoints, could just run another iteration on the same grid before a print, will have to rewor the int changer
//the added highpoints will be randomized with a top 80% bais to the max height
int maxHeight;
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

//WAY better pallete
/*
//for light level refrence later
   map<int,char> BetterLightLevelDict; //light to dark
$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.

BetterLightLevelDict[0] = '$';
BetterLightLevelDict[1] = '@';
BetterLightLevelDict[2] = 'B';
BetterLightLevelDict[3] = '%';
BetterLightLevelDict[4] = '8';
BetterLightLevelDict[5] = 'W';
BetterLightLevelDict[6] = 'M';
BetterLightLevelDict[7] = '#';
BetterLightLevelDict[8] = '*';
BetterLightLevelDict[9] = 'o';
BetterLightLevelDict[10] = 'a';
BetterLightLevelDict[11] = 'h';
BetterLightLevelDict[12] = 'k';
BetterLightLevelDict[13] = 'b';
BetterLightLevelDict[14] = 'd';
BetterLightLevelDict[15] = 'p';
BetterLightLevelDict[16] = 'q';
BetterLightLevelDict[17] = 'w';
BetterLightLevelDict[18] = 'm';
BetterLightLevelDict[19] = 'Z';
BetterLightLevelDict[20] = 'O';
BetterLightLevelDict[21] = '0';
BetterLightLevelDict[22] = 'Q';
BetterLightLevelDict[23] = 'L';
BetterLightLevelDict[24] = 'C';
BetterLightLevelDict[25] = 'J';
BetterLightLevelDict[26] = 'U';
BetterLightLevelDict[27] = 'Y';
BetterLightLevelDict[28] = 'X';
BetterLightLevelDict[29] = 'z';
BetterLightLevelDict[30] = 'c';
BetterLightLevelDict[31] = 'v';
BetterLightLevelDict[32] = 'u';
BetterLightLevelDict[33] = 'n';
BetterLightLevelDict[34] = 'x';
BetterLightLevelDict[35] = 'r';
BetterLightLevelDict[36] = 'j';
BetterLightLevelDict[37] = 'f';
BetterLightLevelDict[38] = 't';
BetterLightLevelDict[39] = '/';
BetterLightLevelDict[40] = '\';
BetterLightLevelDict[41] = '|';
BetterLightLevelDict[42] = '(';
BetterLightLevelDict[43] = ')';
BetterLightLevelDict[44] = '1';
BetterLightLevelDict[45] = '{';
BetterLightLevelDict[46] = '}';
BetterLightLevelDict[47] = '[';
BetterLightLevelDict[48] = ']';
BetterLightLevelDict[49] = '?';
BetterLightLevelDict[50] = '-';
BetterLightLevelDict[51] = '_';
BetterLightLevelDict[52] = '+';
BetterLightLevelDict[53] = '~';
BetterLightLevelDict[54] = '<';
BetterLightLevelDict[55] = '>';
BetterLightLevelDict[56] = 'i';
BetterLightLevelDict[57] = '!';
BetterLightLevelDict[58] = 'I';
BetterLightLevelDict[59] = ';';
BetterLightLevelDict[60] = ':';
BetterLightLevelDict[61] = ',';
BetterLightLevelDict[62] = '"';
BetterLightLevelDict[63] = '^';
BetterLightLevelDict[64] = ''';

*/
