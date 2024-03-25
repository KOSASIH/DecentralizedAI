# Define the dataset
dataset = bigquery.Dataset(dataset_id)

# Set the project for the dataset
dataset.project = project_id

# Set the location of the dataset
dataset.location = 'US'

# Set the default table expiration
dataset.default_table_expiration_ms = 30 * 24 * 60 * 60 * 1000 # expire in 30 days

# Encrypt the dataset using a customer-managed encryption key
# Note: This requires a Cloud KMS key to be created beforehand
# See: https://cloud.google.com/kms/docs/creating-sa-key
# dataset.kms_key_name = 'projects/{}/locations/{}/keyRings/{}/cryptoKeys/{}'.format(
#     project_id,
#     'us-central1',
#     'your-key-ring',
#     'your-crypto-key'
# )

# Create the dataset
dataset = client.create_dataset(dataset, timeout=30)
print("Dataset {} created.".format(dataset.dataset_id))
