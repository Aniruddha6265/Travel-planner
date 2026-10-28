"""
llm_client.py — Unified LLM client supporting Gemini, Groq, and Demo modes.
All methods return parsed Python dicts from structured JSON prompts.
"""

import json
import time
import re
import streamlit as st
from demo_data import (
    get_demo_recommendations,
    get_demo_itinerary,
    get_demo_swap,
    get_demo_day_regeneration,
)


class LLMClient:
    """Unified LLM interface for Gemini, Groq, and Demo mode."""

    def __init__(self, provider: str = "Gemini", api_key: str = "", demo_mode: bool = True):
        self.provider = provider
        self.api_key = api_key
        self.demo_mode = demo_mode
        self._client = None

        if not demo_mode and api_key:
            self._init_client()

    def _init_client(self):
        """Initialize the appropriate LLM client."""
        try:
            if self.provider == "Gemini":
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                self._client = genai.GenerativeModel("gemini-1.5-flash")
            elif self.provider == "Groq":
                from groq import Groq
                self._client = Groq(api_key=self.api_key)
        except Exception as e:
            st.error(f"Failed to initialize {self.provider} client: {e}")
            self.demo_mode = True

    def _generate_raw(self, prompt: str, system_prompt: str = "") -> str:
        """Generate raw text from the LLM with retry logic."""
        max_retries = 2
        for attempt in range(max_retries + 1):
            try:
                if self.provider == "Gemini":
                    full_prompt = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt
                    response = self._client.generate_content(full_prompt)
                    return response.text
                elif self.provider == "Groq":
                    messages = []
                    if system_prompt:
                        messages.append({"role": "system", "content": system_prompt})
                    messages.append({"role": "user", "content": prompt})
                    response = self._client.chat.completions.create(
                        model="llama-3.1-70b-versatile",
                        messages=messages,
                        temperature=0.7,
                        max_tokens=4096,
                    )
                    return response.choices[0].message.content
            except Exception as e:
                if attempt < max_retries:
                    time.sleep(2 ** attempt)
                    continue
                raise e
        return ""

    def _parse_json_response(self, text: str) -> dict:
        """Extract and parse JSON from LLM response text."""
        # Try direct parse first
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass

        # Extract JSON from markdown code blocks
        json_match = re.search(r"```(?:json)?\s*\n(.*?)\n```", text, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group(1))
            except json.JSONDecodeError:
                pass

        # Try to find JSON object or array in the text
        for pattern in [r"\{[\s\S]*\}", r"\[[\s\S]*\]"]:
            match = re.search(pattern, text)
            if match:
                try:
                    return json.loads(match.group())
                except json.JSONDecodeError:
                    continue

        raise ValueError(f"Could not parse JSON from LLM response:\n{text[:500]}")

    def _generate_json(self, prompt: str, system_prompt: str = "") -> dict:
        """Generate and parse a JSON response from the LLM."""
        json_system = (
            (system_prompt + "\n\n" if system_prompt else "")
            + "IMPORTANT: Respond ONLY with valid JSON. No markdown, no explanations, no extra text. Just the JSON object."
        )
        raw = self._generate_raw(prompt, json_system)
        return self._parse_json_response(raw)

    # ── Public API ──────────────────────────────────────────────

    def get_recommendations(self, preferences: dict) -> dict:
        """Get destination recommendations based on user preferences."""
        if self.demo_mode:
            return get_demo_recommendations(preferences)

        prompt = f"""Based on the following traveler preferences, recommend the top 3 matching cities.

Preferences:
- Travel Vibe: {preferences.get('vibe', 'Cultural')}
- Budget Level: {preferences.get('budget_level', 'Moderate')}
- Travel Party: {preferences.get('travel_party', 'Solo')}
- Travel Dates: {preferences.get('start_date', 'Flexible')}
- Interests: {', '.join(preferences.get('interests', ['Food', 'History']))}
- Pace: {preferences.get('pace', 'Moderate')}

Return a JSON object with this exact structure:
{{
    "recommendations": [
        {{
            "city": "City Name",
            "country": "Country Name",
            "match_score": 92,
            "highlight_tags": ["Tag1", "Tag2", "Tag3", "Tag4"],
            "avg_daily_cost_usd": 85,
            "best_season": "Apr–Oct",
            "description": "2-3 sentence compelling description of why this city matches their preferences."
        }}
    ]
}}

Consider weather for their travel dates, budget appropriateness, and match to their stated interests and vibe. Each city should have 3-4 highlight tags and a match_score between 70-99."""

        try:
            return self._generate_json(prompt)
        except Exception as e:
            st.error(f"Error getting recommendations: {e}")
            return get_demo_recommendations(preferences)

    def generate_itinerary(self, preferences: dict) -> dict:
        """Generate a day-by-day optimized itinerary."""
        if self.demo_mode:
            return get_demo_itinerary(preferences)

        destination = preferences.get("destination", "Lisbon")
        duration = preferences.get("duration", 3)
        budget_level = preferences.get("budget_level", "Moderate")
        party = preferences.get("travel_party", "Solo")
        pace = preferences.get("pace", "Moderate")
        interests = ", ".join(preferences.get("interests", ["Food", "History"]))

        prompt = f"""Create a detailed {duration}-day travel itinerary for {destination}.

Traveler Profile:
- Budget Level: {budget_level}
- Travel Party: {party}
- Pace: {pace}
- Interests: {interests}

CRITICAL RULES:
1. GEOGRAPHIC CLUSTERING: Group attractions by geographic proximity so each day covers a walkable neighborhood or cluster. Minimize transit between activities. Never send the traveler to opposite ends of the city on the same day.
2. Each day MUST have 4-5 time slots covering: Morning Sightseeing, Lunch, Afternoon Leisure, Evening Dining & Entertainment.
3. Include realistic cost estimates in local currency for each activity.
4. Vary activities across days — don't repeat restaurant types or attraction categories.

Return a JSON object with this exact structure:
{{
    "destination": "{destination}",
    "currency": "LOCAL_CURRENCY_CODE",
    "currency_symbol": "SYMBOL",
    "exchange_rate_to_usd": 1.0,
    "exchange_rate_to_inr": 83.5,
    "days": [
        {{
            "day": 1,
            "theme": "Day Theme Title",
            "neighborhood_cluster": "Neighborhood / Area Name",
            "slots": [
                {{
                    "time": "9:00 AM",
                    "period": "Morning Sightseeing",
                    "activity": "Activity Name",
                    "description": "2-3 sentence description with insider tips.",
                    "cost_local": 10,
                    "cost_usd": 10.80,
                    "category": "attraction|dining|exploration|entertainment|shopping|transport"
                }}
            ],
            "day_total_local": 65,
            "day_total_usd": 70.20
        }}
    ],
    "trip_total_local": 350,
    "trip_total_usd": 378.00,
    "trip_total_inr": 31563.00
}}

Make the itinerary feel authentic and locally immersive, not touristy and generic."""

        try:
            return self._generate_json(prompt)
        except Exception as e:
            st.error(f"Error generating itinerary: {e}")
            return get_demo_itinerary(preferences)

    def swap_activity(self, itinerary: dict, day: int, slot_index: int, instruction: str) -> dict:
        """Swap a single activity slot based on user instruction."""
        if self.demo_mode:
            return get_demo_swap(day, slot_index, instruction)

        day_data = itinerary["days"][day - 1]
        current_slot = day_data["slots"][slot_index]
        surrounding = [s["activity"] for s in day_data["slots"]]

        prompt = f"""I need to swap ONE activity in my {itinerary['destination']} itinerary.

Current Day {day} — {day_data['theme']} (Neighborhood: {day_data['neighborhood_cluster']})
Current Slot: {current_slot['time']} — {current_slot['activity']}
Other activities this day: {', '.join(surrounding)}

User's swap request: "{instruction}"

Return a JSON object for the replacement slot with this exact structure:
{{
    "time": "{current_slot['time']}",
    "period": "{current_slot['period']}",
    "activity": "New Activity Name",
    "description": "2-3 sentence description.",
    "cost_local": 10,
    "cost_usd": 10.80,
    "category": "attraction|dining|exploration|entertainment|shopping|transport"
}}

IMPORTANT: The replacement must be geographically close to {day_data['neighborhood_cluster']} to maintain clustering."""

        try:
            return self._generate_json(prompt)
        except Exception as e:
            st.error(f"Error swapping activity: {e}")
            return get_demo_swap(day, slot_index, instruction)

    def regenerate_day(self, itinerary: dict, day: int, preferences: dict) -> dict:
        """Regenerate an entire day of the itinerary."""
        if self.demo_mode:
            return get_demo_day_regeneration(day, preferences)

        other_days_themes = [
            d["theme"] for d in itinerary["days"] if d["day"] != day
        ]
        interests = ", ".join(preferences.get("interests", ["Food", "History"]))

        prompt = f"""Regenerate Day {day} of my {itinerary['destination']} itinerary with completely NEW activities.

Traveler Interests: {interests}
Budget Level: {preferences.get('budget_level', 'Moderate')}
Pace: {preferences.get('pace', 'Moderate')}
Currency: {itinerary.get('currency', 'USD')}

AVOID duplicating themes from other days: {', '.join(other_days_themes)}

Return a JSON object with this exact structure:
{{
    "day": {day},
    "theme": "New Day Theme",
    "neighborhood_cluster": "Neighborhood Name",
    "slots": [
        {{
            "time": "9:00 AM",
            "period": "Morning Sightseeing",
            "activity": "Activity Name",
            "description": "Description",
            "cost_local": 10,
            "cost_usd": 10.80,
            "category": "attraction|dining|exploration|entertainment|shopping|transport"
        }}
    ],
    "day_total_local": 55,
    "day_total_usd": 59.40
}}

Include 4-5 time slots and geographically cluster activities in one area."""

        try:
            return self._generate_json(prompt)
        except Exception as e:
            st.error(f"Error regenerating day: {e}")
            return get_demo_day_regeneration(day, preferences)
