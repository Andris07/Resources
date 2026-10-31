# 🔄 Converting Decimal and Binary Numbers

There are two main ways to convert numbers between decimal and binary:

* **Decimal → Binary:** Convert a base-10 number into base-2.
* **Binary → Decimal:** Convert a base-2 number into base-10.

---

# 🔢 Binary → Decimal

To convert a binary number into decimal:

1. Start from the rightmost digit.
2. Assign powers of 2, starting with `2⁰`.
3. Multiply each binary digit by its corresponding power of 2.
4. Add all the results together.

### Example 1 – Easy

Convert `1011` into decimal.

```text
1011 (binary)

= 1 × 2³ + 0 × 2² + 1 × 2¹ + 1 × 2⁰

= 8 + 0 + 2 + 1

= 11 (decimal)
```

### Example 2 – Easy

Convert `11001` into decimal.

```text
11001 (binary)

= 1 × 2⁴ + 1 × 2³ + 0 × 2² + 0 × 2¹ + 1 × 2⁰

= 16 + 8 + 0 + 0 + 1

= 25 (decimal)
```

### Example 3 – Medium

Convert `10110110` into decimal.

```text
10110110 (binary)

= 1 × 2⁷ + 0 × 2⁶ + 1 × 2⁵ + 1 × 2⁴
  + 0 × 2³ + 1 × 2² + 1 × 2¹ + 0 × 2⁰

= 128 + 0 + 32 + 16 + 0 + 4 + 2 + 0

= 182 (decimal)
```

### Example 4 – Hard

Convert `110101101011` into decimal.

```text
110101101011 (binary)

= 1 × 2¹¹ + 1 × 2¹⁰ + 0 × 2⁹ + 1 × 2⁸
  + 0 × 2⁷ + 1 × 2⁶ + 1 × 2⁵ + 0 × 2⁴
  + 1 × 2³ + 0 × 2² + 1 × 2¹ + 1 × 2⁰

= 2048 + 1024 + 0 + 256 + 0 + 64
  + 32 + 0 + 8 + 0 + 2 + 1

= 3435 (decimal)
```

### Example 5 – Very Hard

Convert `1011011010110110` into decimal.

```text
1011011010110110 (binary)

= 1 × 2¹⁵ + 0 × 2¹⁴ + 1 × 2¹³ + 1 × 2¹²
  + 0 × 2¹¹ + 1 × 2¹⁰ + 1 × 2⁹ + 0 × 2⁸
  + 1 × 2⁷ + 0 × 2⁶ + 1 × 2⁵ + 1 × 2⁴
  + 0 × 2³ + 1 × 2² + 1 × 2¹ + 0 × 2⁰

= 32768 + 0 + 8192 + 4096 + 0 + 1024
  + 512 + 0 + 128 + 0 + 32 + 16
  + 0 + 4 + 2 + 0

= 46774 (decimal)
```

---

# 🔟 Decimal → Binary

To convert a decimal number into binary, use **repeated division by 2**.

1. Divide the decimal number by 2.
2. Write down the remainder (`0` or `1`).
3. Divide the quotient by 2 again.
4. Repeat until the quotient becomes `0`.
5. Read the remainders **from bottom to top**.

### Example 1 – Easy

Convert `13` into binary.

```text
13 ÷ 2 = 6 remainder 1
 6 ÷ 2 = 3 remainder 0
 3 ÷ 2 = 1 remainder 1
 1 ÷ 2 = 0 remainder 1

Read from bottom to top:

13 = 1101 (binary)
```

### Example 2 – Easy

Convert `42` into binary.

```text
42 ÷ 2 = 21 remainder 0
21 ÷ 2 = 10 remainder 1
10 ÷ 2 =  5 remainder 0
 5 ÷ 2 =  2 remainder 1
 2 ÷ 2 =  1 remainder 0
 1 ÷ 2 =  0 remainder 1

Read from bottom to top:

42 = 101010 (binary)
```

### Example 3 – Medium

Convert `156` into binary.

```text
156 ÷ 2 = 78 remainder 0
 78 ÷ 2 = 39 remainder 0
 39 ÷ 2 = 19 remainder 1
 19 ÷ 2 =  9 remainder 1
  9 ÷ 2 =  4 remainder 1
  4 ÷ 2 =  2 remainder 0
  2 ÷ 2 =  1 remainder 0
  1 ÷ 2 =  0 remainder 1

Read from bottom to top:

156 = 10011100 (binary)
```

### Example 4 – Hard

Convert `2025` into binary.

```text
2025 ÷ 2 = 1012 remainder 1
1012 ÷ 2 =  506 remainder 0
 506 ÷ 2 =  253 remainder 0
 253 ÷ 2 =  126 remainder 1
 126 ÷ 2 =   63 remainder 0
  63 ÷ 2 =   31 remainder 1
  31 ÷ 2 =   15 remainder 1
  15 ÷ 2 =    7 remainder 1
  7  ÷ 2 =    3 remainder 1
  3  ÷ 2 =    1 remainder 1
  1  ÷ 2 =    0 remainder 1

Read from bottom to top:

2025 = 11111101001 (binary)
```

### Example 5 – Very Hard

Convert `54321` into binary.

```text
54321 ÷ 2 = 27160 remainder 1
27160 ÷ 2 = 13580 remainder 0
13580 ÷ 2 =  6790 remainder 0
 6790 ÷ 2 =  3395 remainder 0
 3395 ÷ 2 =  1697 remainder 1
 1697 ÷ 2 =   848 remainder 1
  848 ÷ 2 =   424 remainder 0
  424 ÷ 2 =   212 remainder 0
  212 ÷ 2 =   106 remainder 0
  106 ÷ 2 =    53 remainder 0
   53 ÷ 2 =    26 remainder 1
   26 ÷ 2 =    13 remainder 0
   13 ÷ 2 =     6 remainder 1
    6 ÷ 2 =     3 remainder 0
    3 ÷ 2 =     1 remainder 1
    1 ÷ 2 =     0 remainder 1

Read from bottom to top:

54321 = 1101010000110001 (binary)
```

---

# 💡 Quick Summary

| Conversion       | Method                                                                   |
| ---------------- | ------------------------------------------------------------------------ |
| Binary → Decimal | Multiply each digit by its corresponding power of 2 and add the results. |
| Decimal → Binary | Repeatedly divide by 2 and read the remainders from bottom to top.       |

### Easy Way to Remember

```text
BINARY → DECIMAL

Multiply by powers of 2
          ↓
     Add the results


DECIMAL → BINARY

Repeated division by 2
          ↓
   Write down remainders
          ↓
  Read from bottom to top
```

Always remember that the **position of each digit matters** when converting between number systems.

---

# 📚 Next Topic

Continue with:

[`4_binary_addition.md`](4_binary_addition.md)

This file introduces **binary addition**, including addition rules, carry-over, and examples of adding binary numbers of different lengths.