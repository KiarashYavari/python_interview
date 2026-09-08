
## 1. What is a Hash Table?

A **hash table** is a data structure designed to answer questions like:

> “Have I seen this before?”
> “How many times have I seen this?”
> “What value belongs to this key?”



For example, imagine we want to store people's ages:

```python
ages = {
    "Alice": 25,
    "Bob": 31,
    "John": 19
}
```

Then:

```python
print(ages["Bob"])
```

returns:

```text
31
```

We don't need to scan through Alice, Bob, John one by one. The hash table can usually jump directly to `"Bob"`.

Average lookup:

```text
O(1)
```

That's the main reason hash tables appear so often in interviews.

---

# 2. Hash Table vs HashMap vs Dictionary

These terms are closely related.

A **hash table** is the general data structure.

A **HashMap** is usually a hash table storing:

```text
key → value
```

Python calls this a:

```python
dict
```

or **dictionary**.

So these are basically the same idea in different languages:

```text
Python       dict
Java         HashMap
C++          unordered_map
JavaScript   Map / Object
```

Example:

```python
student_grades = {
    "Alice": 90,
    "Bob": 82,
    "John": 95
}
```

Think of it as:

```text
Alice ───→ 90
Bob   ───→ 82
John  ───→ 95
```

The left side is the **key**.

The right side is the **value**.

---

# 3. What is a Set?

A set is also usually implemented using hashing, but instead of:

```text
key → value
```

it only stores:

```text
values
```

Example:

```python
users = {"Alice", "Bob", "John"}
```

The important property is:

> A set cannot contain duplicates.

For example:

```python
numbers = {1, 2, 2, 3, 3, 3}
```

becomes:

```python
{1, 2, 3}
```

So sets are extremely useful when the interview question says something like:

> duplicate
> unique
> already seen
> exists
> distinct

Those words should make you think:

```text
Maybe I need a set.
```

---

# 4. Dictionary vs Set

This distinction is important.

Use a **dictionary** when you need additional information about something.

For example:

```python
frequency = {
    "apple": 3,
    "banana": 2
}
```

We care about both:

```text
item → count
```

Use a **set** when you only care whether something exists.

```python
seen = {"apple", "banana"}
```

We are asking:

```text
Have I seen "apple"?
```

not:

```text
How many apples did I see?
```

A useful interview rule is:

| Question                 | Data structure |
| ------------------------ | -------------- |
| Have I seen X?           | `set`          |
| How many X?              | `dict`         |
| What belongs to X?       | `dict`         |
| Remove duplicates        | `set`          |
| Map one thing to another | `dict`         |

---

# 5. Pattern #1 — Fast Lookup

Suppose we have:

```python
numbers = [10, 25, 7, 42, 13, 8]
```

And someone asks:

> Does `42` exist?

The simple approach:

```python
42 in numbers
```

Python may need to scan:

```text
10
25
7
42
```

Worst case:

```text
O(n)
```

But suppose we do:

```python
numbers = {10, 25, 7, 42, 13, 8}

if 42 in numbers:
    print("Found")
```

Lookup is average:

```text
O(1)
```

This is one of the biggest uses of hash tables.

---

# 6. Pattern #2 — Detect Duplicates

Here's a classic interview problem.

### Problem

Given:

```python
nums = [3, 1, 4, 2, 5, 1]
```

Return `True` if any number appears more than once.

A beginner might compare every number to every other number:

```text
3 vs 1
3 vs 4
3 vs 2
...
1 vs 4
1 vs 2
...
```

That becomes approximately:

```text
O(n²)
```

Instead, use a set:

```python
def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False
```

Let's trace it.

Starting with:

```python
seen = set()
```

Read `3`:

```text
3 in seen? No

seen = {3}
```

Read `1`:

```text
1 in seen? No

seen = {1, 3}
```

Read `4`:

```text
4 in seen? No

seen = {1, 3, 4}
```

Eventually we reach the second `1`:

```text
1 in seen? YES
```

Return:

```python
True
```

Time:

```text
O(n)
```

Space:

```text
O(n)
```

This is an extremely common interview pattern:

```python
seen = set()

for item in items:
    if item in seen:
        ...
    seen.add(item)
```

I would memorize this pattern.

---

# 7. Pattern #3 — Frequency Counting

Another huge interview pattern.

Suppose:

```python
nums = [1, 2, 2, 3, 3, 3]
```

We want:

```text
1 appears 1 time
2 appears 2 times
3 appears 3 times
```

Use a dictionary:

```python
count = {}

for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
```

Result:

```python
{
    1: 1,
    2: 2,
    3: 3
}
```

Think:

```text
number → frequency
```

The dictionary evolves like this:

```text
Read 1

{1: 1}
```

Then:

```text
Read 2

{1: 1, 2: 1}
```

Read another `2`:

```text
{1: 1, 2: 2}
```

Read `3` three times:

```text
{1: 1, 2: 2, 3: 3}
```

There's also a shorter Python version:

```python
for num in nums:
    count[num] = count.get(num, 0) + 1
```

Here:

```python
count.get(num, 0)
```

means:

> Give me the current count. If the key doesn't exist yet, use `0`.

---

# 8. Real Interview Example — Most Frequent Element

Suppose the interviewer says:

> Given an array, find the element that appears most frequently.

