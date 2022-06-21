#include <iostream>
/*
RULES:
4x4 grid
each new spawn is a 2, but starts as NULL or 0
numbers can only combine with themselves -> they double


*/

/*
round loop
getmove()
updateBoard(moveMaker) //moveMaker is just to send it to the right move

*/

//inr arr[yHeight][xLen]
int gameBoard[4][4] = {
    {0,0,0,0}
    {0,0,0,0}
    {0,0,0,0}
    {0,0,0,0}
};

char getMove(){
    char moveChar;
    cout << "What Direction do you want to move? (l,r,u,d):" << endl;
    cin >> moveChar;
    moveChar = tolower(moveChar);
    return moveChar;
};

void updateBoard(char move = getMove()){//spawns new 2,  after user turn

        moveMaker(move);

    for (int xCoord = 0 ; xCoord < 4 ; xCoord++){
        for (int yCoord = 0 ; yCoord < 4 ; yCoord++){
            if (gameBoard[xCoord][yCoord] == 0){
                gameBoard[xCoord][yCoord] = 2;
            }
        }
    }
};


// MOVE COMMANDS   
void moveMaker(char move){
    switch (move){
        case 'l':
            moveLeft();
            break;
        case 'r':
            moveRight();
            break;
        case 'u':
            moveUp();
            break;
        case 'd':
            moveDown();
            break;
        default:
            cout << "Please enter a valid Character: " << endl;
            getMove();
    }
    
}

void moveLeft(){
    for (int xCoord = 3 ; xCoord >= 0 ; xCoord--){//should check from left to rihgt
        for (int yCoord = 0 ; yCoord < 4 ; yCoord++){
            if (gameBoard[yCoord][xCoord] == gameBoard[yCoord][xCoord-1]){
                gameBoard[yCoord][xCoord] = 0;
                gameBoard[yCoord][xCoord-1] *= gameBoard[yCoord][xCoord];
            }
        }
    }
    return;
};

void moveRight(){
    for (int xCoord = 0 ; xCoord <= 3 ; xCoord++){//should check from right to left
        for (int yCoord = 0 ; yCoord < 4 ; yCoord++){
            if (gameBoard[yCoord][xCoord] == gameBoard[yCoord][xCoord+1]){
                gameBoard[yCoord][xCoord] = 0;
                gameBoard[yCoord][xCoord+1] *= gameBoard[yCoord][xCoord];
            }
        }
    }
    return;
};

//make possible moves