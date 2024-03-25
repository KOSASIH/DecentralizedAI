from google.cloud import bigquery

# Instantiate a BigQuery client
client = bigquery.Client()

# Replace the values below with your specific project and dataset information
project_id = 'your-project-id'
dataset_id = 'your-dataset-id'

# Define the dataset
dataset = bigquery.Dataset(dataset_id)

# Set the project for the dataset
dataset.project = project_id

# Create the dataset
dataset = client.create_dataset(dataset, timeout=30)
print("Dataset {} created.".format(dataset.dataset_id))
