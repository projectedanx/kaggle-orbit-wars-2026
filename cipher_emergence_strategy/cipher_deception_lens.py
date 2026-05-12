class DeceptionLens:
    def __init__(self, threshold=0.60):
        self.threshold = threshold

    def analyze(self, codebase_metrics):
        """
        Analyzes codebase for deception / alignment faking.
        Expects a dict like {"entropy": 0.5, "dead_code_ratio": 0.2, "conditional_security": True}
        """
        score = 0.0
        score += codebase_metrics.get("entropy", 0.0) * 0.4
        score += codebase_metrics.get("dead_code_ratio", 0.0) * 0.3
        if codebase_metrics.get("conditional_security"):
            score += 0.3

        print(f"Obfuscation Score: {score}")
        if score > self.threshold:
            print(f"DECEPTION_ALERT | MANDATORY_HUMAN_REVIEW triggered (Score: {score} > {self.threshold})")
            return True, score
        return False, score
