# 1st program
print(9**0.5 * 5)

# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1)

# 3rd program
print(2 * 2 + 2)
print(2 * (2 + 2))
print(2 * 2 + 2 == 2 * (2 + 2))

# 4th program
string_number = '123.456'
float_number = float(string_number)
shifted_number = float_number * 10
integer_part = int(shifted_number)
first_digit_after_point = integer_part % 10
print(first_digit_after_point)