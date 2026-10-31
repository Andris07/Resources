# 🔢 Number Representation – Human Decimal System

A **number system** is a way of representing numbers using a set of symbols and rules.

Different number systems use different bases:

| Number System | Base | Digits   |
| ------------- | ---- | -------- |
| Decimal       | 10   | 0–9      |
| Binary        | 2    | 0–1      |
| Octal         | 8    | 0–7      |
| Hexadecimal   | 16   | 0–9, A–F |

Humans commonly use the **decimal number system**, also known as the base-10 system.

It uses ten different digits:

```text
0 1 2 3 4 5 6 7 8 9
```

Each digit has a different value depending on its position in the number.

---

# 🔟 Place Values

In the decimal system, each position represents a power of 10.

Starting from the right:

| Position | Name          | Value | Power |
| -------- | ------------- | ----- | ----- |
| 1st      | Ones          | 1     | 10⁰   |
| 2nd      | Tens          | 10    | 10¹   |
| 3rd      | Hundreds      | 100   | 10²   |
| 4th      | Thousands     | 1000  | 10³   |
| 5th      | Ten Thousands | 10000 | 10⁴   |

Each position is **10 times greater** than the position to its right.

For example:

```text
   724

7 → Hundreds  → 7 × 100
2 → Tens      → 2 × 10
4 → Ones      → 4 × 1
```

A number is therefore the sum of its digits multiplied by their corresponding place values.

---

# 🧮 Breaking Down a Number

Let's take the number `724`.

We can represent it as:

```text
724 = 7 × 100 + 2 × 10 + 4 × 1
```

Since each place value is a power of 10:

```text
724 = 7 × 10² + 2 × 10¹ + 4 × 10⁰
```

Which gives us:

```text
724 = 700 + 20 + 4
```

Another example:

```text
5382 = 5 × 10³ + 3 × 10² + 8 × 10¹ + 2 × 10⁰

     = 5000 + 300 + 80 + 2
```

This is the fundamental principle of the decimal number system:

**Every digit contributes to the total value based on its position.**

---

# ➕ Carry-Over

Carry-over happens when a digit exceeds the maximum value allowed in its position.

In the decimal system, a single position can only contain a digit from `0` to `9`.

For example:

```text
9 + 1 = 10
```

We cannot write `10` in a single position.

Instead:

* We write `0` in the current position.
* We carry `1` to the next position on the left.

Example:

```text
   9
+  1
----
  10
```

The result can be understood as:

```text
9 × 10⁰ + 1 × 10⁰

= 10 × 10⁰

= 1 × 10¹ + 0 × 10⁰

= 10
```

The carried value becomes `1` in the next position, where it represents `1 × 10¹` instead of `1 × 10⁰`.

### Another Example

```text
   28
+  15
-----
   43
```

Step by step:

```text
1. Ones:
   8 + 5 = 13
   Write 3, carry 1.

2. Tens:
   2 + 1 + 1 = 4
   Write 4.
```

The final result is `43`.

---

# 🧠 Why Does the Decimal System Work This Way?

The decimal system is a **positional numeral system**.

This means that:

* The same digit can represent different values depending on its position.
* Each position represents a power of the base (10).
* Moving one position to the left multiplies the place value by 10.
* Moving one position to the right divides the place value by 10.

For example, the digit `5` can represent:

```text
5       → 5
50      → 5 × 10
500     → 5 × 100
5000    → 5 × 1000
```

The digit itself does not change, only its position and place value.

---

# 💡 Quick Summary

| Concept     | Meaning                                   |
| ----------- | ----------------------------------------- |
| Decimal     | Base-10 number system                     |
| Digits      | 0–9                                       |
| Place Value | Value determined by a digit's position    |
| Base        | Number of unique digits used              |
| Power of 10 | Determines the value of each position     |
| Carry-Over  | Moves an extra value to the next position |

### Easy Way to Remember

```text
Thousands   Hundreds    Tens    Ones
   10³         10²        10¹     10⁰
   1000         100        10       1

Moving LEFT  → Multiply by 10
Moving RIGHT → Divide by 10
```

The decimal system represents numbers using ten digits and positional values based on powers of 10.

Understanding this system is important because computers use a different number system internally: **binary (base-2)**.

---

# 📚 Next Topic

Continue with:

[`2_number_representation_computer_binary.md`](number_representation_computer_binary.md)

This file introduces the **binary number system**, explains how computers represent numbers using only `0` and `1`, and explores how positional values work in base-2.