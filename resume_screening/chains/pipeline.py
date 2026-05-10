from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline

# Load model
pipe = pipeline(
    "text-generation",
    model="distilgpt2"
)

llm = HuggingFacePipeline(pipeline=pipe)


def calculate_score(resume, job_description):

    skills = [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "NLP",
        "TensorFlow",
        "PyTorch"
    ]

    matched = []

    for skill in skills:
        if skill.lower() in resume.lower():
            matched.append(skill)

    score = int((len(matched) / len(skills)) * 100)

    return score, matched


def generate_explanation(score, matched):

    if score >= 80:
        return f"Strong candidate with matching skills: {', '.join(matched)}."

    elif score >= 40:
        return f"Average candidate. Some required skills matched: {', '.join(matched)}."

    else:
        return "Weak candidate. Missing most required skills."


def run_pipeline(resume, job_description):

    score, matched = calculate_score(resume, job_description)

    explanation = generate_explanation(score, matched)

    return {
        "score": score,
        "explanation": explanation
    }