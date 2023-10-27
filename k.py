import json

# Your incoming data with single quotes
data_with_single_quotes = "{'bookid': 23, 'dateOfIssued': 'erere'}"

# Remove single quotes from the beginning and end of the string
data = data_with_single_quotes.strip("'")

# Replace single quotes with double quotes
data = data.replace("'", '"')

# Load the JSON data
l = json.loads(data)

print(l)
print("Type of l is", type(l))
