import collections

class TRM:
    def __init__(self, threshold=0.5):
        self.threshold = threshold
        self.metrics = collections.defaultdict(int)

    def update_metrics(self, node_id, metric):
        """Update the trust and reputation metrics"""
        self.metrics[node_id] += metric

    def evaluate(self, node_id):
        """Evaluate the trustworthiness and reliability of the node"""
        if self.metrics[node_id] > self.threshold * sum(self.metrics.values()):
            return True
        else:
            return False

# Example usage

trm = TRM(threshold=0.5)

# Update the metrics for different nodes

# Node 1 has 5 successful transactions, and 1 failed transaction

for _ in range(5):
    trm.update_metrics('node1', 1)

for _ in range(1):
    trm.update_metrics('node1', -1)

# Node 2 has 10 successful transactions, and no failed transactions

for _ in range(10):
    trm.update_metrics('node2', 1)

# Evaluate the trustworthiness and reliability of the nodes

is_node1_trustworthy = trm.evaluate('node1')

is_node2_trustworthy = trm.evaluate('node2')

# Node 1 is considered less trustworthy and reliable

print(f"Node 1 trustworthy: {is_node1_trustworthy}")

# Node 2 is considered trustworthy and reliable

print(f"Node 2 trustworthy: {is_node2_trustworthy}")
