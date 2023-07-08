import tools
import algo_MC
import diffusionModel
import setting_task
import setting_damascus
import setting_dash
import time
import algo_Sampling
import algo_Samping_IM
import incentive

taskWeights = setting_task.taskWeights
qualityOfSubarea = setting_task.qualityOfSubarea
registeredUserSet = setting_dash.registeredUserSet20
userLocation = setting_dash.userLocation
userBidding = setting_dash.userBidding

numberOfTask = 3

if __name__ == '__main__':
    # path = "rt_damascus.edges"
    path = "rt_dash.edges"
    print(path)
    graph = tools.readGraph_direct(path)
    print("registeredUserSet = 20%")
    print("numberOfTask = " + str(numberOfTask))
    D = 50

    # print("Greedy")
    # time_start = time.time()
    # seeds = algo_MC.greedy(graph, D, registeredUserSet, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding)
    # time_end = time.time()
    # print('totally cost', time_end - time_start)
    # print("-------------------------")

    # print("GreedyIM")
    # time_start = time.time()
    # seeds = algo_MC.greedyIM(graph, D, registeredUserSet, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding)
    # time_end = time.time()
    # print('totally cost', time_end - time_start)
    # print("-------------------------")

    # print("maxDegree")
    # seeds = algo_MC.maxDegree(graph, D, registeredUserSet, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding)
    # print("-------------------------")
    #
    # print("random")
    # seeds = algo_MC.randomm(graph, D, registeredUserSet, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding)
    # print("-------------------------")

    # From now on, it is sampling-based methods
    # theta = Modified-OPIM-C()
    # The theta can be obtained by using MT-RR Set in OPIM-C algorithm with constraint K
    # Tang, J., Tang, X., Xiao, X., & Yuan, J. (2018, May). Online processing algorithms for influence maximization. In Proceedings of the 2018 International Conference on Management of Data (pp. 991-1005).

    # Modified-OPIM-C
    totalUserDistribution = algo_Sampling.getUserDistribution(graph, numberOfTask, userLocation, qualityOfSubarea)
    MTRRSetCollection = algo_Sampling.generateMTRRSetCollection(graph, numberOfTask, taskWeights, totalUserDistribution, theta)
    # Check unbiased Estimation
    # seeds1 = {2914, 776, 460, 2256, 755, 1943}
    # seeds2 = {256, 2945, 2914, 774, 776, 460, 2256, 1970, 755, 1943}
    # estimatedMTDiffusion = algo_Sampling.getWeightedCoverage(MTRRSetCollection, seeds2, userBidding, totalUserDistribution) / len(MTRRSetCollection)
    # print(estimatedMTDiffusion)
    # MTDiffusion = diffusionModel.computeMultiTaskDiffusion(graph, seeds2, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding, 3000)
    # print(MTDiffusion)

    # print('Modified-OPIM-C')
    # time_start = time.time()
    # seeds = algo_Sampling.maxCoverage(graph, D, registeredUserSet, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding,
    #     MTRRSetCollection, totalUserDistribution)
    # time_end = time.time()
    # print('totally cost', time_end - time_start)
    # print("-------------------------")

    # OPIM-C
    # RRSetCollection = algo_Samping_IM.generateRRSetCollection(graph, theta)
    # Check unbiased Estimation
    # seeds1 = {2914, 776, 460, 2256, 755, 1943}
    # seeds2 = {256, 2945, 2914, 774, 776, 460, 2256, 1970, 755, 1943}
    # estimatedInfluence = algo_Samping_IM.getCoverage(RRSetCollection, seeds2) / len(RRSetCollection) * len(graph.nodes)
    # print(estimatedInfluence)
    # influence = diffusionModel.computeIC(graph, seeds2, 3000)
    # print(influence)

    # print('OPIM-C')
    # seeds = algo_Samping_IM.maxCoverage(graph, D, registeredUserSet, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding,
    #     RRSetCollection)
    # print("-------------------------")

    # From now on, we begin to verify the incentive mechanism
    userTotalBid = algo_MC.gererateTotalBid(userBidding, numberOfTask)
    P = incentive.MT_DM_L(graph, D, registeredUserSet, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding,
        MTRRSetCollection, totalUserDistribution)
    print("---------------------------")
    print("winner ID:")
    for winner in P:
        print(winner)
    print("---------------------------")
    print("price:")
    for winner in P:
        print(P[winner])
    print("---------------------------")
    print("bid:")
    for winner in P:
        print(userTotalBid[winner])