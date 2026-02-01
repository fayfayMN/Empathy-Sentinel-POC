
def analyze_biff(text):
    blob = TextBlob(text)
    word_count = len(text.split())
    is_brief = word_count < 100
    is_friendly = blob.sentiment.polarity > 0
    is_objective = blob.sentiment.subjectivity < 0.5

    return {
        "Word Count": word_count,
        "Brief": "Pass" if is_brief else "Fail",
        "Objective": "Pass" if is_objective else "Fail"
    }

if __name__ == "__main__":
    sample = "You are always late! You never care about anyone but yourself!"
    analysis = analyze_biff(sample)
    print("--- Empathy Sentinel: BIFF Analysis ---")
    for key, value in analysis.items():
        print(f"{key}: {value}")
