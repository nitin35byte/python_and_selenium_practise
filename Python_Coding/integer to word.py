def number_to_words(num):
    def one_to_nineteen(n):
        words = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"
        ]
        return words[n]

    def tens(n):
        words = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        return words[n]

    def two_digit_number(n):
        if n < 20:
            return one_to_nineteen(n)
        else:
            return tens(n // 10) + (" " + one_to_nineteen(n % 10) if n % 10 != 0 else "")

    def three_digit_number(n):
        if n < 100:
            return two_digit_number(n)
        else:
            return one_to_nineteen(n // 100) + " Hundred" + (
                " and " + two_digit_number(n % 100) if n % 100 != 0 else "")

    def large_number(n, scale):
        if n == 0:
            return ""
        else:
            return three_digit_number(n) + " " + scale

    if num == 0:
        return "Zero"

    billions = num // 1_000_000_000
    millions = (num // 1_000_000) % 1_000
    thousands = (num // 1_000) % 1_000
    remainder = num % 1_000

    result = ""

    if billions > 0:
        result += large_number(billions, "Billion")
    if millions > 0:
        result += " " if result else ""
        result += large_number(millions, "Million")
    if thousands > 0:
        result += " " if result else ""
        result += large_number(thousands, "Thousand")
    if remainder > 0:
        result += " " if result else ""
        result += three_digit_number(remainder)

    return result


# Example usage
number = 1234567890
print(number_to_words(number))
