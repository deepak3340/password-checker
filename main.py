class Password_checker():
    def __init__(self):
        self.password = input("Enter password: ")
        try:
            with open("common_password.txt", "r") as f:
                self.common_pass = f.read().splitlines()
        except FileNotFoundError:
            self.common_pass = []
    def check(self):
        special = "!@#$%^&*()-_{=}+[]|;:',.<>?/`~"
        while True:
            score = 0
            self.why_not_strong = []
            if self.password.strip() in self.common_pass:
                print("This password is one of the most commonly used passwords.")
                self.password = input("Enter unique password: ")
            if any(i.isdigit() for i in self.password):
                score += 1
            else:
                self.why_not_strong.append("Add at least one digit.")
            if any(i.islower() for i in self.password):
                score += 1
            else:
                self.why_not_strong.append("Add lowercase letter.")
            if any(i.isupper() for i in self.password):
                score += 1
            else:
                self.why_not_strong.append("Add uppercase letter.")
            if len(self.password) >= 8:
                score += 1
            else:
                self.why_not_strong.append("Password must be at least 8 characters.")
            if any(i in special for i in self.password):
                score += 1
            else:
                self.why_not_strong.append("Add special symbol.")
            if score <= 2:
                print("🔴 Weak")
                self.password = input("enter strong password: ")
                continue
            elif score <= 4:
                print("🟡 Medium")
                with open("password_history.txt", "a") as f:
                    f.write(f"{self.password} -> Medium\n")
            else:
                print("🟢 Strong")
                with open("password_history.txt", "a") as f:
                    f.write(f"{self.password} -> Strong\n")
            if self.why_not_strong:
                print("\nSuggestions:")
                for i in self.why_not_strong:
                    print("✔", i)
            break
                
pass1 = Password_checker()
pass1.check()