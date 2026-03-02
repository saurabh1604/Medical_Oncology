import csv

# Massive Hardcoded Unique Batch (Expanded Categories)
segments = {
    "General Cancer Knowledge": [
        ("patient", "What are the symptoms of cancer?",
         "The symptoms of cancer can vary depending on the type and stage of cancer. However, some common symptoms include:\n"
         "- Unexplained weight loss\n"
         "- Fatigue or weakness\n"
         "- Changes in skin color or appearance\n"
         "- Persistent pain or discomfort\n"
         "- Unexplained bruising or bleeding\n"
         "- Unexplained growths or lumps\n"
         "- Changes in bowel or bladder habits\n"
         "- Shortness of breath or difficulty breathing\n"
         "- Unexplained loss of appetite or nausea\n\n"
         "If you or someone you know is experiencing any of these symptoms persistently, it is important to seek medical attention immediately."),
        ("patient", "How can I prevent cancer?",
         "There are several ways to reduce your risk of developing cancer:\n"
         "- Quit smoking and avoid secondhand smoke\n"
         "- Maintain a healthy weight\n"
         "- Eat a balanced diet rich in fruits, vegetables, whole grains, and lean proteins\n"
         "- Exercise regularly\n"
         "- Limit alcohol consumption\n"
         "- Avoid exposure to harmful chemicals and radiation\n"
         "- Get vaccinated for certain cancers, such as the human papillomavirus (HPV) vaccine\n"
         "- Practice sun protection and avoid excessive sun exposure\n\n"
         "It is also important to undergo regular cancer screenings, such as mammograms, colonoscopies, and prostate exams, as recommended by your healthcare provider."),
        ("patient", "What are the different types of cancer?",
         "There are over 100 different types of cancer, each with its own unique characteristics and treatment options. Some common types of cancer include:\n"
         "- Breast cancer\n"
         "- Prostate cancer\n"
         "- Colorectal cancer (colon and rectal cancer)\n"
         "- Lung cancer\n"
         "- Skin cancer\n"
         "- Brain cancer\n"
         "- Leukemia\n\n"
         "Each type of cancer has its own risk factors, symptoms, and treatment options. It is important to consult with a healthcare professional for personalized information and guidance."),
        ("patient", "How long does cancer treatment typically take?",
         "The duration of cancer treatment can vary depending on the type and stage of cancer, as well as the individual's overall health and response to treatment. Some types of cancer may require surgery, chemotherapy, radiation therapy, or a combination of these treatments. The length of treatment can range from a few weeks to several months or even years.\n\n"
         "It is important to work closely with your healthcare team to determine the most appropriate treatment plan and to monitor your progress throughout the treatment process."),
        ("patient", "How can I stay informed about cancer research and treatment advancements?",
         "Staying informed about cancer research and treatment advancements is crucial for individuals and their loved ones. Here are some ways to stay up-to-date:\n"
         "- Follow reputable cancer organizations and organizations dedicated to cancer research and advocacy\n"
         "- Subscribe to newsletters and publications related to cancer\n"
         "- Attend cancer support groups and events\n"
         "- Connect with healthcare professionals and researchers in the field\n"
         "- Participate in clinical trials and studies\n"
         "- Engage in online forums and social media communities\n\n"
         "By staying informed, you can better understand the latest research and treatment options, and make informed decisions about your health and well-being."),
        ("professional", "What is the TNM staging system in oncology?",
         "The TNM staging system is globally recognized for determining the extent of cancer spread. It evaluates three key components:\n"
         "- **T (Tumor):** Refers to the size, extent, and invasion depth of the primary tumor (T1-T4, with T0 indicating no evidence of primary tumor, and Tis indicating carcinoma in situ).\n"
         "- **N (Nodes):** Describes the degree of regional lymph node involvement (N0-N3, reflecting the number or location of affected nodes).\n"
         "- **M (Metastasis):** Indicates whether distant metastasis is present (M0 means none, M1 means metastasis is present).\n\n"
         "These values are combined to assign an overall stage grouping (Stage I through IV), which dictates the prognostic outlook and therapeutic strategy."),
        ("patient", "What does it mean if my cancer is metastatic?",
         "When cancer is described as 'metastatic,' it means that the cancer cells have spread from the original (primary) site where they first formed to other parts of the body. \n"
         "- This spread occurs when cancer cells travel through the bloodstream or the lymphatic system.\n"
         "- Metastatic cancer has the same name and the same type of cancer cells as the original, primary cancer. For example, breast cancer that spreads to the lungs is called metastatic breast cancer, not lung cancer.\n"
         "- Treatment for metastatic cancer often involves systemic therapies (like chemotherapy, hormone therapy, or immunotherapy) that can reach cancer cells throughout the entire body."),
        ("patient", "What is a biopsy and why is it necessary?",
         "A biopsy is a medical procedure in which a doctor removes a small sample of tissue or cells from your body so they can be examined under a microscope. It is necessary for several critical reasons:\n"
         "- **Confirmation:** It is the only definitive way to diagnose most types of cancer.\n"
         "- **Cancer Typing:** It allows pathologists to determine exactly what type of cancer cells are present.\n"
         "- **Grading:** It helps determine how abnormal the cells look and how quickly the cancer is likely to grow and spread.\n"
         "- **Receptor Testing:** The sample can be tested for specific genetic mutations or hormone receptors, which is crucial for determining if targeted therapies or immunotherapies will be effective."),
        ("professional", "How are tumor markers utilized in clinical oncology?",
         "Tumor markers are biological substances, typically proteins, produced by cancer cells or by the body in response to cancer. They are utilized in several clinical contexts:\n"
         "- **Screening and Diagnosis:** While rarely diagnostic on their own due to low specificity, they can aid in diagnosis (e.g., PSA for prostate cancer).\n"
         "- **Prognosis:** Elevated baseline levels may correlate with greater disease burden or more aggressive histology.\n"
         "- **Monitoring Treatment Response:** Serial measurements are invaluable for assessing the efficacy of systemic therapy. A consistent decline suggests response, while a rising trend may indicate resistance or disease progression (e.g., CA-125 in ovarian cancer, CEA in colorectal cancer).\n"
         "- **Detecting Recurrence:** Rising marker levels after curative-intent therapy can often precede radiographic or clinical recurrence by months.")
    ],
    "Chemotherapy Side Effects": [
        ("patient", "What should I do if I get a fever during my chemotherapy?",
         "Experiencing a fever during chemotherapy can be a sign of a serious infection, especially if your white blood cell count is low (neutropenia). Here is what you should do:\n"
         "- Check your temperature if you feel warm, chilled, or unwell.\n"
         "- A temperature of 100.4°F (38°C) or higher is generally considered a medical emergency.\n"
         "- Do not take fever-reducing medications like acetaminophen (Tylenol) or ibuprofen without speaking to your care team first, as they can mask the fever.\n"
         "- Go to the nearest emergency room or contact your oncology clinic immediately for further instructions.\n\n"
         "Because your immune system may be compromised, prompt medical evaluation and antibiotics are often critical."),
        ("patient", "How can I manage nausea after my chemo session?",
         "Nausea is a common side effect of chemotherapy, but there are several effective ways to manage it:\n"
         "- Take prescribed anti-nausea medications exactly as directed, even if you don't feel sick yet (prevention is key).\n"
         "- Eat small, frequent meals throughout the day rather than three large ones.\n"
         "- Choose bland, easily digestible foods like crackers, toast, or clear broths.\n"
         "- Avoid foods that are overly sweet, greasy, spicy, or have strong odors.\n"
         "- Stay hydrated by sipping clear liquids like water, ginger ale, or electrolyte solutions slowly.\n"
         "- Practice relaxation techniques like deep breathing or listening to calming music to help reduce anxiety-induced nausea.\n\n"
         "If your nausea persists or you are unable to keep fluids down, contact your healthcare team."),
        ("patient", "Will all chemotherapy cause me to lose my hair?",
         "Not all chemotherapy causes hair loss (alopecia). Whether or not you lose your hair depends on the specific drugs you receive and their dosages. Some key points to consider:\n"
         "- Certain drugs, like taxanes (e.g., paclitaxel) and anthracyclines (e.g., doxorubicin), are very likely to cause complete hair loss.\n"
         "- Other drugs may cause only mild thinning, or no hair loss at all.\n"
         "- Hair loss usually begins 1 to 3 weeks after your first treatment.\n"
         "- Your hair will almost always grow back after treatment is completed, though it may be a different texture or color initially.\n"
         "- Some clinics offer scalp cooling caps, which can reduce the risk of severe hair loss for certain regimens.\n\n"
         "Ask your oncologist what to expect with your specific treatment protocol."),
        ("patient", "What is 'chemo brain' and how can I manage it?",
         "'Chemo brain' is a common term used by cancer survivors to describe thinking and memory problems that can occur during and after cancer treatment. Symptoms often include mental fogginess, difficulty concentrating, and trouble remembering details. Ways to manage this include:\n"
         "- Use planners or smartphone apps to track daily tasks and appointments.\n"
         "- Break complex tasks into smaller, manageable steps.\n"
         "- Ensure you get adequate sleep and rest.\n"
         "- Stay mentally active with puzzles, reading, or learning new skills.\n"
         "- Engage in regular, light physical exercise to improve blood flow to the brain.\n"
         "- Minimize distractions when focusing on important tasks.\n\n"
         "If these cognitive changes severely impact your daily life, speak to your care team about potentially seeing a cognitive rehabilitation specialist."),
        ("professional", "What are the common hematologic toxicities of the AC (Adriamycin/Cytoxan) regimen?",
         "The AC (doxorubicin/cyclophosphamide) regimen frequently causes significant hematologic toxicities. The most common include:\n"
         "- Neutropenia: Often severe, with a typical nadir occurring between days 10 and 14 of the cycle. Prophylactic use of G-CSF (granulocyte colony-stimulating factor) is often considered depending on the patient's overall risk profile and age.\n"
         "- Anemia: Cumulative and may require red blood cell transfusions if symptomatic or if hemoglobin drops significantly.\n"
         "- Thrombocytopenia: Less commonly dose-limiting compared to neutropenia, but platelet counts should be carefully monitored prior to each cycle.\n\n"
         "Careful monitoring with complete blood counts (CBC) with differential is standard practice before administering subsequent cycles."),
        ("patient", "Why do my hands and feet tingle after receiving certain chemotherapies?",
         "Tingling, numbness, or pain in the hands and feet is a condition called peripheral neuropathy. It is caused by certain chemotherapy drugs (like taxanes, platinums, and vinca alkaloids) damaging the peripheral nerves. To manage and monitor this:\n"
         "- Report any tingling, numbness, burning, or weakness to your oncologist immediately. They may need to adjust your chemo dose to prevent permanent damage.\n"
         "- Be very careful with sharp objects (like knives) and avoid walking barefoot to prevent injuries you might not feel.\n"
         "- Wear comfortable, well-fitting shoes.\n"
         "- Use gloves when handling cold objects if you are receiving drugs like oxaliplatin, which can cause severe cold sensitivity in the nerves.\n"
         "- Your doctor may prescribe medications (such as duloxetine or gabapentin) to help manage severe nerve pain."),
        ("patient", "How can I treat mouth sores caused by my cancer treatment?",
         "Mouth sores (mucositis) are a painful side effect of some chemotherapy and radiation treatments. To help manage and heal them:\n"
         "- Maintain excellent oral hygiene. Gently brush your teeth using a soft-bristled toothbrush after every meal and at bedtime.\n"
         "- Rinse your mouth 4 to 6 times a day with a mixture of baking soda and salt in warm water (1/4 tsp each in 8 oz water). Avoid mouthwashes containing alcohol.\n"
         "- Eat soft, bland, and moist foods (like mashed potatoes, scrambled eggs, or yogurt).\n"
         "- Avoid spicy, acidic, or very hot foods and drinks, as they can burn the sores.\n"
         "- Sucking on ice chips during the administration of certain chemotherapy drugs (like 5-FU) can sometimes help prevent mouth sores.\n"
         "- Ask your doctor for prescription 'magic mouthwash' to numb the pain before you eat.")
    ],
    "Targeted Therapies and Immunotherapy": [
        ("patient", "What are the common side effects of Darzalex (daratumumab)?",
         "Darzalex (daratumumab) is a targeted therapy used primarily for multiple myeloma. Common side effects you might experience include:\n"
         "- Infusion-related reactions: These often happen during or shortly after the first infusion. Symptoms can include chills, fever, shortness of breath, and a runny or stuffy nose.\n"
         "- Fatigue or feeling unusually tired.\n"
         "- Nausea and diarrhea.\n"
         "- Upper respiratory tract infections, such as a cold or cough.\n"
         "- Low blood cell counts, which may increase your risk of bleeding or infections.\n\n"
         "Your healthcare team will give you pre-medications (like antihistamines and steroids) to help lower the risk of infusion reactions."),
        ("patient", "What is the difference between chemotherapy and immunotherapy?",
         "While both are treatments for cancer, they work in very different ways:\n"
         "- **Chemotherapy** uses powerful drugs to directly attack and kill rapidly dividing cells in the body, which includes cancer cells but also healthy fast-growing cells (like hair follicles and the digestive tract lining), leading to traditional side effects like hair loss and nausea.\n"
         "- **Immunotherapy** does not directly kill cancer cells. Instead, it boosts or trains your body's own immune system to recognize and attack the cancer cells more effectively.\n\n"
         "Because they work differently, the side effects of immunotherapy are often different from chemotherapy, typically presenting as inflammatory or autoimmune-like reactions (e.g., skin rashes, colitis, or thyroid issues)."),
        ("patient", "How is Herceptin (trastuzumab) different from standard chemotherapy for breast cancer?",
         "Herceptin (trastuzumab) is a type of targeted therapy, not traditional chemotherapy. \n"
         "- It is specifically designed to target breast cancer cells that overproduce a protein called HER2 (HER2-positive breast cancer).\n"
         "- Because it targets specific cancer cells rather than all rapidly dividing cells, it typically does not cause hair loss or severe nausea like traditional chemotherapy.\n"
         "- It is often given in combination with chemotherapy, but its primary unique risk is potential cardiac toxicity (weakening of the heart muscle). Therefore, your doctor will regularly monitor your heart function (e.g., with an echocardiogram) while you are on this medication."),
        ("professional", "What premedications are required before Darzalex infusion?",
         "To minimize the risk of severe infusion-related reactions (IRRs) associated with daratumumab, standard premedication protocols are required. These typically include:\n"
         "- An intravenous corticosteroid (e.g., methylprednisolone 100 mg for the first few infusions, tapering to a lower dose for subsequent doses).\n"
         "- An oral or intravenous antipyretic (e.g., acetaminophen 650-1000 mg).\n"
         "- An oral or intravenous antihistamine (e.g., diphenhydramine 25-50 mg).\n\n"
         "Additionally, post-infusion medications (such as oral corticosteroids) may be administered on the days following the infusion to prevent delayed reactions, particularly in patients with a history of chronic obstructive pulmonary disease (COPD)."),
        ("professional", "How should immune-related adverse events (irAEs) from checkpoint inhibitors be managed?",
         "Management of irAEs (such as pneumonitis, colitis, or hepatitis) secondary to PD-1/PD-L1 or CTLA-4 inhibitors relies on grading the severity of the toxicity according to CTCAE criteria:\n"
         "- **Grade 1:** Generally, continue immunotherapy with close monitoring; symptomatic treatment may be provided.\n"
         "- **Grade 2:** Withhold the checkpoint inhibitor. Initiate systemic corticosteroids (e.g., prednisone 0.5-1 mg/kg/day). Resume immunotherapy only when symptoms resolve to Grade 1 or less and steroids are tapered.\n"
         "- **Grade 3/4:** Permanently discontinue the checkpoint inhibitor. Initiate high-dose systemic corticosteroids (e.g., methylprednisolone 1-2 mg/kg/day IV). If symptoms are refractory to steroids after 48-72 hours, consider secondary immunosuppressive agents (e.g., infliximab for colitis, mycophenolate mofetil for hepatitis).\n\n"
         "Early recognition and prompt immunosuppression are critical for resolving severe irAEs."),
        ("patient", "Why is my doctor testing my tumor for PD-L1 expression?",
         "Testing a tumor for PD-L1 (Programmed Death-Ligand 1) expression helps your oncologist determine if you are a good candidate for certain types of immunotherapy called checkpoint inhibitors (such as Keytruda or Opdivo).\n"
         "- PD-L1 is a protein that some cancer cells use to 'hide' from your body's immune system.\n"
         "- If your tumor has high levels of PD-L1, it means the cancer is relying heavily on this 'hiding' mechanism.\n"
         "- Checkpoint inhibitor drugs work by blocking PD-L1, effectively exposing the cancer cells so your immune system can attack them.\n"
         "- Tumors with high PD-L1 expression generally respond better to these specific immunotherapies, allowing your doctor to tailor your treatment plan effectively.")
    ],
    "Radiation Therapy": [
        ("patient", "Does radiation therapy make me radioactive?",
         "For the vast majority of external beam radiation treatments, the answer is no. \n"
         "- External beam radiation is like having an X-ray; the radiation passes through your body to target the tumor, but it does not stay inside you. You are perfectly safe to be around pregnant women and children immediately after your session.\n"
         "- However, if you are receiving internal radiation (brachytherapy) or systemic radiation (like radioactive iodine for thyroid cancer), radioactive materials are placed inside your body.\n"
         "- In those specific internal cases, your body may give off a small amount of radiation for a short time, and your medical team will give you specific safety precautions (like keeping a certain distance from others) until the radiation levels drop."),
        ("patient", "What skin changes should I expect during radiation therapy?",
         "Radiation dermatitis is a common side effect where the skin in the treatment area becomes irritated. You may experience:\n"
         "- Redness, similar to a mild or severe sunburn.\n"
         "- Dryness, itching, and peeling (dry desquamation).\n"
         "- In more severe cases, the skin may blister or weep fluid (moist desquamation).\n"
         "- The treated skin may eventually become darker or tanned.\n\n"
         "To care for your skin, wash the area gently with warm water and mild, unscented soap. Pat dry, avoid tight clothing over the area, and only use lotions or creams (like Aquaphor or calendula cream) that are explicitly approved by your radiation oncologist."),
        ("professional", "What are the indications for stereotactic body radiation therapy (SBRT) in early-stage non-small cell lung cancer (NSCLC)?",
         "SBRT (also known as SABR) is primarily indicated for patients with medically inoperable, early-stage (Stage I or node-negative Stage II) non-small cell lung cancer.\n"
         "- It is highly effective for peripheral tumors typically < 5 cm in diameter.\n"
         "- It delivers highly conformal, ablative doses of radiation in a hypofractionated schedule (typically 3 to 5 fractions).\n"
         "- SBRT has shown excellent local control rates (often >90% at 3 years) that rival surgical outcomes for this specific patient population, though it carries risks of radiation pneumonitis or chest wall toxicity depending on tumor location.")
    ],
    "Nutrition and Diet during Treatment": [
        ("patient", "What should I eat when I have no appetite due to radiation?",
         "A loss of appetite is very common during radiation therapy. Maintaining your nutrition is vital for healing. Try these strategies:\n"
         "- Eat small, frequent snacks every 2-3 hours instead of trying to force large meals.\n"
         "- Focus on high-calorie and high-protein foods like nuts, cheese, Greek yogurt, and eggs.\n"
         "- Try drinking your calories if solid food is unappealing. Smoothies, milkshakes, and specialized nutritional supplement drinks can be easier to get down.\n"
         "- Keep your favorite snacks visible and easily accessible.\n"
         "- Eat in a pleasant, relaxing environment and try making meals a social activity.\n\n"
         "If you continue to lose weight, ask to speak with an oncology dietitian for personalized advice."),
        ("patient", "Are there any foods I should avoid during chemotherapy?",
         "Because chemotherapy can lower your white blood cell count and weaken your immune system, food safety is very important. You should generally avoid:\n"
         "- Raw or undercooked meat, poultry, and seafood (including sushi).\n"
         "- Unpasteurized milk, cheese, and juices.\n"
         "- Raw or undercooked eggs (such as in homemade mayonnaise or raw cookie dough).\n"
         "- Unwashed fresh fruits and vegetables. Ensure you wash all produce thoroughly before eating.\n"
         "- Deli meats or cold cuts unless they have been heated until steaming hot.\n"
         "- Salad bars or buffets where food sits out for long periods.\n\n"
         "Following strict food hygiene practices reduces your risk of foodborne illnesses while your immune system is compromised."),
        ("patient", "I have a metallic taste in my mouth from chemo. How can I make food taste better?",
         "Changes in taste, often described as a metallic or bitter flavor, are common side effects of chemotherapy (dysgeusia). To improve the taste of food:\n"
         "- Use plastic or bamboo utensils instead of metal silverware.\n"
         "- Avoid eating out of canned containers; use glass or ceramic plates.\n"
         "- Add tart flavors like lemon juice, vinegar, or citrus marinades to foods (unless you have mouth sores).\n"
         "- Try using stronger seasonings and herbs, like garlic, onion, basil, or mint, to mask bitter flavors.\n"
         "- Eat foods cold or at room temperature, as this can reduce strong odors and distinct flavors.\n"
         "- Try sucking on sugar-free lemon drops or mints before meals to clear your palate."),
        ("professional", "What are the indications for enteral nutrition in head and neck cancer patients undergoing chemoradiotherapy?",
         "Patients undergoing concurrent chemoradiotherapy for advanced head and neck squamous cell carcinoma are at high risk for severe mucositis, dysphagia, and subsequent malnutrition. Indications for prophylactic or reactive enteral nutrition (typically via PEG tube) include:\n"
         "- Prophylactic placement is recommended for patients expected to experience significant weight loss, those with pre-existing severe malnutrition (e.g., >10% weight loss in 6 months), or those presenting with significant baseline dysphagia.\n"
         "- Reactive placement is indicated if oral intake becomes inadequate to maintain hydration and nutrition despite aggressive oral supplementation and symptom management (e.g., resulting in >5% weight loss during treatment).\n\n"
         "Early involvement of a registered dietitian and speech-language pathologist is standard of care.")
    ],
    "Emotional and Mental Support": [
        ("patient", "How can I support someone who is undergoing cancer treatment?",
         "Supporting someone who is undergoing cancer treatment can be a challenging but rewarding experience. Here are some ways to provide emotional and practical support:\n"
         "- Listen without judgment\n"
         "- Offer encouragement and positive words\n"
         "- Be present and attentive\n"
         "- Help with daily tasks and errands (be specific, e.g., 'Can I bring dinner on Tuesday?' instead of 'Let me know if you need help')\n"
         "- Encourage self-care and relaxation\n"
         "- Provide emotional support and resources for coping with stress and anxiety\n"
         "- Encourage regular check-ins with healthcare professionals\n\n"
         "Remember, everyone's experience with cancer is unique, and it is essential to be patient, compassionate, and understanding."),
        ("patient", "How do I talk to my children about my cancer diagnosis?",
         "Discussing a cancer diagnosis with children is incredibly difficult, but honesty is usually the best approach. Here are some guidelines:\n"
         "- **Be age-appropriate:** Use simple, clear language for younger children, while older children and teens can handle more detailed medical information.\n"
         "- **Use the word 'cancer':** Avoid vague terms like 'sick,' which can make children fear that normal illnesses (like a cold) are dangerous.\n"
         "- **Reassure them:** Children often worry that they caused the illness or that they can 'catch' it. Clarify that cancer is not contagious and it is not their fault.\n"
         "- **Explain the treatment plan:** Let them know what to expect regarding physical changes (like hair loss or fatigue) or disruptions to their daily routine.\n"
         "- **Encourage questions:** Let them know it is okay to feel sad, angry, or scared, and that they can ask you anything.\n\n"
         "Consider utilizing resources from hospital social workers or child life specialists, who are trained to help families navigate these conversations."),
        ("patient", "I feel incredibly anxious before every scan (scanxiety). How can I cope?",
         "'Scanxiety'—the severe anxiety leading up to medical imaging and waiting for results—is a highly common and valid experience for cancer patients and survivors. Coping strategies include:\n"
         "- Communicate with your medical team. Ask exactly when and how you will receive your results so you aren't waiting by the phone unnecessarily.\n"
         "- Schedule scans early in the morning or early in the week to reduce the waiting time for results.\n"
         "- Bring a trusted friend or family member to the appointment for distraction and support.\n"
         "- Practice mindfulness, deep breathing exercises, or meditation in the waiting room.\n"
         "- Plan an enjoyable distraction or a small reward for immediately after the scan is completed.\n"
         "- Speak to a counselor or join a support group where you can share these feelings with others who understand exactly what you are going through.")
    ]
}

