import tools
import copy

def diffusionTransform(userSet, task, qualityOfSubarea, userLocation):
    taskDiffusion = 0
    for user in userSet:
        subarea = userLocation[user]
        taskDiffusion += qualityOfSubarea[task][subarea]
    return taskDiffusion

def computeIC(graph, seeds, R=500):
    influence = 0
    for i in range(R):
        queue = []
        queue.extend(seeds)
        checked = copy.deepcopy(seeds)
        while len(queue) != 0:
            current_node = queue.pop(0)
            children = graph.get_children(current_node)
            for child in children:
                if child not in checked:
                    if tools.isHappened(0.4):
                        checked.add(child)
                        queue.append(child)
        influence += len(checked)
    influence = influence/R
    return influence

def computeMultiTaskDiffusion(graph, seeds, numberOfTask, taskWeights, qualityOfSubarea, userLocation, userBidding, R=500):
    multiTaskDiffusion = 0
    for i in range(R):
        averageRealDiffusion = 0
        for task in range(1, numberOfTask + 1):
            task_seeds = set()
            for seed in seeds:
                if userBidding[seed][task] == 1:
                    task_seeds.add(seed)
            queue = []
            queue.extend(task_seeds)
            checked = copy.deepcopy(task_seeds)
            while len(queue) != 0:
                current_node = queue.pop(0)
                children = graph.get_children(current_node)
                for child in children:
                    if child not in checked:
                        rate = taskWeights[task]
                        if tools.isHappened(rate):
                            checked.add(child)
                            queue.append(child)
            taskDiffusion = diffusionTransform(checked, task, qualityOfSubarea, userLocation)
            averageRealDiffusion += taskDiffusion / numberOfTask
        multiTaskDiffusion += averageRealDiffusion
    multiTaskDiffusion = multiTaskDiffusion / R
    return multiTaskDiffusion