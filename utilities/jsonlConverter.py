import json
import os
import glob
import datetime

def merge_jsonl_files(source_folder, output_folder):
    try:
        # Ensure the source and output folders exist
        if not os.path.exists(source_folder):
            raise FileNotFoundError(f"The source folder '{source_folder}' does not exist.")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Find all .jsonl files in the source folder
        jsonl_files = glob.glob(os.path.join(source_folder, "*.jsonl"))
        if not jsonl_files:
            raise FileNotFoundError("No .jsonl files found in the source folder.")
        
        # Generate output filename based on the current datetime
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"merged_{now}.jsonl"
        output_filepath = os.path.join(output_folder, output_filename)
        
        # Merge all lines from the jsonl files
        with open(output_filepath, 'w', encoding='utf-8') as outfile:
            for file_path in jsonl_files:
                with open(file_path, 'r', encoding='utf-8') as infile:
                    for line in infile:
                        outfile.write(line)
        
        print(f"Successfully merged files into '{output_filepath}'")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# merge_jsonl_files('source_folder_path', 'output_folder_path')


def convert_llama_to_pf_jsonl(source_file, destination_file):
    # Step 1: Read the Source File
    with open(source_file, "r") as file:
        input_json = json.load(file)

    # Step 2: Conversion Logic
    jsonl_data = [
        {
            "question": example["query"],
            "answer": example["reference_answer"],
            "messages": [],
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
