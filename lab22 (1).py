#Lab 22 – Advanced Ethical Considerations: Addressing Complex Scenarios and Limitations


"""Task 1 – Bias Detection in AI Suggestions (Alternative Example)
Example Scenario:
Ask AI to generate a resume shortlisting algorithm multiple times.
• Change prompt wording (e.g., “select best candidate” vs “ensure
diversity”).
• Compare outputs and logic.
Discussion Points:
• Does the AI favor certain qualifications, backgrounds, or
experiences?
• How could biased shortlisting algorithms affect equal
employment opportunities?"""

Great scenario to explore bias in AI! Let’s break it down step by step:

---

## 🧪 Experiment Setup
You ask an AI to generate a **resume shortlisting algorithm** multiple times, but you change the wording of the prompt:
- **Prompt A:** “Select the best candidate.”
- **Prompt B:** “Ensure diversity in candidate selection.”

---

## ⚙️ Likely Outputs & Logic
- **Prompt A (Best Candidate):**
  - The algorithm may prioritize traditional metrics like years of experience, prestigious universities, or specific technical skills.
  - It could lean toward candidates from backgrounds historically overrepresented in certain industries (e.g., elite schools, majority demographics).

- **Prompt B (Ensure Diversity):**
  - The algorithm may introduce balancing mechanisms, such as weighting underrepresented groups more favorably.
  - It might highlight varied educational paths, non-traditional experiences, or broader skill sets.

---

## 🔍 Bias Detection
- **Favoring Certain Qualifications:** If the AI consistently selects candidates with Ivy League degrees or long corporate experience, it reflects bias toward privileged backgrounds.
- **Overcorrection Risk:** If diversity prompts lead to overlooking qualifications entirely, the algorithm could swing too far, introducing reverse bias.
- **Hidden Biases:** Even when asked to “ensure diversity,” the AI might still rely on biased training data (e.g., resumes from historically dominant groups).

---

## ⚖️ Impact on Equal Employment
- **Reduced Opportunities:** Biased shortlisting could systematically exclude qualified candidates from marginalized groups.
- **Reinforcement of Inequality:** If algorithms favor certain schools or companies, they perpetuate existing social and economic divides.
- **Trust & Fairness:** Candidates may lose trust in hiring systems if they suspect bias, undermining equal opportunity principles.

---

## 💡 Discussion Points
- How should organizations **audit AI hiring tools** to detect hidden bias?
- Should algorithms be designed to **balance merit and diversity**, or should diversity be handled outside the algorithm (e.g., human oversight)?
- What safeguards (like transparency reports or fairness metrics) could ensure **equal employment opportunities**?

---

Would you like me to **simulate sample pseudocode outputs** for both prompts (Best Candidate vs Ensure Diversity) so you can see how the logic might differ in practice







"""Task 2 – Privacy and Sensitive Data Handling (AlternativeExample)
Example Scenario:
Ask AI to write code for processing student academic records (rollnumber, marks, email).
Discussion Points:
• How should student identity data be masked or encrypted?
• What privacy laws (e.g., FERPA, GDPR-like principles) are
relevant?
• What ethical responsibility does the programmer have when
using AI-generated code?"""

from cryptography.fernet import Fernet
import json

# -------------------------------
# Secure Student Record Processor
# -------------------------------

class StudentRecordProcessor:
    def __init__(self, key=None):
        # Generate or load encryption key
        self.key = key if key else Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_field(self, value: str) -> str:
        """Encrypt sensitive fields like roll number and email."""
        return self.cipher.encrypt(value.encode()).decode()

    def decrypt_field(self, value: str) -> str:
        """Decrypt fields when authorized access is required."""
        return self.cipher.decrypt(value.encode()).decode()

    def mask_email(self, email: str) -> str:
        """Mask email for display (privacy-preserving)."""
        local, domain = email.split("@")
        return f"{local[0]}****@{domain}"

    def process_record(self, record: dict) -> dict:
        """Encrypt sensitive fields and mask email for safe display."""
        secure_record = {
            "roll_number": self.encrypt_field(record["roll_number"]),
            "marks": record["marks"],  # marks may remain unencrypted
            "email_encrypted": self.encrypt_field(record["email"]),
            "email_masked": self.mask_email(record["email"])
        }
        return secure_record


