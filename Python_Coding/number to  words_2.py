def number_to_words(num):
    below_20 = [
        'Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
        'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
        'Seventeen', 'Eighteen', 'Nineteen'
    ]
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    thousands = ['', 'Thousand', 'Million', 'Billion']

    def word(num):
        if num == 0:
            return ""
        elif num < 20:
            return below_20[num]
        elif num < 100:
            return tens[num // 10] + (" " + below_20[num % 10] if num % 10 != 0 else "")
        else:
            return below_20[num // 100] + " Hundred" + (" " + word(num % 100) if num % 100 != 0 else "")

    def recursive_conversion(num):
        if num == 0:
            return "Zero"

        i = 0
        words = ""

        while num > 0:
            if num % 1000 != 0:
                words = word(num % 1000) + " " + thousands[i] + " " + words
            num //= 1000
            i += 1

        return words.strip()

    return recursive_conversion(num)


# Example usage
number = 987654321
print(number_to_words(number))
