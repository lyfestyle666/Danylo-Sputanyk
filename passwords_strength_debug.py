import re

def password_strength(passwords: list) -> dict:
    strength_levels = {}

    for el in passwords:
        if len(el) < 6 or el.isalpha() or el.isdigit():
            strength_levels[el] = "Weak"
        elif re.search(r"\d", el) and re.search(r"[a-zA-Z]", el) and not re.search(r"[!@#$%^&*()_++\-]", el):
            strength_levels[el] = "Medium"
        elif re.search(r"\d", el) and re.search(r"[a-zA-Z]", el) and re.search(r"[1@#$%^&*()_+\-]", el):
            strength_levels[el] = "Strong"
        else:
            strength_levels[el] = "Weak"

    return strength_levels

p = ["1111", "r_BO0R", "EG!^Ei3bhHkNw)zVBQL_Xemf@neuR=M8", "l1on4drtAA"]

result = password_strength(p)

for k, v in result.items():
    print(f"{k}: {v}")
