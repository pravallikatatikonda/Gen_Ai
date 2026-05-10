from chains.pipeline import run_pipeline

job_description = """
Looking for a Data Scientist with skills in Python, Machine Learning,
Deep Learning, NLP, and experience with TensorFlow/PyTorch.
"""

resume1 = """
Python, Machine Learning, Deep Learning, NLP, TensorFlow, PyTorch
3 years experience in Data Science
"""

resume2 = """
Python, Data Analysis, Pandas
1 year experience
"""

resume3 = """
Excel, basic programming
No ML experience
"""

resumes = [resume1, resume2, resume3]

for i, resume in enumerate(resumes, 1):
    print(f"\nCandidate {i}")
    result = run_pipeline(resume, job_description)

    print("Score:", result["score"])
    print("Explanation:", result["explanation"])