# 💻 Number Representation – Computer Binary System

Computers use the **binary number system**, also known as the base-2 system, to represent and process information.

Unlike the decimal system, which uses ten different digits, binary uses only two:

```text
0 and 1
```

These digits are called **bits** (binary digits).

Different number systems use different bases:

| Number System | Base | Digits   |
| ------------- | ---- | -------- |
| Decimal       | 10   | 0–9      |
| Binary        | 2    | 0–1      |
| Octal         | 8    | 0–7      |
| Hexadecimal   | 16   | 0–9, A–F |

Binary is especially important because computers use electronic circuits that can represent two states:

* `0` → OFF / LOW
* `1` → ON / HIGH

---

# 🔢 Place Values

Just like the decimal system, binary is a **positional numeral system**.

However, instead of powers of 10, binary uses powers of 2.

Starting from the right:

| Position | Name        | Value | Power |
| -------- | ----------- | ----- | ----- |
| 1st      | Ones        | 1     | 2⁰    |
| 2nd      | Twos        | 2     | 2¹    |
| 3rd      | Fours       | 4     | 2²    |
| 4th      | Eights      | 8     | 2³    |
| 5th      | Sixteens    | 16    | 2⁴    |
| 6th      | Thirty-Twos | 32    | 2⁵    |

Each position is **2 times greater** than the position to its right.

For example:

```text
   1011

1 → Eights → 1 × 8
0 → Fours  → 0 × 4
1 → Twos   → 1 × 2
1 → Ones   → 1 × 1
```

Unlike decimal, each position can only contain `0` or `1`.

---

# 🧮 Breaking Down a Binary Number

Let's take the binary number `1011`.

We can represent it as:

```text
1011 = 1 × 8 + 0 × 4 + 1 × 2 + 1 × 1
```

Since each place value is a power of 2:

```text
1011 = 1 × 2³ + 0 × 2² + 1 × 2¹ + 1 × 2⁰
```

Which gives us:

```text
1011 = 8 + 0 + 2 + 1

1011 = 11 (decimal)
```

Another example:

```text
1001 = 1 × 2³ + 0 × 2² + 0 × 2¹ + 1 × 2⁰

     = 8 + 0 + 0 + 1

     = 9 (decimal)
```

**Important:** A binary number and a decimal number can contain the same digits but represent completely different values.

For example:

```text
1011 (binary) = 11 (decimal)
1011 (decimal) = 1011 (decimal)
```

The base determines how the number must be interpreted.

---

# ➕ Carry-Over

Carry-over works similarly to the decimal system.

However, binary only has two digits: `0` and `1`.

When adding two binary digits, the result can be:

| Addition | Result |
| -------- | ------ |
| 0 + 0    | 0      |
| 0 + 1    | 1      |
| 1 + 0    | 1      |
| 1 + 1    | 10     |

The important rule is:

```text
1 + 1 = 10 (binary)
```

We cannot write `2` in a single binary position.

Instead:

* We write `0` in the current position.
* We carry `1` to the next position on the left.

### Example: 1011 + 1001

```text
     1011
   + 1001
   ------
    10100
```

Step by step:

```text
1. Ones:
   1 + 1 = 10
   Write 0, carry 1.

2. Twos:
   1 + 0 + 1 = 10
   Write 0, carry 1.

3. Fours:
   0 + 0 + 1 = 1
   Write 1.

4. Eights:
   1 + 1 = 10
   Write 0, carry 1.

5. Final carry:
   Write 1 in the next position.
```

The final result is:

```text
1011 + 1001 = 10100 (binary)
```

In decimal:

```text
11 + 9 = 20
```

---

# 🧠 Why Does the Binary System Work This Way?

Binary is also a **positional numeral system**.

This means that:

* The same digit has a different value depending on its position.
* Each position represents a power of the base (2).
* Moving one position to the left multiplies the place value by 2.
* Moving one position to the right divides the place value by 2.

For example, the digit `1` can represent:

```text
1      → 1 × 1
10     → 1 × 2
100    → 1 × 4
1000   → 1 × 8
10000  → 1 × 16
```

The digit itself does not change, only its position and place value.

---

# 💡 Quick Summary

| Concept     | Meaning                                   |
| ----------- | ----------------------------------------- |
| Binary      | Base-2 number system                      |
| Bits        | Binary digits (0 and 1)                   |
| Place Value | Value determined by a digit's position    |
| Base        | Number of unique digits used              |
| Powers of 2 | Determine the value of each position      |
| Carry-Over  | Moves an extra value to the next position |

### Easy Way to Remember

```text
Sixteens   Eights   Fours   Twos   Ones
   2⁴        2³      2²      2¹     2⁰
    16        8       4       2      1

Moving LEFT  → Multiply by 2
Moving RIGHT → Divide by 2
```

The binary system represents numbers using only two digits and positional values based on powers of 2.

This makes it possible for computers to represent and process information using two electronic states.

---

# 📚 Next Topic

Continue with:

[`3_converting_decimal_binary.md`](3_converting_decimal_binary.md)

This file explains how to **convert decimal numbers into binary and binary numbers into decimal**, using step-by-step examples.