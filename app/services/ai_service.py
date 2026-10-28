from langchain_groq import ChatGroq

from app.config import (
    GROQ_API_KEY,
    GROQ_MODEL,
)

from app.prompts.travel_prompt import build_travel_prompt


class AIService:

    def __init__(self):

        if not GROQ_API_KEY:
            raise ValueError(
                "GROQ_API_KEY is missing. Please check your .env file."
            )

        self.llm = ChatGroq(
        model=GROQ_MODEL,
        api_key=GROQ_API_KEY,
        temperature=0.7,
        timeout=60,
        max_retries=3,
    )

    def generate_itinerary(
        self,
        destination: str,
        days: int,
        budget: float,
        travelers: int,
        interests: str,
    ):

        prompt = build_travel_prompt(
            destination=destination,
            days=days,
            budget=budget,
            travelers=travelers,
            interests=interests,
        )

        response = self.llm.invoke(prompt)

        return response.content