"""Personality Evaluation Module.

Evaluates babysitter responses to stressful childcare scenarios to assess
patience level and educational approach.
"""

from dataclasses import dataclass


@dataclass
class EvaluationResult:
    """Evaluation result of a babysitter's response to a crisis scenario.

    Attributes:
        patience_level: Evaluated patience level (e.g., 'High', 'Medium', 'Low').
        approach: Primary educational approach (e.g., 'Comforting',
            'Strict / Independent', 'Distraction').
    """

    patience_level: str
    approach: str


class PersonalityEvaluator:
    """Evaluates candidate responses to childcare crisis scenarios."""

    def evaluate_response(self, response: str) -> EvaluationResult:
        """Evaluate a babysitter's text response to a crisis scenario.

        Args:
            response: The babysitter's text response to the crisis scenario.

        Returns:
            EvaluationResult containing the patience level and approach.
        """
        pass


def evaluate_response(response: str) -> EvaluationResult:
    """Evaluate a babysitter's text response to a crisis scenario.

    Args:
        response: The babysitter's text response to the crisis scenario.

    Returns:
        EvaluationResult containing the patience level and approach.
    """
    pass