Example:

```python
nums = [1, 2, 2, 3, 3, 3, 4]
```

We first count:

```python
{
    1: 1,
    2: 2,
    3: 3,
    4: 1
}
```

Then find the largest count.

```python
def most_frequent(nums):
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    best_num = None
    best_count = 0

    for num, freq in count.items():
        if freq > best_count:
            best_num = num
            best_count = freq

    return best_num
```

Returns:

```python
3
```

Notice the interview thought process:

```text
Question says "most frequent"

↓

I need to know how many times each thing occurs.

↓

item → count

↓

Dictionary / HashMap
```

That mental translation is more important than memorizing code.

---

# 9. Pattern #4 — Mapping Relationships

HashMaps aren't only for counting.

They can represent relationships.

Imagine an employee database:

```python
employees = {
    101: "Alice",
    102: "Bob",
    103: "John"
}
```

That's:

```text
employee ID → employee name
```

Or:

```python
manager = {
    "Alice": "Sarah",
    "Bob": "Sarah",
    "John": "Michael"
}
```

That's:

```text
employee → manager
```

Or in an interview problem:

```python
phone_owner = {
    "555-1234": "Alice",
    "555-5678": "Bob"
}
```

That's:

```text
phone number → owner
```

This becomes especially important later with:

* graphs
* caching
* Two Sum
* grouping
* adjacency lists
* memoization

---

# 10. One of the Most Famous Interview Problems — Two Sum

Suppose:

```python
nums = [2, 7, 11, 15]
target = 9
```

Find two numbers whose sum is `9`.

Obviously:

```text
2 + 7 = 9
```

A brute-force solution checks:

```text
2 + 7
2 + 11
2 + 15
7 + 11
...
```

That's:

```text
O(n²)
```

But there's a smarter question.

When looking at `7`, we need:

```text
9 - 7 = 2
```

So ask:

> Have I already seen `2`?

That is exactly what a hash table is good at.

```python
def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i
```

Trace it:

```text
nums = [2, 7, 11, 15]
target = 9
```

First:

```text
num = 2

needed = 9 - 2
       = 7

Have we seen 7?
No.

Store:
2 → index 0
```

Dictionary:

```python
{2: 0}
```

Next:

```text
num = 7

needed = 9 - 7
       = 2
```

Ask:

```text
Is 2 in seen?
```

Yes!

```python
seen[2] = 0
```

Current index:

```text
1
```

Return:

```python
[0, 1]
```

Time:

```text
O(n)
```

This problem is a perfect example of the core HashMap technique:

> Instead of searching the rest of the array, remember what you've already seen.

---

# 11. Why is HashMap Lookup O(1)?

At a high level, a hash table uses something called a **hash function**.

Imagine:

```python
ages["Bob"]
```

Internally Python does something conceptually similar to:

```text
"Bob"

 ↓

hash("Bob")

 ↓

some number

 ↓

location in memory

 ↓

31
```

So instead of scanning:

```text
Alice?
No.

John?
No.

Bob?
Yes.
```

it calculates where `"Bob"` should be stored.

That's why lookup is normally:

```text
O(1)
```

You don't usually implement the hashing algorithm yourself in DSA interviews.

Python handles it for you.

---

# 12. Then Why Can Worst Case Be O(n)?

Different keys can sometimes produce locations that conflict.

This is called a:

> **hash collision**

Conceptually imagine:

```text
hash("Alice") → bucket 5
hash("Bob")   → bucket 5
```

Both want the same place.

The hash table has to handle the collision.

If many items collide, lookup can degrade toward:

```text
O(n)
```

So interview complexity is usually stated as:

```text
Insert:   O(1) average
Lookup:   O(1) average
Delete:   O(1) average

Worst case: O(n)
```

For normal LeetCode/interview analysis, you usually say **average O(1)**.

genui{"learning_viz":{"type_id":"BIG_O_TIME_COMPLEXITY"}}

---

# 13. The Four Patterns I Want You to Recognize

When reading an interview problem, start looking for these signals:

### A. Existence

Question:

> Have I seen this before?

Think:

```python
set()
```

Example:

```python
if x in seen:
```

---

### B. Frequency

Question:

> How many times does this appear?

Think:

```python
dict
```

Example:

```python
count[x] = count.get(x, 0) + 1
```

---

### C. Mapping

Question:

> What information belongs to this key?

Think:

```python
dict
```

Example:

```text
user → email
number → index
employee → manager
```

---

### D. Deduplication

Question:

> Give me only unique elements.

Think:

```python
set
```

For example:

```python
nums = [1, 1, 2, 3, 3]

unique = set(nums)
```

gives:

```python
{1, 2, 3}
```

---

## A very useful interview mental model

Don't immediately think:

> "I need a HashMap."

Instead, ask:

```text
1. What information do I need to remember?

2. What should be the key?

3. What should be the value?
```

For example, **Two Sum**:

```text
What do I remember?
Numbers I've already seen.

Key?
number

Value?
its index

So:

number → index
```

For frequency counting:

```text
What do I remember?
How often each number occurs.

Key?
number

Value?
count

So:

number → count
```

For duplicate detection:

```text
What do I remember?
Only whether I've seen the number.

No extra value is needed.

So:
Set
```

This way of thinking will help you solve problems you haven't memorized.
