from SortedSet.sorted_set import SortedSet

def refresh():
    global nbNodes
    global coordinates
    global adjacencyList
    global adjacencyMatrix 
    nbNodes = 0
    coordinates = []
    adjacencyList = []
    adjacencyMatrix = []

def euclidianDistance(cor1,cor2):
    return ((cor1[0]-cor2[0])**2 + (cor1[1]-cor2[1])**2)**0.5

#Menambahkan node berkoordinat (x,y)
def addNode(x,y):
    global nbNodes
    global coordinates
    global adjacencyList
    global adjacencyMatrix
    coordinates.append((x,y))
    adjacencyList.append([])
    for i in range (nbNodes):
        adjacencyMatrix[i].append(-1)
    adjacencyMatrix.append([])
    nbNodes += 1
    for i in range (nbNodes):
        adjacencyMatrix[nbNodes-1].append(-1)

def addEdge(id1, id2):
    global nbNodes
    global coordinates
    global adjacencyList
    global adjacencyMatrix 
    distance = euclidianDistance(coordinates[id1], coordinates[id2])
    adjacencyList[id1].append((id2, distance))
    adjacencyList[id2].append((id1, distance))
    adjacencyMatrix[id1][id2] = distance
    adjacencyMatrix[id2][id1] = distance

def Astar(idfrom, idto, isUsingAdjacencyMatrix):
    global nbNodes
    global coordinates
    global adjacencyList
    global adjacencyMatrix 
    visited = [False for i in range (nbNodes)]
    visitedfrom = [-1 for i in range (nbNodes)]
    totalDistance = [-1 for i in range (nbNodes)]

    totalDistance[idfrom] = 0
    ss = SortedSet([(euclidianDistance(coordinates[idfrom], coordinates[idto]), idfrom)])
    while(len(ss) > 0 and not(visited[idto])):
        expandNode = ss[0]
        ss.discard(expandNode)
        expandID = expandNode[1]
        #debug
        print(expandNode)
        visited[expandID] = True
        if(isUsingAdjacencyMatrix):
            for i in range (nbNodes):
                if adjacencyMatrix[expandID][i] > 0 and not(visited[i]):
                    if totalDistance[i] < 0:
                        totalDistance[i] = totalDistance[expandID] + adjacencyMatrix[expandID][i]
                        ss.add((euclidianDistance(coordinates[i], coordinates[idto])  + totalDistance[i], i))
                        visitedfrom[i] = expandID
                    elif totalDistance[expandID] + adjacencyMatrix[expandID][i] < totalDistance[i]:
                        ss.discard((euclidianDistance(coordinates[i], coordinates[idto])  + totalDistance[i], i))
                        totalDistance[i] = totalDistance[expandID] + adjacencyMatrix[expandID][i]
                        ss.add((euclidianDistance(coordinates[i], coordinates[idto])  + totalDistance[i], i))
                        visitedfrom[i] = expandID
        else:
            for i in range (len(adjacencyList[expandID])):
                visitedID = adjacencyList[expandID][i][0]
                distance = adjacencyList[expandID][i][1]
                if not(visited[visitedID]):
                    if totalDistance[visitedID] < 0:
                        totalDistance[visitedID] = totalDistance[expandID] + distance
                        ss.add((euclidianDistance(coordinates[visitedID], coordinates[idto]) + totalDistance[visitedID], visitedID))
                        visitedfrom[visitedID] = expandID
                    elif totalDistance[expandID] + distance < totalDistance[visitedID]:
                        ss.discard((euclidianDistance(coordinates[visitedID], coordinates[idto]) + totalDistance[visitedID], visitedID))
                        totalDistance[visitedID] = totalDistance[expandID] + distance
                        ss.add((euclidianDistance(coordinates[visitedID], coordinates[idto]) + totalDistance[visitedID], visitedID))
                        visitedfrom[visitedID] = expandID

    if(visited[idto]):
        toReturn = [idto]
        ID = idto
        while(ID != idfrom):
            ID = visitedfrom[idto]
            toReturn.append(ID)
        toReturn.reverse()
        return toReturn
    else:
        return [] 