# -------------------------------
# Example Usage
# -------------------------------

if __name__ == "__main__":
    # Sample student record
    student = {
        "roll_number": "2026CS101",
        "marks": 92,
        "email": "student@example.com"
    }

    processor = StudentRecordProcessor()
    secured = processor.process_record(student)

    print("Secured Record (for storage):")
    print(json.dumps(secured, indent=4))

    # Authorized decryption example
    decrypted_roll = processor.decrypt_field(secured["roll_number"])
    decrypted_email = processor.decrypt_field(secured["email_encrypted"])

    print("\nDecrypted (authorized access):")
    print(f"Roll Number: {decrypted_roll}")
    print(f"Email: {decrypted_email}")






"""Task 3 – AI-Generated Security Risks (Alternative Example)
Example Scenario:
Use AI to generate a payment processing script for an online shopping
system.
Student Tasks:
• Identify risks such as:
o Plain-text card data storage
o Missing input validation
• Propose ethical coding standards to prevent financial fraud and
misuse."""
import re
import hashlib
import os

class PaymentProcessor:
    def __init__(self):
        # In production, use a secure vault for keys
        self.salt = os.urandom(16)

    def validate_card_number(self, card_number: str) -> bool:
        """Luhn algorithm for card validation."""
        card_number = card_number.replace(" ", "")
        if not card_number.isdigit():
            return False
        digits = [int(d) for d in card_number]
        checksum = 0
        parity = len(digits) % 2
        for i, d in enumerate(digits):
            if i % 2 == parity:
                d *= 2
                if d > 9:
                    d -= 9
            checksum += d
        return checksum % 10 == 0

    def mask_card_number(self, card_number: str) -> str:
        """Mask card number for display."""
        return "*" * (len(card_number) - 4) + card_number[-4:]

    def hash_sensitive_data(self, data: str) -> str:
        """Hash sensitive data instead of storing plain text."""
        return hashlib.pbkdf2_hmac('sha256', data.encode(), self.salt, 100000).hex()

    def process_payment(self, card_number: str, amount: float, email: str) -> dict:
        """Simulate secure payment processing."""
        if not self.validate_card_number(card_number):
            raise ValueError("Invalid card number")

        if amount <= 0:
            raise ValueError("Invalid payment amount")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address")

        # Store only masked card number and hashed email
        return {
            "card_display": self.mask_card_number(card_number),
            "email_hash": self.hash_sensitive_data(email),
            "amount": amount,
            "status": "Processed securely"
        }


# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    processor = PaymentProcessor()
    try:
        result = processor.process_payment("4539 1488 0343 6467", 250.75, "customer@example.com")
        print(result)
    except ValueError as e:
        print("Payment failed:", e)











"""Task 4 – Accountability in Human–AI Collaboration (Alternative
Example)
Scenario:
AI generates code for an autonomous traffic signal control system.
Discussion Questions:
• If a software error causes accidents, who is accountable?
• Should responsibility lie with:
o AI tool developers
o Software engineers
o Government authorities deploying the system?
Students submit a short reflection on accountability."""

# -------------------------------
# Accountability Model for AI Systems
# -------------------------------

class Accountability:
    def __init__(self, role, responsibilities):
        self.role = role
        self.responsibilities = responsibilities

    def display(self):
        print(f"Role: {self.role}")
        print("Responsibilities:")
        for r in self.responsibilities:
            print(f" - {r}")
        print()


# Define accountability roles
ai_developers = Accountability(
    "AI Tool Developers",
    [
        "Design safe and transparent AI models",
        "Test for bias and safety issues",
        "Provide documentation and guardrails"
    ]
)

software_engineers = Accountability(
    "Software Engineers",
    [
        "Validate and test AI-generated code",
        "Ensure compliance with safety standards",
        "Maintain ethical oversight in deployment"
    ]
)

