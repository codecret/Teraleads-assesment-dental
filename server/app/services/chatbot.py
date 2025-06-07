from typing import Dict, List
import re
import random

class ChatbotService:
    def __init__(self):
        self.templates = {
            "greeting": [
                "Hello! How can I help you today?",
                "Hi there! What can I assist you with?",
                "Welcome! How may I help you with your dental care needs?"
            ],
            "appointment": [
                "To schedule an appointment, please contact our front desk at (555) 123-4567 or use our online booking system.",
                "You can book an appointment through our website or by calling our office directly.",
                "For appointment scheduling, you can reach us during business hours at (555) 123-4567."
            ],
            "procedure": [
                "I can provide information about various dental procedures. Which specific procedure would you like to know about?",
                "We offer a wide range of dental procedures. Could you please specify which one you're interested in?",
                "I'd be happy to explain any dental procedure. What would you like to learn about?"
            ],
            "emergency": [
                "For dental emergencies, please call our emergency line at (555) 999-8888 immediately.",
                "If you're experiencing a dental emergency, contact our emergency line right away at (555) 999-8888.",
                "In case of a dental emergency, please call (555) 999-8888 for immediate assistance."
            ],
            "cost": [
                "Dental costs vary depending on the procedure and your insurance coverage. Would you like to schedule a consultation to discuss specific costs?",
                "We can provide a detailed cost estimate during your consultation. Would you like to schedule one?",
                "Costs depend on your specific needs and insurance. Let's schedule a consultation to discuss the details."
            ],
            "default": [
                "I understand you're asking about {topic}. Let me help you with that. Could you please provide more specific details?",
                "Regarding {topic}, I'd be happy to assist. What specific information are you looking for?",
                "I can help you with {topic}. Could you please elaborate on your question?"
            ]
        }
        
        self.keywords = {
            "greeting": ["hello", "hi", "hey", "greetings"],
            "appointment": ["appointment", "schedule", "booking", "book", "when", "available"],
            "procedure": ["procedure", "treatment", "extraction", "filling", "root canal", "cleaning"],
            "emergency": ["emergency", "urgent", "pain", "hurt", "swelling", "bleeding"],
            "cost": ["cost", "price", "expensive", "insurance", "payment", "bill"]
        }

    def _identify_topic(self, message: str) -> str:
        message = message.lower()
        for topic, words in self.keywords.items():
            if any(word in message for word in words):
                return topic
        return "default"

    def _extract_topic_from_message(self, message: str) -> str:
        # Extract potential topic words from the message
        words = message.lower().split()
        # Remove common words
        common_words = {"what", "how", "when", "where", "why", "is", "are", "the", "a", "an", "in", "on", "at", "to", "for", "with", "by"}
        topic_words = [word for word in words if word not in common_words]
        return " ".join(topic_words[:3])  # Return up to 3 words as the topic

    def get_response(self, message: str) -> str:
        """
        Get a response from the chatbot for the given message.
        """
        # Identify the topic of the message
        topic = self._identify_topic(message)
        
        # Get a random response template for the identified topic
        if topic == "default":
            # For default responses, include the extracted topic words
            topic_words = self._extract_topic_from_message(message)
            template = random.choice(self.templates[topic])
            return template.format(topic=topic_words)
        else:
            return random.choice(self.templates[topic])

# Create a singleton instance
chatbot_service = ChatbotService() 