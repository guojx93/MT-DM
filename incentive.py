import algo_Sampling
import algo_MC
import copy

def MT_DM_L(graph, D, registeredUserSet, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding,
        MTRRSetCollection, totalUserDistribution):
    # winning worker selection stage
    S = algo_Sampling.maxCoverage(graph, D, registeredUserSet, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding,
        MTRRSetCollection, totalUserDistribution)
    print(S)
    # payment determination stage
    userTotalBid = algo_MC.gererateTotalBid(userBidding, numberOfTask)
    P = {}
    for winner in S:
        P[winner] = -10000
        currentRegisteredUserSet = copy.deepcopy(registeredUserSet)
        currentRegisteredUserSet.remove(winner)
        H = set()
        currentConsumption = 0
        MTRRSetCollectionPrime = MTRRSetCollection
        while H != currentRegisteredUserSet:
            candidate = currentRegisteredUserSet - H
            candidate = list(candidate)
            max_user = 0
            max_marginal_gain = -10000
            for user in candidate:
                if userTotalBid[user] == 0:
                    continue
                current_user = set()
                current_user.add(user)
                current_marginal_gain = algo_Sampling.getWeightedCoverage(MTRRSetCollectionPrime, current_user, userBidding, totalUserDistribution) / len(MTRRSetCollection) / userTotalBid[user]
                if current_marginal_gain > max_marginal_gain:
                    max_user = user
                    max_marginal_gain = current_marginal_gain
            H.add(max_user)
            currentConsumption = currentConsumption + userTotalBid[max_user]
            current_winner = set()
            current_winner.add(winner)
            winner_marginal_gain_nonunit = algo_Sampling.getWeightedCoverage(MTRRSetCollectionPrime, current_winner, userBidding, totalUserDistribution) / len(MTRRSetCollection)
            P[winner] = max(P[winner], winner_marginal_gain_nonunit / max_marginal_gain)
            if currentConsumption + userTotalBid[winner] > D:
                break
            MTRRSetCollectionPrime = algo_Sampling.removeCoveredUser(MTRRSetCollectionPrime, max_user, userBidding)
        if currentConsumption + userTotalBid[winner] <= D:
            P[winner] = max(P[winner], D - currentConsumption)
        print("Winner is " + str(winner) + ", its price is " + str(P[winner]) + ", its bid is " + str(userTotalBid[winner]))
    return P