def ask_financial_ai(question, financial_data):
    question = str(question).lower().strip()

    if not financial_data:
        return "No financial data is available yet. Add some expenses first."

    if isinstance(financial_data, str):
        data_text = financial_data
    else:
        data_text = str(financial_data)

    if any(word in question for word in ["total", "spent", "spending", "expenses"]):
        return (
            "Here is your available financial data:\n"
            + data_text
            + "\nReview this data to identify your spending."
        )

    if any(word in question for word in ["save", "saving", "reduce", "budget"]):
        return (
            "To manage your budget, review your largest expense "
            "categories, set spending limits, and reduce non-essential "
            "purchases. Use your recorded financial data to choose a realistic limit."
        )

    if any(word in question for word in ["category", "categories"]):
        return (
            "Here is your available financial data:\n"
            + data_text
        )

    if any(word in question for word in ["help", "advice", "suggestion", "suggest"]):
        return (
            "Review your recorded expenses, identify recurring costs, "
            "compare spending against your budget, and set a savings target."
        )

    return (
        "I can help with basic spending, budget, savings, and category questions. "
        "Try asking about your total spending or how to reduce expenses.\n\n"
        "Available financial data:\n"
        + data_text
    )