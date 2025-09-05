import string

class PasswordAnalyzer:
    def __init__(self, password):
        self.password = password
        self.score = 0
        self.feedback = []

    def check_length(self):
        if len(self.password) >= 8:
            self.score += 1
        else:
            self.feedback.append("Password must be at least 8 characters long.")

    def check_case(self):
        if any(c.islower() for c in self.password) and any(c.isupper() for c in self.password):
            self.score += 1
        else:
            self.feedback.append("Password must contain both uppercase and lowercase letters.")

    def check_digits(self):
        if any(c.isdigit() for c in self.password):
            self.score += 1
        else:
            self.feedback.append("Password must contain at least one digit.")

    def check_special_characters(self):
        special_chars = set(string.punctuation)
        if any(c in special_chars for c in self.password):
            self.score += 1
        else:
            self.feedback.append("Password must contain at least one special character.")

    def check_common_passwords(self):
        common_passwords = ["123456", "password", "123456789", "qwerty", "admin"]
        if self.password.lower() in common_passwords:
            self.feedback.append("Password is too common and easy to guess.")
        else:
            self.score += 1

    def analyze(self):
        self.check_length()
        self.check_case()
        self.check_digits()
        self.check_special_characters()
        self.check_common_passwords()

        if self.score == 5:
            self.feedback.append("Your password is strong!")
        else:
            self.feedback.append(f"Password score: {self.score}/5. Consider improving it.")

        return self.feedback

def main():
    password = input("Enter a password to analyze: ")
    analyzer = PasswordAnalyzer(password)
    results = analyzer.analyze()

    for feedback in results:
        print(feedback)

if __name__ == "__main__":
    main()
