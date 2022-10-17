# recursive towerof hanoi solver 
# move disk n from source to destination move n-1 from source to auxilary 
# move disk n back to auxilary 
# and thats it recuring the above until the the bottom disk solved
def hanoiSolver(n:int,source:str,auxilary:str,destination:str)->None:
    if n> 0:
        hanoiSolver(n-1,source,destination,auxilary)
        print(f"move disk {n-1} from {source} to {destination} ")
        hanoiSolver(n-1,auxilary,destination,source)


hanoiSolver(4,"A","B","C")