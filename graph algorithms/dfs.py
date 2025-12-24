from typing import Dict,List 
graph={"a":["b","c"],"b":["E","F"],"C":["D","G"]}

def DFS(graph:Dict[str,List], goal:str,start:str)->bool:
    visited=[start]
    while visited:
        key=visited.pop()
        print(key)
        if key==goal:
            return True 
        else:
            if graph.__contains__(key):
                for child in reversed(graph[key]):
                    visited.append(child)

        
    return False
DFS(graph,"F",'a')