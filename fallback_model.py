# fallback_model.py
# Author: David Leatherman


class FallbackModel:
    """Asks the first model. If it returns None, asks the second."""

    def __init__(self, primary_model, secondary_model):
        """Store the two models."""
        self.primary = primary_model
        self.secondary = secondary_model

    def decide(self, instructions, history, tools):
        """Try the primary model first. Fall back if it fails."""
        decision = self.primary.decide(instructions, history, tools)
        if decision is None:
            return self.secondary.decide(instructions, history, tools)
        return decision
