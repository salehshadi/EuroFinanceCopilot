import random
import time

from locust import HttpUser, between, task


class ChatUser(HttpUser):
    wait_time = between(5, 20)

    @task
    def ask_question(self):
        self.client.get("/")
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "history": [
                    {
                        "user": random.choice(
                            [
                                "How to avoid double taxation?",
                                "How do I start long term investment?",
                                "How to register a business for VAT?",
                            ]
                        )
                    }
                ],
                "approach": "rrr",
                "overrides": {
                    "retrieval_mode": "hybrid",
                    "semantic_ranker": True,
                    "semantic_captions": False,
                    "top": 3,
                    "suggest_followup_questions": False,
                },
            },
        )
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "history": [
                    {
                        "user": "How to avoid double taxation?",
                        "bot": "Utilizing tax treaties or conventions: Many countries have signed bilateral tax treaties or conventions with each other to prevent double taxation. These agreements typically provide mechanisms such as tax credits or exemptions to eliminate or reduce the impact of double taxation. [employee_handbook-3.pdf].",
                    },
                    {"user": "Can I claim tax credits?"},
                ],
                "approach": "rrr",
                "overrides": {
                    "retrieval_mode": "hybrid",
                    "semantic_ranker": True,
                    "semantic_captions": False,
                    "top": 3,
                    "suggest_followup_questions": False,
                },
            },
        )
