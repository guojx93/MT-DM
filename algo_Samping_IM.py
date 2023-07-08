import random
import tools
import copy
import algo_MC
import diffusionModel

def reverseSearch(graph, root):
    searchSet = set()
    queue = []
    queue.append(root)
    searchSet.add(root)
    while len(queue) != 0:
        current_node = queue.pop(0)
        parentss = graph.get_parentss(current_node)
        for parent in parentss:
            if parent not in searchSet:
                if tools.isHappened(0.4):
                    searchSet.add(parent)
                    queue.append(parent)
    return searchSet

def generateRRSet(graph):
    selectedUser = random.choice(list(graph.nodes))
    searchSet = reverseSearch(graph, selectedUser)
    return searchSet

def generateRRSetCollection(graph, theta):
    RRSetCollection = []
    for i in range(theta):
        RRSetCollection.append(generateRRSet(graph))
    return RRSetCollection

def getCoverage(RRSetCollection, seeds):
    Coverage = 0
    for RRset in RRSetCollection:
        if not seeds.isdisjoint(RRset):
            Coverage += 1
    return Coverage

def removeCoveredUser(RRSetCollection, seeds):
    RRSetCollectionPrime = copy.deepcopy(RRSetCollection)
    for RRset in RRSetCollection:
        if not seeds.isdisjoint(RRset):
            RRSetCollectionPrime.remove(RRset)
    return RRSetCollectionPrime

def maxCoverage(graph, D, registeredUserSet, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding,
        RRSetCollection):
    userTotalBid = algo_MC.gererateTotalBid(userBidding, numberOfTask)
    seeds = set()
    currentConsumption = 0
    RRSetCollectionPrime = RRSetCollection
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
            current_marginal_gain = getCoverage(RRSetCollectionPrime, current_user) / userBidding[user]['unitbid']
            if current_marginal_gain > max_marginal_gain:
                max_user = user
                max_marginal_gain = current_marginal_gain
        if currentConsumption + userTotalBid[max_user] > D:
            break
        seeds.add(max_user)
        currentConsumption = currentConsumption + userTotalBid[max_user]
        RRSetCollectionPrime = removeCoveredUser(RRSetCollectionPrime, seeds)
        MTDiffusion = diffusionModel.computeMultiTaskDiffusion(graph, seeds, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding, 2000)
        print("currentConsumption = ", str(currentConsumption), ", MTDiffsion = " + str(MTDiffusion))
    return seeds