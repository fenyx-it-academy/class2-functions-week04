def reading_number(two_digit_number=''):
    """gives the reading of entered two-digit number."""
    exceptional_numbers = ('Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
                           'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')
    units = ('', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')
    tens = ('', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety')
    if str(two_digit_number).isnumeric() is False:
        return 'All characters of the input must be number!'
    elif int(two_digit_number) < 10 or int(two_digit_number) > 99:
        return 'This function returns only two digit numbers'
    elif int(two_digit_number) < 20:
        return exceptional_numbers[int(str(two_digit_number)[1])]
    return tens[int(str(two_digit_number)[0])] + ' ' + units[int(str(two_digit_number)[1])]


print(reading_number(input('Please enter a two-digit number: ')))
