"""Terminal UI for AI Babysitter Crisis Response Evaluation (Scenario 1).

Reads a babysitter's response to a crisis scenario from the terminal,
evaluates it using the personality evaluation module, and prints the result.
Exits when the user presses Enter on an empty line.
"""

import sys
from pathlib import Path

# Ensure root directory is in sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

try:
    from source.personality_evaluation import evaluate_response
except ImportError:
    from personality_evaluation import evaluate_response


def main() -> None:
    """Run the interactive terminal interface for Scenario 1."""
    print("=== AI Babysitter: Crisis Response Evaluation ===")
    print("Enter a babysitter's response (or press Enter on an empty line to exit):\n")

    while True:
        try:
            response = input("Babysitter response: ")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break

        if not response.strip():
            print("Exiting...")
            break

        result = evaluate_response(response)
        print(f"Patience Level: {result.patience_level}")
        print(f"Approach: {result.approach}\n")


if __name__ == "__main__":
    main()
