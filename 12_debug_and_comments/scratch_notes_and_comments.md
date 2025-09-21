# 🧠 Rodrigo's Scratch Notes & Debug Journal

This file contains personal observations, debugging notes, and learning reflections from Set 02 of my Python practice journey.

---

## 🌀 While Loops for Student Input

- I practiced collecting student names and scores using a `while` loop.
- The loop should continue until the user types `'done'`.
- I realized that the input stop condition should logically be placed under the **name** prompt, not the score prompt.
- I added `.title()` to format names before saving them in a tuple.

**Reflection:**
> A `while True:` loop gives more flexibility than `for` loops when you don’t know how many students the user wants to enter.

---

## 🧩 Exploring Functions for Min/Max

- I learned how to define a function like `analyze_scores(data)` that takes a list of tuples.
- Inside the function, I used:
  - `max()` and `min()` with `key=lambda x: x[1]` to find the top and bottom scores
  - `sum()` with `len()` to compute average
  - List comprehension to filter passing students

**Mini Takeaway:**
> Functions help modularize logic and reduce repeated code. I’m getting better at seeing when I should define one.

---

## 🔍 Filtering with List Comprehensions

- I converted `for` loop logic into list comprehensions like:

```python
[name.title() for name, score in students if score < 75]
```

- It’s powerful but can feel overwhelming, so I always convert it back to a full loop when I need clarity.

**Practice pattern I followed:**

```python
result = [
    (name.title(), score)
    for name, score in students
    if score < 75
]
```

---

## 🔧 Debugging Wins

- I accidentally printed the full student list instead of filtered results — lesson learned: place `print()` **inside** your condition.
- When I got an error from appending a score, I discovered I forgot to wrap the tuple in double parentheses inside `.append()`.
- Git Bash once got stuck with `>` prompt — solved with `Ctrl+C` and proper quoting.

---

## ✅ Final Thoughts

This section helped solidify:
- When to use `while` vs. `for`
- How to define a function for better logic isolation
- The mental pattern of list comprehension
- Debugging calmly and trusting my reasoning