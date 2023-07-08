import tools
import numpy as np
import random
import copy
import algo_MC
import diffusionModel

# methods of Modified-OPIM-C
def reverseSearch(graph, root, task, taskWeights):
    searchSet = set()
    queue = []
    queue.append(root)
    searchSet.add(root)
    while len(queue) != 0:
        current_node = queue.pop(0)
        parentss = graph.get_parentss(current_node)
        for parent in parentss:
            if parent not in searchSet:
                rate = taskWeights[task]
                if tools.isHappened(rate):
                    searchSet.add(parent)
                    queue.append(parent)
    return searchSet

def getUserDistribution(graph, numberOfTask, userLocation, qualityOfSubarea):
    totalUserDistribution = {}
    for task in range(1, numberOfTask + 1):
        totalUserDistribution[task] = {}
        qualitySum = 0
        for user in graph.nodes:
            qualitySum += qualityOfSubarea[task][userLocation[user]]
        totalUserDistribution[task]['qualitySum'] = qualitySum
        userList = []
        userDistribution = []
        for user in graph.nodes:
            userList.append(user)
            userDistribution.append(qualityOfSubarea[task][userLocation[user]] / qualitySum)
        totalUserDistribution[task]['userList'] = userList
        totalUserDistribution[task]['userDistribution'] = userDistribution
    return totalUserDistribution

def generateRRSet(graph, task, taskWeights, totalUserDistribution):
    qualitySum = totalUserDistribution[task]['qualitySum']
    userList = totalUserDistribution[task]['userList']
    userDistribution = totalUserDistribution[task]['userDistribution']
    selectedUser = np.random.choice(userList, p=userDistribution)
    searchSet = reverseSearch(graph, selectedUser, task, taskWeights)
    return searchSet

def gererateMTRRSet(graph, numberOfTask, taskWeights, totalUserDistribution):
    task = random.randint(1, numberOfTask)
    searchSet = generateRRSet(graph, task, taskWeights, totalUserDistribution)
    return (task, searchSet)

def generateMTRRSetCollection(graph, numberOfTask, taskWeights, totalUserDistribution, theta):
    MTRRSetCollection = []
    for i in range(theta):
        MTRRSetCollection.append(gererateMTRRSet(graph, numberOfTask, taskWeights, totalUserDistribution))
    return MTRRSetCollection

def getWeightedCoverage(MTRRSetCollection, seeds, userBidding, totalUserDistribution):
    weightedCoverage = 0
    for MTRRset in MTRRSetCollection:
        task = MTRRset[0]
        RRSet = MTRRset[1]
        task_seeds = set()
        for seed in seeds:
            if userBidding[seed][task] == 1:
                task_seeds.add(seed)
        if not task_seeds.isdisjoint(RRSet):
            weightedCoverage += totalUserDistribution[task]['qualitySum']
    return weightedCoverage

def removeCoveredUser(MTRRSetCollection, max_user, userBidding):
    MTRRSetCollectionPrime = copy.deepcopy(MTRRSetCollection)
    for MTRRset in MTRRSetCollection:
        task = MTRRset[0]
        RRSet = MTRRset[1]
        if userBidding[max_user][task] == 1:
            if max_user in RRSet:
                MTRRSetCollectionPrime.remove(MTRRset)
    return MTRRSetCollectionPrime

def maxCoverage(graph, D, registeredUserSet, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding,
        MTRRSetCollection, totalUserDistribution):
    userTotalBid = algo_MC.gererateTotalBid(userBidding, numberOfTask)
    seeds = set()
    currentConsumption = 0
    MTRRSetCollectionPrime = MTRRSetCollection
    while seeds != registeredUserSet:
        candidate = registeredUserSet - seeds
        candidate = list(candidate)
        max_user = 0
        max_marginal_gain = -10000
        for user in candidate:
            if userTotalBid[user] == 0:
                continue
            current_user = set()
            current_user.add(user)
            current_marginal_gain = getWeightedCoverage(MTRRSetCollectionPrime, current_user, userBidding, totalUserDistribution) / len(MTRRSetCollection) / userTotalBid[user]
            if current_marginal_gain > max_marginal_gain:
                max_user = user
                max_marginal_gain = current_marginal_gain
        if currentConsumption + userTotalBid[max_user] > D:
            break
        # print(getWeightedCoverage(MTRRSetCollection, seeds, userBidding, totalUserDistribution) / len(MTRRSetCollection) + max_marginal_gain * userTotalBid[max_user])
        seeds.add(max_user)
        currentConsumption = currentConsumption + userTotalBid[max_user]
        MTRRSetCollectionPrime = removeCoveredUser(MTRRSetCollectionPrime, max_user, userBidding)
        # estimatedMTDiffusion = getWeightedCoverage(MTRRSetCollection, seeds, userBidding, totalUserDistribution) / len(MTRRSetCollection)
        # MTDiffusion = diffusionModel.computeMultiTaskDiffusion(graph, seeds, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding, 2000)
        # print("currentConsumption = ", str(currentConsumption), ", estimatedMTDiffusion = " + str(estimatedMTDiffusion) + ", MTDiffsion = " + str(MTDiffusion))
    return seeds
