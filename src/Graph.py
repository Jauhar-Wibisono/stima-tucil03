def euclidianDistance(cor1,cor2):
    return ((cor1[0]-cor2[0])**2 + (cor1[1]-cor2[1])**2)**0.5

class Graph:
    def __init__(self, nodes=[], adjacencyMatrix=[]):
        self.__nbNodes = len(nodes)
        self.__nodeNames = []
        self.__idNodes = {}
        self.__coordinates = []
        for i in range (self.__nbNodes):
            self.__nodeNames.append(nodes[i][0])
            self.__idNodes[nodes[i][0]] = i
            self.__coordinates.append((nodes[i][1], nodes[i][2]))
        self.__adjacencyMatrix = [[-1 for i in range (self.__nbNodes)] for j in range (self.__nbNodes)]
        self.__adjacencyList = [[] for i in range (self.__nbNodes)]
        for i in range (self.__nbNodes):
            for j in range (self.__nbNodes):
                if adjacencyMatrix[i][j]>0:
                    distance = euclidianDistance(self.__coordinates[i], self.__coordinates[j])
                    self.__adjacencyMatrix[i][j] = distance
                    self.__adjacencyList[i].append((j, distance))
            #print(self.__adjacencyMatrix[i])

    def nbNodes(self):
        return self.__nbNodes
    def nodes(self):
        toReturn = []
        for i in range (self.__nbNodes):
            toReturn.append([self.__nodeNames[i], self.__coordinates[i][0], self.__coordinates[i][1]])
        return toReturn
    def idNodes(self):
        return self.__idNodes
    def adjacencyMatrix(self):
        toReturn = []
        return self.__adjacencyMatrix
    def adjacencyList(self):
        return self.__adjacencyList
    def edgeList(self):
        edgeCoordinates = []
        for i in range (self.__nbNodes):
            for j in range (i):
                #print(self.__adjacencyMatrix[i][j], end = " ")
                if (self.__adjacencyMatrix[i][j] >= 0):
                    edgeCoordinates.append([self.__coordinates[i][0], self.__coordinates[i][1], self.__coordinates[j][0], self.__coordinates[j][1]])
            #print()
        return edgeCoordinates
    
    def addNode(self, newNode):
        self.__nodeNames.append(newNode[0])
        self.__idNodes[newNode[0]] = self.__nbNodes
        self.__coordinates.append((newNode[1], newNode[2]))
        self.__adjacencyList.append([])
        for i in range (self.__nbNodes):
            self.__adjacencyMatrix[i].append(-1)
        self.__adjacencyMatrix.append([])
        self.__nbNodes += 1
        for i in range (self.__nbNodes):
            self.__adjacencyMatrix[self.__nbNodes-1].append(-1)
    
    def addEdgebyID(self, id1, id2):
        distance = euclidianDistance(self.__coordinates[id1], self.__coordinates[id2])
        if(self.__adjacencyMatrix[id1][id2]<0):
            self.__adjacencyMatrix[id1][id2] = distance
            self.__adjacencyMatrix[id2][id1] = distance
            self.__adjacencyList[id1].append((id2, distance))
            self.__adjacencyList[id2].append((id1, distance))

    def addEdge(self, node1, node2):
        if (node1 in self.__idNodes.keys()) and (node2 in self.__idNodes.keys()):
            id1 = self.__idNodes[node1]
            id2 = self.__idNodes[node2]
            self.addEdgebyID(id1, id2)

    def AstarbyID(self, idfrom, idto, isUsingAM):
        visited = [False for i in range (self.__nbNodes)]
        visitedFrom = [-1 for i in range (self.__nbNodes)]#belum ada yang dikunjungi
        totalDistance = [-1 for i in range (self.__nbNodes)]
        distanceTo = [euclidianDistance(self.__coordinates[i], self.__coordinates[idto]) for i in range (self.__nbNodes)]
        PQPosition = [-1 for i in range (self.__nbNodes)]
        
        totalDistance[idfrom] = 0
        PQPosition[idfrom] = 0
        PQ = [idfrom] #Nilai awal dari PriorityQueue
        visitedEdges = []
        head = 0
        while(head < len(PQ) and PQ[head] != idto):
            visited[PQ[head]] = True
            if(isUsingAM):
                for i in range (self.__nbNodes):
                    if(self.__adjacencyMatrix[PQ[head]][i] >= 0) and not(visited[i]):
                        if(totalDistance[i] < 0):
                            visitedFrom[i] = PQ[head]
                            totalDistance[i] = totalDistance[PQ[head]] + self.__adjacencyMatrix[PQ[head]][i]
                            PQPosition[i] = len(PQ)
                            PQ.append(i)
                            toFront = True
                            while(PQPosition[i]-1>head) and (toFront):
                                inFront = PQ[PQPosition[i]-1]
                                if (totalDistance[i] + distanceTo[i] < totalDistance[inFront] + distanceTo[inFront]):
                                    PQPosition[i] -= 1
                                    PQPosition[inFront] += 1
                                    PQ[PQPosition[i]] = i
                                    PQ[PQPosition[inFront]] = inFront
                                else:
                                    toFront = False
                        elif (totalDistance[PQ[head]] + self.__adjacencyMatrix[PQ[head]][i] < totalDistance[i]):
                            visitedFrom[i] = PQ[head]
                            totalDistance[i] = totalDistance[PQ[head]] + self.__adjacencyMatrix[PQ[head]][i]
                            toFront = True
                            while(PQPosition[i]-1>head) and (toFront):
                                inFront = PQ[PQPosition[i]-1]
                                if (totalDistance[i] + distanceTo[i] < totalDistance[inFront] + distanceTo[inFront]):
                                    PQPosition[i] -= 1
                                    PQPosition[inFront] += 1
                                    PQ[PQPosition[i]] = i
                                    PQ[PQPosition[inFront]] = inFront
                                else:
                                    toFront = False
            else:
                for neighbor in self.__adjacencyList[PQ[head]]:
                    i = neighbor[0]
                    distance = neighbor[1]
                    if(not(visited[i])):
                        if(totalDistance[i] < 0):
                            visitedFrom[i] = PQ[head]
                            totalDistance[i] = totalDistance[PQ[head]] + distance
                            PQPosition[i] = len(PQ)
                            PQ.append(i)
                            toFront = True
                            while(PQPosition[i]-1>head) and (toFront):
                                inFront = PQ[PQPosition[i]-1]
                                if (totalDistance[i] + distanceTo[i] < totalDistance[inFront] + distanceTo[inFront]):
                                    PQPosition[i] -= 1
                                    PQPosition[inFront] += 1
                                    PQ[PQPosition[i]] = i
                                    PQ[PQPosition[inFront]] = inFront
                                else:
                                    toFront = False
                        elif (totalDistance[PQ[head]] + distance < totalDistance[i]):
                            visitedFrom[i] = PQ[head]
                            totalDistance[i] = totalDistance[PQ[head]] + distance
                            toFront = True
                            while(PQPosition[i]-1>head) and (toFront):
                                inFront = PQ[PQPosition[i]-1]
                                if (totalDistance[i] + distanceTo[i] < totalDistance[inFront] + distanceTo[inFront]):
                                    PQPosition[i] -= 1
                                    PQPosition[inFront] += 1
                                    PQ[PQPosition[i]] = i
                                    PQ[PQPosition[inFront]] = inFront
                                else:
                                    toFront = False
            head+=1
        path = []
        if(head < len(PQ)):
            node = idto
            path.append(node)
            while(node != idfrom):
                node = visitedFrom[node]
                path.append(node)
            path.reverse()
        return {"path": path, "distance": totalDistance[idto]}
    
    def Astar(self, nodeto, nodefrom, isUsingAM):
        idto = self.__idNodes[nodeto]
        idfrom = self.__idNodes[nodefrom]
        return self.AstarbyID(idto, idfrom, isUsingAM)

        


    