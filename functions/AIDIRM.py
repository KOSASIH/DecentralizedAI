from collections import defaultdict

def AIDIRM(nodes, tasks):
    """
    AIDIRM intelligently allocates resources among a set of nodes to complete a set of tasks.

    Parameters:
    nodes (List[Node]): A list of nodes in the decentralized AI ecosystem
    tasks (List[Task]): A list of tasks that need to be completed

    Returns:
    A dict with task ids as keys and node ids as values, indicating which node has been assigned which task
    """

    # Initialize task assignment dict
    task_assignments = defaultdict(str)

    # Sort tasks based on priority
    tasks = sorted(tasks, key=lambda x: x.priority, reverse=True)

    # Loop through all tasks
    for task in tasks:

        # Initialize variables
        available_nodes = [node for node in nodes
                          if node.status == "available"
                          and node.capabilities[task.resource] >= task.requirement]
        min_latency = float("inf")
        best_node = None

        # Find best node for task
        for node in available_nodes:

            # Compute latency
            node_latency = compute_latency(node, task)

            # If latency is better than the best, update
            if node_latency < min_latency:
                min_latency = node_latency
                best_node = node

        # Update task_assignments
        if best_node:
            task_assignments[task.id] = best_node.id
            best_node.allocate(task.resource, task.requirement)
            best_node.status = "busy"

    return task_assignments

