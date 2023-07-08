import tools
import random

def generateRegisterUser(graph, prob):
    registeredUserSet = set()
    for node in graph.nodes:
        if tools.isHappened(prob):
            registeredUserSet.add(node)
    return registeredUserSet

def generateHalfRegisterUser(registeredUserSet):
    halfSet = set()
    i = 0
    for node in registeredUserSet:
        if i % 2 == 0:
            halfSet.add(node)
        i += 1
    return halfSet

def generateLocation(graph, numberOfSubarea):
    userLocation = {}
    for node in graph.nodes:
        userLocation[node] = random.randint(1, numberOfSubarea)
    return userLocation

def generateQualityOfSubarea(numberOfTasks, numberOfSubareas):
    qualityOfSubarea = {}
    for task in range(1, numberOfTasks + 1):
        qualityOfSubarea[task] = {}
        for subarea in range(1, numberOfSubareas + 1):
            qualityOfSubarea[task][subarea] = random.uniform(0, 1)
    return qualityOfSubarea

def generateUserUnitBid(graph):
    userUnitBid = {}
    for user in graph.nodes:
        userUnitBid[user] = random.uniform(0, 1)
    return userUnitBid

def generateUserBidding(graph, numberOfTasks):
    userBidding = {}
    for user in graph.nodes:
        userBidding[user] = {}
        for task in range(1, numberOfTasks + 1):
            userBidding[user][task] = 0
            if tools.isHappened(0.5):
                userBidding[user][task] = 1
        userBidding[user]["unitbid"] = random.uniform(0.8, 1.2)
    return userBidding



if __name__ == '__main__':
    # path = "rt_damascus.edges"
    path = "rt_dash.edges"
    graph = tools.readGraph_direct(path)

    registeredUserSet = generateRegisterUser(graph, 0.2)
    print(registeredUserSet)
    print(len(registeredUserSet))
    print("------------------------")
    # halfSet = generateHalfRegisterUser(registeredUserSet)
    # print(halfSet)
    # print(len(halfSet))

    # userLocation = generateLocation(graph, 100)
    # print(userLocation)

    # qualityOfSubarea = generateQualityOfSubarea(4, 100)
    # print(qualityOfSubarea)

    # userBidding = generateUserBidding(graph, 4)
    # print(userBidding)