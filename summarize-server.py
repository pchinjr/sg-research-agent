import csv
import requests
import time

start_time = time.time()

# Open the input and output files.
with open("NYC_decision_makers.csv", "r") as csvinput, open(
    "output.csv", "w", newline=""
) as csvoutput:
    # Create CSV reader and writer.
    reader = csv.DictReader(csvinput)
    fieldnames = reader.fieldnames + [
        "response"
    ]  # Assuming 'response' is the additional field for the response
    writer = csv.DictWriter(csvoutput, fieldnames=fieldnames)

    # Write the header to the output file.
    writer.writeheader()

    # Loop over each row in the input file.
    for row in reader:
        # Form the query string
        query = f"what is {row['Company']}'s main line of business?"
        print(query)
        # Make a POST request with the data in the current row.
        response = requests.post(
            # "https://sg-research-agent.onrender.com", json={"query": query}
            "http://0.0.0.0:3000", json={"query": query}
        )

        # Check if request was successful
        if response.status_code == 200:
            # Add the response to the row.
            row[
                "response"
            ] = response.text  # Or any other data from the response you care about
        else:
            row["response"] = f"Error: {response.status_code}"

        # Write the updated row to the output file.
        print("writing to output file...")
        writer.writerow(row)

end_time = time.time()

execution_time = end_time - start_time

print(f"The script took {execution_time} seconds to complete.")

# print(
#     requests.post(
#         "https://sg-research-agent.onrender.com",
#         json={
#             "query": "Who is David Lin,	Assistant Director for Information Technology & Operations,	The Frick Collection and what is the company's main line of business?"
#         }
#     ).json()
# )
