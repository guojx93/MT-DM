import copy
import random

import diffusionModel

def maxDegree(graph, D, registeredUserSet, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding):
    userTotalBid = gererateTotalBid(userBidding, numberOfTask)
    user_degree = {}
    for user in registeredUserSet:
        if userTotalBid[user] == 0:
            continue
        user_degree[user] = len(graph.get_children(user)) / userBidding[user]['unitbid']
    user_degree = sorted(user_degree.items(), key=lambda item: item[1], reverse=True)

    seeds = set()
    currentConsumption = 0
    i = 0
    while seeds != registeredUserSet:
        max_user = user_degree[i][0]
        if currentConsumption + userTotalBid[max_user] > D:
            break
        seeds.add(max_user)
        currentConsumption = currentConsumption + userTotalBid[max_user]
        i += 1
        print("currentConsumption = ", str(currentConsumption), ", MTDiffusion = " + str(
            diffusionModel.computeMultiTaskDiffusion(graph, seeds, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding, 2000)))
    return seeds

def randomm(graph, D, registeredUserSet, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding):
    userTotalBid = gererateTotalBid(userBidding, numberOfTask)
    seeds = set()
    candidate = copy.deepcopy(registeredUserSet)
    candidate = list(candidate)
    currentConsumption = 0
    while seeds != registeredUserSet:
        user = random.choice(candidate)
        candidate.remove(user)
        if userTotalBid[user] == 0:
            continue
        if currentConsumption + userTotalBid[user] > D:
            break
        seeds.add(user)
        currentConsumption = currentConsumption + userTotalBid[user]
        print("currentConsumption = ", str(currentConsumption), ", MTDiffusion = " + str(
            diffusionModel.computeMultiTaskDiffusion(graph, seeds, numberOfTask, taskWeights, qualityOfSubarea,
                                                     userLocation, userBidding, 2000)))
    return seeds

def gererateTotalBid(userBidding, numberOfTask):
    userTotalBid = {}
    for user in userBidding:
        numBiddingTask = 0
        for task in range(1, numberOfTask + 1):
            if userBidding[user][task] == 1:
                numBiddingTask += 1
        userTotalBid[user] = numBiddingTask * userBidding[user]['unitbid']
    return userTotalBid

def greedy(graph, D, registeredUserSet, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding):
    userTotalBid = gererateTotalBid(userBidding, numberOfTask)
    seeds = set()
    currentConsumption = 0
    currentMTDiffution = 0
    while seeds != registeredUserSet:
        candidate = registeredUserSet - seeds
        candidate = list(candidate)
        max_user = 0
        max_marginal_gain = -10000
        for user in candidate:
            if userTotalBid[user] == 0:
                continue
            current_seeds = copy.deepcopy(seeds)
            current_seeds.add(user)
            current_marginal_gain = (diffusionModel.computeMultiTaskDiffusion(graph, current_seeds, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding) - currentMTDiffution) / userTotalBid[user]
            if current_marginal_gain > max_marginal_gain:
                max_user = user
                max_marginal_gain = current_marginal_gain
        if currentConsumption + userTotalBid[max_user] > D:
            break
        seeds.add(max_user)
        currentConsumption = currentConsumption + userTotalBid[max_user]
        currentMTDiffution = diffusionModel.computeMultiTaskDiffusion(graph, seeds, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding, 2000)
        print("currentConsumption = ", str(currentConsumption), ", MTDiffusion = " + str(currentMTDiffution))
    return seeds

def greedyIM(graph, D, registeredUserSet, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding):
    userTotalBid = gererateTotalBid(userBidding, numberOfTask)
    seeds = set()
    currentConsumption = 0
    currentInfluence = 0
    while seeds != registeredUserSet:
        candidate = registeredUserSet - seeds
        candidate = list(candidate)
        max_user = 0
        max_marginal_gain = -10000
        for user in candidate:
            if userTotalBid[user] == 0:
                continue
            current_seeds = copy.deepcopy(seeds)
            current_seeds.add(user)
            current_marginal_gain = (diffusionModel.computeIC(graph, current_seeds) - currentInfluence) / userBidding[user]['unitbid']
            if current_marginal_gain > max_marginal_gain:
                max_user = user
                max_marginal_gain = current_marginal_gain
        if currentConsumption + userTotalBid[max_user] > D:
            break
        seeds.add(max_user)
        currentConsumption = currentConsumption + userTotalBid[max_user]
        currentInfluence = diffusionModel.computeIC(graph, seeds, 2000)
        currentMTDiffution = diffusionModel.computeMultiTaskDiffusion(graph, seeds, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding, 2000)
        print("currentConsumption = ", str(currentConsumption), ", MTDiffusion = " + str(currentMTDiffution))
    return seeds