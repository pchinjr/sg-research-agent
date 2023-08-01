import csv
import requests
import time

start_time = time.time()

# Open the input and output files.
with open("output_research.csv", "r") as csvinput, open(
    "output_personalized.csv", "w", newline=""
) as csvoutput:
    # Create CSV reader and writer.
    reader = csv.DictReader(csvinput)
    fieldnames = reader.fieldnames + [
        "personalized"
    ]  # Assuming 'personalized' is the additional field for the response
    writer = csv.DictWriter(csvoutput, fieldnames=fieldnames)

    # Write the header to the output file.
    writer.writeheader()

    # Loop over each row in the input file.
    for row in reader:
        # Form the query string
        query = f"""Write an outreach email with a maximum of five sentences. Insert new wording between the “[]” by incorporating the target company information to persuade them to take action. Create a persuasive subject line. Hi {row['First Name']}! We met at the AWS Summit in NYC. We discussed the need for serverless-focused developers and I wanted to highlight how Serverless Guru can help. At Serverless Guru, we understand [company challenges inferred from target summary]. [Customized call to action that includes the company mission and how Serverless Guru can help]. We are dedicated to a serverless-first approach in planning, adopting, migrating, and scaling applications on AWS. Our expertise in serverless architecture and development positions us as an ideal partner to support [company line of business and mission] 
        Thanks so much for your time, and we look forward to solving your toughest challenges. Best, Mason
        Target Company Information: {row['response']}"""
        # Make a POST request with the data in the current row.
        response = requests.post(
            # "https://sg-research-agent.onrender.com", json={"query": query}
            "http://0.0.0.0:3000", json={"query": query}
        )

        # Check if request was successful
        if response.status_code == 200:
            # Add the response to the row.
            row[
                "personalized"
            ] = response.text  # Or any other data from the response you care about
        else:
            row["personalized"] = f"Error: {response.status_code}"

        # Write the updated row to the output file.
        print("writing to output file...")
        writer.writerow(row)

end_time = time.time()

execution_time = end_time - start_time

print(f"The script took {execution_time} seconds to complete.")