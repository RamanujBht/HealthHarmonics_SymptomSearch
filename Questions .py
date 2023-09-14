# Sample Symptom Checker for a Common Cold

# Initialize a dictionary with symptoms and their associated questions
symptom_questions = {
    'Shortness_of_breath': 'Do you have a cough? (yes/no): ',
    'Chest_pain': 'Do you have a runny nose? (yes/no): ',
    'Irregular_pulse': 'Do you have a runny nose? (yes/no): ',
    'Chest_pain': 'Do you have a runny nose? (yes/no): ',
    'Chest_pain': 'Do you have a runny nose? (yes/no): ',
    'Chest_pain': 'Do you have a runny nose? (yes/no): ',
}

# Initialize a dictionary with disease information
disease_info = {
    'common_cold': {
        'symptoms': ['cough', 'runny_nose'],
        'remedies': ['Rest', 'Drink fluids', 'Herbal teas'],
    },
}

# Initialize user symptoms
user_symptoms = []

# Ask the user about symptoms
for symptom, question in symptom_questions.items():
    response = input(question).strip().lower()
    if response == 'yes':
        user_symptoms.append(symptom)

# Check for common cold
for disease, info in disease_info.items():
    if all(symptom in user_symptoms for symptom in info['symptoms']):
        print(f"You might have a {disease}.")
        print("Recommendation:")
        for remedy in info['remedies']:
            print(f"- {remedy}")

# If no match found
else:
    print("We couldn't identify your condition. Please consult a healthcare professional.")
