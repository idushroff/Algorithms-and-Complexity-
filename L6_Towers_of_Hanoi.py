def Hanoi(n, init, aux, fin):
    # snapshot(printstack=True)
    if n > 0:
        Hanoi(n - 1, init, fin, aux)  # 1
        #snapshot(printstack=True)
        fin[1].append(init[1].pop()) # move 1 disk from init to fin
        Hanoi(n - 1, aux, init, fin)  # 2
        #snapshot(printstack=True)

# each tower is a pair (name,list) were 'name' is the name of the tower
# and 'list' is the list of disks where the topmost disk is at the end
init = ("left",[4, 3, 2, 1])
fin = ("right",[])
aux = ("middle",[])
# clear_frames()
Hanoi(4, init, aux, fin)
print("Hanoi done. Rendering animation may take some time...")
# show_animation(size=[20,5])