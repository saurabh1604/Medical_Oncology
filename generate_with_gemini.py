import csv
import json
import os
import argparse
from google import genai

# Define specific segments focused on Medical Oncology and Patient Care
segments = [
    "Medical Oncology: Systemic Chemotherapy",
    "Medical Oncology: Targeted Therapies & Immunotherapy",
    "Medical Oncology: Hormonal Therapy",
    "Patient Care: Side Effect & Symptom Management",
    "Patient Care: Palliative Care & Quality of Life",
    "Patient Care: Psychosocial & Emotional Support"
]

system_prompt_patient = "You are a helpful, highly educated, and empathetic medical AI assistant. Provide detailed, structured, and informative answers using formatting like bullet points when appropriate. Always append this disclaimer at the very end of your answer: 'I am an AI, not a doctor. Please consult your oncologist or healthcare provider for personalized medical advice.'"
system_prompt_professional = "You are a specialized medical AI assistant designed for oncology professionals. Provide precise, comprehensive, and evidence-based answers using medical terminology based on the retrieved context."

def generate_batch_with_gemini(client, segment, num_pairs=10):
    """
    Calls the Gemini API to generate a batch of unique, high-quality Q&A pairs
    for a specific oncology segment. Returns a list of dictionaries.
    """

    prompt = f"""
    You are an expert oncology data curator. Your task is to generate exactly {num_pairs} completely unique, highly detailed, and accurate medical Q&A pairs focused exclusively on the topic of '{segment}'.

    The questions should be realistic questions that would be asked in a clinical oncology setting.
    Half of the questions should be from the perspective of a 'patient' (asking about their care, side effects, or treatments).
    Half of the questions should be from the perspective of a 'professional' (e.g., another doctor or nurse asking about mechanisms of action, guidelines, or specific regimens).

    The answers MUST be long-form, highly detailed, educational, and structured (using bullet points where appropriate). Do not just give a one-sentence answer.

    Return the output STRICTLY as a valid JSON array of objects.
    Do NOT include any markdown formatting blocks (like ```json), just return the raw JSON string.
    Each object must have exactly these keys:
    - "audience": either "patient" or "professional"
    - "question": the detailed question
    - "answer": the comprehensive, bulleted, educational answer
    """

    print(f"Requesting {num_pairs} pairs for segment: {segment}...")

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                temperature=0.7,
                response_mime_type="application/json",
            ),
        )

        # Parse the JSON response
        qa_pairs = json.loads(response.text)
        return qa_pairs

    except Exception as e:
        print(f"Error generating content for {segment}: {e}")
        return []

def main(api_key, total_target=300, output_file="oncology_qa_dataset_gemini.csv"):
    client = genai.Client(api_key=api_key)

    pairs_per_segment = total_target // len(segments)
    batch_size = 10 # Generate in batches of 10 to ensure high quality and avoid timeouts

    total_generated = 0

    # Open CSV in write mode
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Segment", "Target Audience", "System Prompt", "User Question", "Simulated RAG Context", "Ideal Assistant Response"])

        for segment in segments:
            segment_count = 0
            retries = 0
            max_retries = 3

            while segment_count < pairs_per_segment:
                current_batch_size = min(batch_size, pairs_per_segment - segment_count)

                qa_batch = generate_batch_with_gemini(client, segment, current_batch_size)

                if not qa_batch:
                    retries += 1
                    print(f"Skipping batch due to error... (Retry {retries}/{max_retries})")
                    if retries >= max_retries:
                        print(f"Max retries reached for segment '{segment}'. Moving to next segment.")
                        break
                    continue

                # Reset retries on success
                retries = 0

                for qa in qa_batch:
                    audience = qa.get("audience", "patient").lower()
                    question = qa.get("question", "")
                    base_answer = qa.get("answer", "")

                    if not question or not base_answer:
                        continue

                    sys_prompt = system_prompt_patient if audience == "patient" else system_prompt_professional

                    # Add safety guardrails to the base answer for patients
                    if audience == "patient":
                        final_answer = f"{base_answer}\n\n*Disclaimer: I am an AI, not a doctor. Please consult your oncologist or healthcare provider for personalized medical advice.*"
                    else:
                        final_answer = base_answer

                    # For RAG context, we simulate a retrieved document that contains the exact high-quality answer
                    simulated_context = f"Retrieved Medical Guidelines for {segment}: {base_answer}"

                    writer.writerow([segment, audience, sys_prompt, question, simulated_context, final_answer])

                    segment_count += 1
                    total_generated += 1

                print(f"  Progress: {segment_count}/{pairs_per_segment} pairs for '{segment}'")

    print(f"\nSuccessfully generated {total_generated} unique Q&A pairs in {output_file} using Gemini!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate comprehensive oncology dataset using Gemini API.")
    parser.add_argument("--api_key", type=str, help="Your Gemini API Key (or set GEMINI_API_KEY environment variable)")
    parser.add_argument("--target", type=int, default=300, help="Total number of unique Q&A pairs to generate")
    parser.add_argument("--output", type=str, default="oncology_qa_dataset_gemini.csv", help="Output CSV file path")

    args = parser.parse_args()

    # Prioritize command line arg, fallback to env var
    api_key = args.api_key or os.environ.get("GEMINI_API_KEY")

    if not api_key:
        print("Error: You must provide a Gemini API key. Use --api_key or set the GEMINI_API_KEY environment variable.")
        print("Example: python generate_with_gemini.py --api_key YOUR_API_KEY_HERE")
        exit(1)

    main(api_key, args.target, args.output)
