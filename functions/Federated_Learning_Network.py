import collections
import tensorflow as tf
import tensorflow_federated as tff

# Define the model
def create_model():
  model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
  ])
  return model

# Define the metrics
def metrics_fn():
  return collections.OrderedDict(
      num_examples=tf.function(func=lambda x: x[0]),
      loss=tf.function(func=lambda x: x[0] / x[1]),
      accuracy=tf.function(func=lambda x: x[0] / x[1]))

# Define the model structure
MnistModel = tff.learning.models.FromKerasModel(
  model_fn=create_model,
  input_spec=preprocessed_example_dataset.element_spec,
  loss=tf.keras.losses.SparseCategoricalCrossentropy(),
  metrics_fn=metrics_fn)

# Define the Federated Average (FedAvg) training process
fed_avg_process = tff.learning.algorithms.build_weighted_fed_avg(
    model_fn=MnistModel,
    client_optimizer_fn=lambda: tf.keras.optimizers.SGD(learning_rate=0.02))

# Initialize the training state
state = fed_avg_process.initialize()

# Run one round of training with a sample of the federated data
result = fed_avg_process.next(state, federated_train_data)

# Print the training metrics
train_metrics = result.metrics
print('round  1, metrics={}'.format(train_metrics))