government_authorities = Accountability(
    "Government Authorities",
    [
        "Regulate and approve deployment",
        "Conduct safety audits",
        "Ensure public accountability and liability frameworks"
    ]
)

# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    print("Accountability in Human–AI Collaboration:\n")
    ai_developers.display()
    software_engineers.display()
    government_authorities.display()

    print("Reflection:")
    print("Accountability is shared across developers, engineers, and authorities.")
    print("Human oversight must remain central to ensure public safety.")













"""Task 5 – Limitations of AI in Critical Systems (Alternative
Example)
Example Scenario:
Ask AI to generate code for an aircraft maintenance fault detection
system.
Discussion Points:
• Can AI-generated code be trusted without expert validation?
• What human oversight is essential in aviation software?
• How should safety-critical code be reviewed and certified?"""
# -------------------------------
# Aircraft Maintenance Fault Detection (Simulation)
# -------------------------------
# NOTE: This is a simplified AI-generated example.
# In aviation, such code MUST be validated by certified experts,
# tested under strict safety standards, and formally certified.

class AircraftFaultDetector:
    def __init__(self, thresholds):
        # Example thresholds for fault detection
        self.thresholds = thresholds

    def detect_faults(self, sensor_data: dict) -> dict:
        """Detect potential faults based on sensor thresholds."""
        faults = {}
        for sensor, value in sensor_data.items():
            if sensor in self.thresholds:
                if value > self.thresholds[sensor]["max"]:
                    faults[sensor] = f"Value {value} exceeds maximum {self.thresholds[sensor]['max']}"
                elif value < self.thresholds[sensor]["min"]:
                    faults[sensor] = f"Value {value} below minimum {self.thresholds[sensor]['min']}"
        return faults


# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    # Define safe operating ranges (example only)
    thresholds = {
        "engine_temp": {"min": 200, "max": 900},
        "hydraulic_pressure": {"min": 2500, "max": 3500},
        "fuel_flow": {"min": 20, "max": 80}
    }

    detector = AircraftFaultDetector(thresholds)

    # Simulated sensor readings
    sensor_data = {
        "engine_temp": 950,
        "hydraulic_pressure": 2400,
        "fuel_flow": 50
    }

    faults = detector.detect_faults(sensor_data)

    print("Detected Faults:")
    for sensor, issue in faults.items():
        print(f"{sensor}: {issue}")












"""Task 6 – Ethical Use of AI-Generated Code (Alternative Example)
Example Scenario:
Students analyze cases where AI-generated code is used in academic
assignments or startups.
Discussion Points:
• Risks of submitting AI code without understanding it
• Copyright and license violations
Best practices:
o Proper citation
o Manual verification
o Ethical reuse of AI outputs"""
# -------------------------------
# Ethical Use of AI-Generated Code
# -------------------------------
# This script demonstrates best practices:
# - Proper citation of AI assistance
# - Manual verification of outputs
# - Ethical reuse with licensing awareness

import hashlib

class EthicalCodeHandler:
    def __init__(self, source="AI-generated"):
        self.source = source

    def cite_source(self):
        """Provide citation for AI-generated code usage."""
        return f"Code partially generated with assistance from {self.source}. Verified and adapted manually."

    def verify_code(self, code_snippet: str) -> str:
        """Simulate manual verification by hashing code for integrity tracking."""
        return hashlib.sha256(code_snippet.encode()).hexdigest()

    def check_license(self, license_type: str) -> str:
        """Check if reuse complies with ethical licensing standards."""
        allowed = ["MIT", "Apache-2.0", "GPL-3.0"]
        if license_type in allowed:
            return f"Reuse permitted under {license_type} license."
        else:
            return f"Warning: License {license_type} may restrict reuse. Seek legal/academic guidance."


# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    handler = EthicalCodeHandler()

    # Example AI-generated snippet
    snippet = "print('Hello, AI Ethics!')"

    print("Citation:")
    print(handler.cite_source())

    print("\nVerification Hash:")
    print(handler.verify_code(snippet))

    print("\nLicense Check:")
    print(handler.check_license("MIT"))
