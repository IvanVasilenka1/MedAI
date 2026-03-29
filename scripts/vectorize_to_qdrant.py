
from myapp.utils.config import Config
from myapp.repositories.qdrant import QdrantRepository

cases = [
    {
        "text": "Migraine is a neurological condition with severe headache, nausea, and light sensitivity.",
        "payload": {
            "condition": "Migraine",
            "doctor": "neurologist",
            "symptoms": ["headache", "nausea", "light sensitivity"],
            "actions": ["rest in a dark room", "stay hydrated", "avoid bright light"]
        }
    },
    {
        "text": "Common cold is a viral infection causing runny nose, sore throat, and mild fever.",
        "payload": {
            "condition": "Common Cold",
            "doctor": "general practitioner",
            "symptoms": ["runny nose", "sore throat", "mild fever"],
            "actions": ["rest", "drink fluids", "take OTC cold medicine"]
        }
    },
    {
        "text": "Type 2 diabetes affects blood sugar levels, causing fatigue, increased thirst, and frequent urination.",
        "payload": {
            "condition": "Type 2 Diabetes",
            "doctor": "endocrinologist",
            "symptoms": ["high blood sugar", "fatigue", "frequent urination"],
            "actions": ["monitor blood sugar", "diet control", "regular exercise"]
        }
    },
    {
        "text": "Hypertension often has no symptoms but may include headaches, shortness of breath, and nosebleeds.",
        "payload": {
            "condition": "Hypertension",
            "doctor": "cardiologist",
            "symptoms": ["headache", "shortness of breath", "nosebleeds"],
            "actions": ["monitor blood pressure", "reduce salt intake", "exercise"]
        }
    },
    {
        "text": "Asthma is a chronic respiratory condition causing wheezing, shortness of breath, and chest tightness.",
        "payload": {
            "condition": "Asthma",
            "doctor": "pulmonologist",
            "symptoms": ["wheezing", "shortness of breath", "chest tightness"],
            "actions": ["use inhaler", "avoid triggers", "monitor breathing"]
        }
    },
    {
        "text": "Allergic rhinitis causes sneezing, itchy eyes, and runny nose due to allergens.",
        "payload": {
            "condition": "Allergic Rhinitis",
            "doctor": "allergist",
            "symptoms": ["sneezing", "itchy eyes", "runny nose"],
            "actions": ["avoid allergens", "use antihistamines", "nasal sprays"]
        }
    },
    {
        "text": "Bronchitis involves inflammation of the bronchial tubes, causing cough, mucus, and fatigue.",
        "payload": {
            "condition": "Bronchitis",
            "doctor": "pulmonologist",
            "symptoms": ["cough", "mucus", "fatigue"],
            "actions": ["rest", "stay hydrated", "use humidifier"]
        }
    },
    {
        "text": "Gastroenteritis leads to diarrhea, vomiting, and abdominal pain, usually from infection.",
        "payload": {
            "condition": "Gastroenteritis",
            "doctor": "gastroenterologist",
            "symptoms": ["diarrhea", "vomiting", "abdominal pain"],
            "actions": ["stay hydrated", "oral rehydration salts", "light diet"]
        }
    },
    {
        "text": "Anemia causes fatigue, weakness, and pale skin due to low red blood cells.",
        "payload": {
            "condition": "Anemia",
            "doctor": "hematologist",
            "symptoms": ["fatigue", "weakness", "pale skin"],
            "actions": ["iron supplements", "balanced diet", "blood tests"]
        }
    },
    {
        "text": "Depression leads to persistent sadness, loss of interest, and fatigue.",
        "payload": {
            "condition": "Depression",
            "doctor": "psychiatrist",
            "symptoms": ["sadness", "loss of interest", "fatigue"],
            "actions": ["therapy", "medication", "exercise"]
        }
    },
    {
        "text": "Anxiety disorder causes excessive worry, restlessness, and muscle tension.",
        "payload": {
            "condition": "Anxiety Disorder",
            "doctor": "psychiatrist",
            "symptoms": ["excessive worry", "restlessness", "muscle tension"],
            "actions": ["therapy", "meditation", "medication"]
        }
    },
    {
        "text": "Chickenpox is a viral infection causing itchy rash, fever, and fatigue.",
        "payload": {
            "condition": "Chickenpox",
            "doctor": "pediatrician",
            "symptoms": ["itchy rash", "fever", "fatigue"],
            "actions": ["antihistamines", "rest", "hydration"]
        }
    },
    {
        "text": "Influenza presents with fever, cough, sore throat, and body aches.",
        "payload": {
            "condition": "Influenza",
            "doctor": "general practitioner",
            "symptoms": ["fever", "cough", "sore throat", "body aches"],
            "actions": ["rest", "fluids", "antiviral medication if needed"]
        }
    },
    {
        "text": "Otitis media is an infection of the middle ear causing ear pain, fever, and irritability.",
        "payload": {
            "condition": "Otitis Media",
            "doctor": "ENT specialist",
            "symptoms": ["ear pain", "fever", "irritability"],
            "actions": ["pain relief", "antibiotics if bacterial", "monitor"]
        }
    },
    {
        "text": "Pneumonia causes cough, fever, and difficulty breathing due to lung infection.",
        "payload": {
            "condition": "Pneumonia",
            "doctor": "pulmonologist",
            "symptoms": ["cough", "fever", "difficulty breathing"],
            "actions": ["antibiotics if bacterial", "rest", "hydration"]
        }
    },
    {
        "text": "Urinary tract infection (UTI) causes burning urination, frequent urination, and lower abdominal pain.",
        "payload": {
            "condition": "UTI",
            "doctor": "urologist",
            "symptoms": ["burning urination", "frequent urination", "lower abdominal pain"],
            "actions": ["antibiotics", "hydration", "urine tests"]
        }
    },
    {
        "text": "Appendicitis causes severe abdominal pain, nausea, and loss of appetite, usually requiring surgery.",
        "payload": {
            "condition": "Appendicitis",
            "doctor": "surgeon",
            "symptoms": ["abdominal pain", "nausea", "loss of appetite"],
            "actions": ["emergency surgery", "pain management"]
        }
    },
    {
        "text": "Hypothyroidism results in fatigue, weight gain, and cold intolerance due to low thyroid hormone.",
        "payload": {
            "condition": "Hypothyroidism",
            "doctor": "endocrinologist",
            "symptoms": ["fatigue", "weight gain", "cold intolerance"],
            "actions": ["thyroid hormone replacement", "monitor TSH"]
        }
    },
    {
        "text": "Hyperthyroidism causes weight loss, heat intolerance, and anxiety due to excess thyroid hormone.",
        "payload": {
            "condition": "Hyperthyroidism",
            "doctor": "endocrinologist",
            "symptoms": ["weight loss", "heat intolerance", "anxiety"],
            "actions": ["medication", "radioactive iodine", "monitor thyroid levels"]
        }
    },
    {
        "text": "COVID-19 infection can cause fever, cough, loss of taste or smell, and fatigue.",
        "payload": {
            "condition": "COVID-19",
            "doctor": "infectious disease specialist",
            "symptoms": ["fever", "cough", "loss of taste or smell", "fatigue"],
            "actions": ["isolation", "hydration", "medical monitoring"]
        }
    },
    {
        "text": "Strep throat causes sore throat, fever, and swollen lymph nodes.",
        "payload": {
            "condition": "Streptococcal Pharyngitis",
            "doctor": "general practitioner",
            "symptoms": ["sore throat", "fever", "swollen lymph nodes"],
            "actions": ["antibiotics", "rest", "hydration"]
        }
    },
    {
        "text": "Chickenpox vaccination prevents itchy rash and fever caused by varicella virus.",
        "payload": {
            "condition": "Chickenpox Vaccine",
            "doctor": "pediatrician",
            "symptoms": [],
            "actions": ["vaccination"]
        }
    },
]

def main():
    collection_name = "medical_cases"

    with QdrantRepository() as qdr:
        qdr.ensure_collection(collection_name, vector_size=1024)

        texts = [c["text"] for c in cases]
        metadatas = [c["payload"] for c in cases]

        qdr.upsert_points(texts=texts, metadatas=metadatas)

    print(f"✅ {len(cases)} medical cases loaded into Qdrant")

if __name__ == "__main__":
    main()