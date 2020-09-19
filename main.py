import argparse
import sys

def move(t1, t2):
    t2.append(t1.pop())

def solve(t1, t2, t3, num_disks):
    if num_disks == 3:
        move(t1,t3) #
        render()    #
        move(t1,t2) #
        render()    #
        move(t3,t2) #
        render()    #
        move(t1,t3) #change all these calls somewhat? looks kinda ugly/repetitive
        render()    #if not then put render() inside move? but then I have a function that does 2 separate things :\
        move(t2,t1) #
        render()    #
        move(t2,t3) #
        render()    #
        move(t1,t3) #
        render()    #

    if num_disks > 3:
        solve(t1,t3,t2, num_disks - 1)
        move(t1,t3)
        render()


if __name__ == '__main__':

    tower1 = []
    tower2 = []
    tower3 = []

    parser = argparse.ArgumentParser(description='Number of disks and game mode')
    parser.add_argument('disks_nr',type=int,help='Choose the number of disks (3 or more)')
    parser.add_argument('game_mode', type=int,help='Choose game mode: 1 for player vs player | 2 for player vs computer')

    args = parser.parse_args()

    if args.disks_nr < 3:
        print('\n')
        print('The minimum number of disks is 3, choose a bigger number')
        print('\n')
        sys.exit()

    if args.game_mode !=1 and args.game_mode !=2 :
        print('\n')
        print(args.game_mode,'is not a valid value for game mode, choose 1 or 2')
        print('\n')
        sys.exit()

    init_num_disks = args.disks_nr

    for i in range(init_num_disks,1,-1):
        tower1.append(i)

    if args.game_mode == 1:

        render()

        win = false
        player = 1
        num_moves = 0

        while win == false:
            print("Player", player, "moves \n")

            ok = false

            while ok == false
                inp = int(input("Choose current tower (1 or 2 or 3) : "))

                if inp == 1
                    current = tower1
                if inp == 2
                    current = tower2
                if inp == 3
                    current = tower3

                print("\n")
                inp = input("Choose destination tower (1 or 2 or 3) : ")

                if inp == 1
                    dest = tower1
                if inp == 2
                    dest = tower2
                if inp == 3
                    dest = tower3

                print("\n")

                if current != dest
                    if is_valid(current,dest) == true
                        num_moves++
                        ok = true
                    else
                        invalid_message1()
                else
                    invalid_message2()

            render()

            if len(tower3) == init_num_disks
                win = true
                print("Player", player, " won with ", num_moves, " moves! \n")
                if player == 1
                    player = 2
                else
                    player = 1





    solve(tower1, tower2, tower3, init_num_disks)
