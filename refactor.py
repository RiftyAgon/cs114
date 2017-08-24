"""Convert a number in base-10 into a written out number in English."""


def get_tens(num):
    tens = num // 10
    return tens

def get_ones(num):
    ones = num % 10
    return ones

# def get_teens(num)
#     teens = num % 10
#     return teens

def get_tens_word(tens):
    """this function takes in a number and outputs the corresponding word"""
    if tens == 9:
        tens_word = 'ninety'
    elif tens == 8:
        tens_word = 'eighty'
    elif tens == 7:
        tens_word = 'seventy'
    elif tens == 6:
        tens_word = 'sixty'
    elif tens == 5:
        tens_word = 'fifty'
    elif tens == 4:
        tens_word = 'fourty'
    elif tens == 3:
        tens_word = 'thirty'
    elif tens == 2:
        tens_word = 'twenty'
    return tens_word
#
#
def get_ones_word(ones):
    if ones == 9:
        ones_word = 'nine'
    elif ones == 8:
        ones_word = 'eight'
    elif ones == 7:
        ones_word = 'seven'
    elif ones == 6:
        ones_word = 'six'
    elif ones == 5:
        ones_word = 'five'
    elif ones == 4:
        ones_word = 'four'
    elif ones == 3:
        ones_word = 'three'
    elif ones == 2:
        ones_word = 'two'
    elif ones == 1:
        ones_word = 'one'
    return ones_word

# def get_teens_word(teens):
#     if tens == 0:
#         output = ones_word
#     elif tens == 1:
#         if ones == 1:
#             output = 'eleven'
#         elif ones == 2:
#             output = 'twelve'
#         elif ones == 3:
#             output = 'thirteen'
#      return = ones_word + 'teen'


def main():
    num = int(input('A number between 1 and 99: '))

    # tens = num // 10
    # ones = num % 10
    # output = tens_word + '-' + ones_word
    ones_num = get_ones(num)
    ones_word = get_ones_word(ones_num)

    tens_num = get_tens(num)
    tens_word = get_tens_word(tens_num)

    # teens_num = get_teens(num)
    # teens_word = get_teens_word(teens_num)

    print(tens_word + ones_word)
    # print(ones_word)

    # get number input
    # if num == 11 or 12 or 13 or...
    #     output = runfunction()
    # else:
    #     standard logic
    #     output = result of standard logic
    # print(output)
main()
