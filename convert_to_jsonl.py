import csv
import json
import argparse

def convert_csv_to_jsonl(input_csv, output_jsonl):
    """
    Converts a CSV of verified Q&A pairs into OpenAI's JSONL format for fine-tuning.
    Expected CSV columns:
    0: Segment
    1: Target Audience
    2: System Prompt
    3: User Question
    4: Simulated RAG Context
    5: Ideal Assistant Response
    """
    converted_count = 0
    with open(input_csv, mode='r', encoding='utf-8') as f_in, open(output_jsonl, mode='w', encoding='utf-8') as f_out:
        reader = csv.reader(f_in)
        header = next(reader)  # Skip header

        for row in reader:
            if len(row) < 6:
                continue

            system_prompt = row[2]
            user_question = row[3]
            rag_context = row[4]
            assistant_response = row[5]

            # Combine the user question and the simulated RAG context into the user message
            user_content = f"Context: {rag_context}\n\nQuestion: {user_question}"

            # OpenAI Chat Completion format
            conversation = {
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content},
                    {"role": "assistant", "content": assistant_response}
                ]
            }

            f_out.write(json.dumps(conversation) + "\n")
            converted_count += 1

    print(f"Successfully converted {converted_count} rows from {input_csv} to {output_jsonl}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert CSV dataset to OpenAI JSONL format.")
    parser.add_argument("--input", type=str, default="oncology_qa_dataset.csv", help="Input CSV file path")
    parser.add_argument("--output", type=str, default="oncology_finetuning.jsonl", help="Output JSONL file path")

    args = parser.parse_args()

    convert_csv_to_jsonl(args.input, args.output)
