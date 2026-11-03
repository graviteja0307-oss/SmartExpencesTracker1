
def analyze_spending(
    total,
    monthly_total,
    previous_month_total,
    category_totals,
    budget_amount
):
    try:
        total = float(total or 0)
        monthly_total = float(monthly_total or 0)
        previous_month_total = float(previous_month_total or 0)
        budget_amount = float(budget_amount or 0)

        categories = []

        for item in (category_totals or []):
            categories.append({
                "category": str(item.get("category", "Other")),
                "total": float(item.get("total", 0) or 0)
            })

        if categories:
            highest = max(categories, key=lambda item: item["total"])
            highest_category = highest["category"]
            highest_amount = highest["total"]
        else:
            highest_category = "None"
            highest_amount = 0

        if monthly_total > previous_month_total:
            difference = monthly_total - previous_month_total
            percentage = (
                difference / previous_month_total * 100
                if previous_month_total > 0 else None
            )

            if percentage is not None:
                trend = f"Spending increased by {percentage:.1f}% compared with last month."
            else:
                trend = f"Spending increased by ₹{difference:.2f} compared with last month."

        elif monthly_total < previous_month_total:
            difference = previous_month_total - monthly_total
            percentage = (
                difference / previous_month_total * 100
                if previous_month_total > 0 else 0
            )
            trend = f"Spending decreased by {percentage:.1f}% compared with last month."

        else:
            trend = "Spending is unchanged compared with last month."

        if budget_amount <= 0:
            budget_status = "No monthly budget has been set."
        else:
            remaining = budget_amount - monthly_total

            if remaining > 0:
                budget_status = (
                    f"Within budget. ₹{remaining:.2f} remaining "
                    f"out of ₹{budget_amount:.2f}."
                )
            elif remaining == 0:
                budget_status = "The monthly budget has been fully used."
            else:
                budget_status = (
                    f"Over budget by ₹{abs(remaining):.2f}."
                )

        if budget_amount > 0 and monthly_total > budget_amount:
            recommendation = (
                "Reduce non-essential spending to bring expenses "
                "within your monthly budget."
            )
        elif highest_amount > 0:
            recommendation = (
                f"Review your {highest_category} spending, currently "
                f"₹{highest_amount:.2f}, to identify possible savings."
            )
        else:
            recommendation = (
                "Record your expenses regularly to identify spending patterns."
            )

        summary = (
            f"Total spending: ₹{total:.2f}. "
            f"This month's spending: ₹{monthly_total:.2f}. "
            f"Highest spending category: {highest_category}."
        )

        return {
            "category": highest_category,
            "trend": trend,
            "budget_status": budget_status,
            "recommendation": recommendation,
            "summary": summary
        }

    except (TypeError, ValueError, AttributeError) as error:
        print("Spending Analysis Error:", error)

        return {
            "category": "Unknown",
            "trend": "Unable to determine",
            "budget_status": "Unable to determine",
            "recommendation": "Check your financial data and try again.",
            "summary": "Spending analysis could not be completed."
        }
