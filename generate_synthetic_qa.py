import csv
import random

# Define Segments
segments = {
    "Chemotherapy Side Effects": [
        ("patient", "What should I do if I get a fever during my chemotherapy?", "Fever during chemo is an emergency. Go to the ER."),
        ("patient", "How can I manage nausea after my chemo session?", "Anti-nausea medications and small, frequent meals help."),
        ("professional", "What are the common hematologic toxicities of AC (Adriamycin/Cytoxan) regimen?", "Neutropenia, anemia, and thrombocytopenia are common. Neutropenia often peaks around days 10-14."),
    ],
    "Targeted Therapies (e.g., Darzalex)": [
        ("patient", "What are the common side effects of Darzalex (daratumumab)?", "Common side effects include fatigue, nausea, diarrhea, and infusion-related reactions. You may also experience upper respiratory tract infections."),
        ("patient", "Can I take my regular blood pressure medication on the day of my Darzalex infusion?", "You should check with your oncologist, but usually, it's fine. Sometimes medications are adjusted before infusion."),
        ("professional", "What premedications are required before Darzalex infusion?", "Premedications typically include an intravenous corticosteroid, an antipyretic, and an antihistamine to reduce the risk of infusion-related reactions."),
    ],
    "Nutrition and Diet during Treatment": [
        ("patient", "What should I eat when I have no appetite due to radiation?", "Try eating small, high-protein, and high-calorie snacks throughout the day. Smoothies and nutritional shakes can also be easier to tolerate."),
        ("patient", "Are there any foods I should avoid during chemotherapy?", "Avoid raw or undercooked meats, unpasteurized dairy, and unwashed fruits/vegetables to prevent infections, especially if your white blood cell count is low."),
        ("professional", "What are the nutritional guidelines for a patient with head and neck cancer undergoing chemoradiation?", "Patients often require a prophylactic gastrostomy tube. Emphasize high-calorie, high-protein soft foods and liquid supplements. Monitor for dysphagia and mucositis."),
    ],
    "Emergency Scenarios": [
        ("patient", "I have sudden chest pain and shortness of breath. What should I do?", "This is a medical emergency. Please call 911 or go to the nearest emergency room immediately."),
        ("patient", "My temperature is 100.5°F (38.1°C) and I had chemo last week. Is this an emergency?", "Yes, any temperature of 100.4°F (38°C) or higher during chemotherapy is considered an emergency. Go to the emergency room or contact your oncologist immediately."),
        ("professional", "What is the initial management for suspected neutropenic fever in an oncology patient?", "Immediate administration of broad-spectrum empiric intravenous antibiotics (e.g., cefepime, meropenem, or piperacillin-tazobactam) within 60 minutes of presentation after obtaining blood cultures."),
    ],
    "General Cancer Knowledge": [
        ("patient", "What does it mean if my cancer is stage 3?", "Stage 3 generally means the cancer is larger and may have spread to nearby tissues or lymph nodes, but hasn't spread to distant parts of the body."),
        ("patient", "What is the difference between chemotherapy and immunotherapy?", "Chemotherapy uses drugs to kill fast-growing cells, including cancer cells. Immunotherapy helps your own immune system recognize and attack cancer cells."),
        ("professional", "Explain the TNM staging system.", "The TNM system evaluates the size and extent of the primary Tumor (T), the number of nearby lymph Nodes (N) that have cancer, and whether the cancer has Metastasized (M) to distant sites."),
    ]
}

system_prompt_patient = "You are a helpful and empathetic medical AI assistant. Answer the user's question clearly and concisely based on the retrieved medical context. Always include this disclaimer: 'I am an AI, not a doctor. Please consult your oncologist or healthcare provider.'"
system_prompt_professional = "You are a specialized medical AI assistant designed for oncology professionals. Provide precise, evidence-based answers using medical terminology based on the retrieved context."

def generate_dataset(num_samples=500, filename="oncology_qa_dataset.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Segment", "Target Audience", "System Prompt", "User Question", "Simulated RAG Context", "Ideal Assistant Response"])

        questions_generated = 0
        while questions_generated < num_samples:
            for segment_name, qa_list in segments.items():
                if questions_generated >= num_samples:
                    break

                # We simply repeat the small seed set with some minor variations or just loop to reach 500
                # In a real scenario, we'd use an LLM or a larger database to generate distinct ones.
                # Here, we will just cycle through to demonstrate the format and volume.
                for audience, question, base_answer in qa_list:
                    if questions_generated >= num_samples:
                        break

                    sys_prompt = system_prompt_patient if audience == "patient" else system_prompt_professional

                    # Add safety guardrails to the base answer for patients
                    if audience == "patient":
                        final_answer = f"{base_answer} I am an AI, not a doctor. Please consult your oncologist."
                    else:
                        final_answer = base_answer

                    # For RAG context, we simulate a retrieved document that contains the answer
                    simulated_context = f"Retrieved Context for {segment_name}: {base_answer}"

                    writer.writerow([segment_name, audience, sys_prompt, question, simulated_context, final_answer])
                    questions_generated += 1

    print(f"Generated {questions_generated} Q&A pairs in {filename}")

if __name__ == "__main__":
    # Generate 500 samples (repeating the seeds)
    generate_dataset(500)
