def build_travel_prompt(
    destination: str,
    days: int,
    budget: float,
    travelers: int,
    interests: str,
) -> str:

    return f"""
You are an expert AI Travel Planner.

Generate a professional travel itinerary.

Destination:
{destination}

Number of Days:
{days}

Budget:
₹{budget}

Travelers:
{travelers}

Interests:
{interests}

Requirements:

1. Create a day-by-day itinerary.

2. Include:
- Morning
- Afternoon
- Evening

3. Recommend:
- Tourist attractions
- Food
- Transportation
- Estimated daily budget

4. Keep the total cost within the user's budget.

5. Return the answer in clean Markdown format.

Be practical, realistic, and well organized.
"""