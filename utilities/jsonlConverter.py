import json

def convert_llama_to_pf_jsonl(source_file, destination_file):
    # Step 1: Read the Source File
    with open(source_file, "r") as file:
        input_json = json.load(file)

    # Step 2: Conversion Logic
    jsonl_data = [
        {
            "question": example["query"],
            "answer": example["reference_answer"],
            "ground_truth": " ".join(example["reference_contexts"])
        }
        for example in input_json["examples"]
    ]

    # Step 3: Save the Converted JSONL to the Destination
    with open(destination_file, "w") as jsonl_file:
        for item in jsonl_data:
            jsonl_file.write(json.dumps(item) + "\n")
    
    print(f"Conversion complete! JSONL saved to {destination_file}")

# Example usage:
# convert_llama_to_pf_jsonl("input.json", "output.jsonl")
