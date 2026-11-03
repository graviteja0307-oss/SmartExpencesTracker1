
def local_category(description):
    description = str(description).lower().strip()

    categories = {
        "Food": [
            "food", "lunch", "dinner", "breakfast", "restaurant",
            "pizza", "burger", "kfc", "swiggy", "zomato", "coffee", "tea"
        ],
        "Travel": [
            "uber", "ola", "taxi", "bus", "train", "flight",
            "metro", "travel", "fuel", "petrol", "diesel"
        ],
        "Shopping": [
            "amazon", "flipkart", "shopping", "clothes", "shirt",
            "shoes", "mall", "purchase"
        ],
        "Bills": [
            "electricity", "water bill", "internet", "wifi",
            "recharge", "bill", "rent"
        ],
        "Education": [
            "book", "course", "college", "school", "education",
            "udemy", "coursera", "exam"
        ]
    }

    for category, keywords in categories.items():
        if any(word in description for word in keywords):
            return {
                "category": category,
                "confidence": 0.70,
                "reason": f"Matched a keyword associated with {category}."
            }

    return {
        "category": "Other",
        "confidence": 0.40,
        "reason": "No clear category was detected."
    }


def suggest_category(description, expense_history=None):
    return local_category(description)