system_prompt_patient = "You are a helpful, highly educated, and empathetic medical AI assistant. Provide detailed, structured, and informative answers using formatting like bullet points when appropriate. Always append this disclaimer at the very end of your answer: 'I am an AI, not a doctor. Please consult your oncologist or healthcare provider for personalized medical advice.'"
system_prompt_professional = "You are a specialized medical AI assistant designed for oncology professionals. Provide precise, comprehensive, and evidence-based answers using medical terminology based on the retrieved context."

def generate_dataset(filename="oncology_qa_dataset.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Segment", "Target Audience", "System Prompt", "User Question", "Simulated RAG Context", "Ideal Assistant Response"])

        questions_generated = 0

        # Iterate over the unique dictionary exactly once
        for segment_name, qa_list in segments.items():
            for audience, question, base_answer in qa_list:

                sys_prompt = system_prompt_patient if audience == "patient" else system_prompt_professional

                # Add safety guardrails to the base answer for patients
                if audience == "patient":
                    final_answer = f"{base_answer}\n\n*Disclaimer: I am an AI, not a doctor. Please consult your oncologist or healthcare provider for personalized medical advice.*"
                else:
                    final_answer = base_answer

                # For RAG context, we simulate a retrieved document that contains the exact high-quality answer
                simulated_context = f"Retrieved Medical Guidelines for {segment_name}: {base_answer}"

                writer.writerow([segment_name, audience, sys_prompt, question, simulated_context, final_answer])
                questions_generated += 1

    print(f"Generated {questions_generated} completely unique, high-quality Q&A pairs in {filename}")

if __name__ == "__main__":
    generate_dataset()
