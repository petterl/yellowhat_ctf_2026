#!/usr/bin/env python3
import sys
import os
from azure.kusto.data import KustoClient, KustoConnectionStringBuilder
from azure.identity import InteractiveBrowserCredential, TokenCachePersistenceOptions, AuthenticationRecord

cluster = "https://kvc-yw8yk8v588yp26jxxm.northeurope.kusto.windows.net"
database = "BluRavenCTF"

# Path to store authentication record
auth_record_path = os.path.expanduser("~/.azure/bluraven-ctf-auth-record.json")

# Enable persistent token cache
cache_options = TokenCachePersistenceOptions(name="bluraven-ctf-cache")

# Load existing authentication record if available
auth_record = None
if os.path.exists(auth_record_path):
    with open(auth_record_path, "r") as f:
        auth_record = AuthenticationRecord.deserialize(f.read())

# Create credential with cached auth record to skip account picker
credential = InteractiveBrowserCredential(
    cache_persistence_options=cache_options,
    authentication_record=auth_record
)

# If no auth record exists, authenticate and save the record
if auth_record is None:
    auth_record = credential.authenticate(scopes=["https://kusto.kusto.windows.net/.default"])
    os.makedirs(os.path.dirname(auth_record_path), exist_ok=True)
    with open(auth_record_path, "w") as f:
        f.write(auth_record.serialize())

kcsb = KustoConnectionStringBuilder.with_azure_token_credential(cluster, credential)
client = KustoClient(kcsb)

query = sys.argv[1]
response = client.execute(database, query)

for table in response.primary_results:
    columns = [col.column_name for col in table.columns]
    print("\t".join(columns))
    print("-" * 80)
    for row in table:
        print("\t".join(str(val) for val in row))
