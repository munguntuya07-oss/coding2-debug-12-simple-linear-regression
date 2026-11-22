"""Display your Homework 1 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "309e097d94163b413fad57523f4bdddd"
GRADE_HASH = "82626595abf2594763c2394374a251378ea7f7791660cd7b91c9f317d3eefd24"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 1: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
