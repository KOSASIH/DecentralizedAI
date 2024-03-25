class Agent:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.best_position = position
        self.best_fitness = objective(position)

    def update_velocity(self, neighbor_best_position, personal_best_position, global_best_position, alpha=2, beta=2):
        v_new = []
        for dim in range(len(self.position)):
            v_dim = (alpha * (personal_best_position[dim] - self.position[dim]) + 
                     beta * (global_best_position[dim] - self.position[dim]) + 
                     self.velocity[dim])
            v_new.append(max(min(v_dim, objective.max_velocity), -objective.max_velocity))
        self.velocity = v_new

    def update_position(self, objective):
        "Update and return the new position."
        self.position = [position + velocity for position, velocity in zip(self.position, self.velocity)]
        self.best_position = min(self.best_position, self.position, key=lambda p: objective(p))

def ScalableAI_SwarmOptimization(agents, num_iterations, objective, objective.max_velocity==10):
    """
    A generic function for conducting scalable swarm optimization.

    Parameters:
        agents (List[Agent]): A list of Agent objects representing the population of agents in the swarm.
        num_iterations (int): Number of iterations for the swarm optimization.
        objective (Callable): The objective function to optimize.

    Returns:
        A tuple of the best agent position, best fitness value, and optimized agent positions.

    """

    global_best_position = agents[0].best_position
    global_best_fitness = objective(global_best_position)

    for iteration in range(num_iterations):
        for agent in agents:
            agent.update_velocity(neighbor_best_position, agent.best_position, global_best_position)
            agent.update_position(objective)

        if objective(agents[0].best_position) < global_best_fitness:
            global_best_position = agents[0].best_position
            global_best_fitness = objective(global_best_position)

    best_positions = [agent.best_position for agent in agents]

    return global_best_position, global_best_fitness, best_positions
