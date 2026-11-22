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


# Hardcoded stub mapping based on design/scenarios.md
_STUB_RESPONSES = {
    "i would take a deep breath, pick the baby up, and sing a quiet song until he calms down.": EvaluationResult(
        patience_level="High", approach="Comforting"
    ),
    "i'd put him in his crib and leave the room for 5 minutes so he learns to self-soothe.": EvaluationResult(
        patience_level="Low", approach="Strict / Independent"
    ),
    "i will try to distract him with a noisy toy or give him a screen to watch.": EvaluationResult(
        patience_level="Medium", approach="Distraction"
    ),
}


class PersonalityEvaluator:
    """Evaluates candidate responses to childcare crisis scenarios."""

    def evaluate_response(self, response: str) -> EvaluationResult:
        """Evaluate a babysitter's text response to a crisis scenario.

        Args:
            response: The babysitter's text response to the crisis scenario.

        Returns:
            EvaluationResult containing the patience level and approach.
        """
        return evaluate_response(response)


def evaluate_response(response: str) -> EvaluationResult:
    """Evaluate a babysitter's text response to a crisis scenario using a stub.

    Args:
        response: The babysitter's text response to the crisis scenario.

    Returns:
        EvaluationResult containing the hardcoded or mapped patience level and approach.
    """
    cleaned = response.strip().lower()

    if cleaned in _STUB_RESPONSES:
        return _STUB_RESPONSES[cleaned]

    # Keyword fallback for partial matches from the scenario examples
    if any(k in cleaned for k in ("deep breath", "sing", "quiet song", "calms down")):
        return EvaluationResult(patience_level="High", approach="Comforting")
    if any(k in cleaned for k in ("crib", "leave the room", "self-soothe")):
        return EvaluationResult(patience_level="Low", approach="Strict / Independent")
    if any(k in cleaned for k in ("distract", "toy", "screen")):
        return EvaluationResult(patience_level="Medium", approach="Distraction")

    # Default hardcoded return value
    return EvaluationResult(patience_level="High", approach="Comforting")
