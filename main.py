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

    #maybe put all of this in some menu/initialize function?
    init_num_disks = int(input("Insert number of disks: "))
    for i in range(init_num_disks,1,-1):
        tower1.append(i)
    #

    solve(tower1, tower2, tower3, init_num_disks)
