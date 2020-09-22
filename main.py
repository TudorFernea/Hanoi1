import argparse
import sys

init_num_disks = 0

tower1 = [10000]
tower2 = [10000]
tower3 = [10000]

def renderdsk(i, t):
    for j in range(0, init_num_disks * 2 + 1, ):
        if j >= init_num_disks - t[i - 1] and j <= init_num_disks + t[i - 1]:
            print('-', end='')
        else:
            print(' ', end='')

def renderpole():
    for j in range(0, init_num_disks * 2 + 1, 1):
        if j == init_num_disks:
            print('|', end='')
        else:
            print(' ', end='')

def rendert(t,i):
    if i <= len(t):
        renderdsk(i, t)
    else:
        renderpole()

def render():
    for i in range(init_num_disks+1,1,-1):
        rendert(tower1,i)
        rendert(tower2,i)
        rendert(tower3,i)
        print('\n')
    print('\n')




def is_valid(t1, t2):
    if t1[len(t1)-1] > t2[len(t2)-1]:
        return False
    return True



def invalid_message1():
    print('Invalid move, disk on top of destination must be bigger than disk on top of current tower \n')
def invalid_message2():
    print('Invalid move, destination and current towers must be different \n')




def move(t1, t2):
    t2.append(t1.pop())

def solve(t1, t2, t3, num_disks):
    if num_disks == 1:
        move(t1,t3)
        render()
    if num_disks > 1:
        solve(t1,t3,t2, num_disks - 1)
        move(t1,t3)
        render()
        solve(t2,t1,t3, num_disks - 1)




def game(player):
    win = False
    num_moves = 0
    while win == False:
        f"Player {player} moves \n"

        ok = False

        while ok == False:
            inp = int(input("Choose current tower (1 or 2 or 3) : "))

            if inp == 1:
                current = tower1
            if inp == 2:
                current = tower2
            if inp == 3:
                current = tower3

            print("\n")
            inp = int(input("Choose destination tower (1 or 2 or 3) : "))

            if inp == 1:
                dest = tower1
            if inp == 2:
                dest = tower2
            if inp == 3:
                dest = tower3

            print("\n")

            if current != dest:
                if is_valid(current, dest) == True:
                    move(current, dest)
                    num_moves += 1
                    ok = True
                else:
                    invalid_message1()
            else:
                invalid_message2()

        render()

        if len(tower3) == init_num_disks + 1:
            win = True
            f"Player {player} finished with {num_moves} moves \n"





if __name__ == '__main__':

    tower1 = [100000]
    tower2 = [100000]
    tower3 = [100000]

    parser = argparse.ArgumentParser(description='Number of disks and game mode')
    parser.add_argument('disks_nr',type=int,help='Choose the number of disks (3 or more)')
    parser.add_argument('game_mode', type=int,help='Choose game mode: 1 for player vs player | 2 for player vs computer')

    args = parser.parse_args()

    if args.disks_nr < 3:
        print('\n')
        f"{args.disks_nr} is not a valid number of disks, minimum number of disks is 3"
        print('\n')
        sys.exit()

    if args.game_mode !=1 and args.game_mode !=2 :
        print('\n')
        f"{args.game_mode} is not a valid value for game mode, choose 1 or 2"
        print('\n')
        sys.exit()

    init_num_disks = args.disks_nr

    for i in range(init_num_disks,0,-1):
        tower1.append(i)

    if args.game_mode == 1:

        render()

        num_moves = 0

        game(1)
        score1 = num_moves

        tower1 = [100000]
        tower2 = [100000]
        tower3 = [100000]

        for i in range(init_num_disks, 0, -1):
            tower1.append(i)

        render()


        game(2)
        score2 = num_moves

        if score1 >= score2:
            print("Player 1 wins!",end='')
        else:
            print("Player 2 wins!",end='')
        f"{score1} moves vs {score2} moves"
    else:
        solve(tower1, tower2, tower3, init_num_disks)
