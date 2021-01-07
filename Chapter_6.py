#Author: Charles D. Maddux
#Date: 12/28/2020
#Description: Think Python Chapter 6 exercises

def ackermann(num_m, num_n, result=0):
    """
    performs the Ackermann Function
    :param num_m: int
    :param num_n: int
    :return: int(result)
    """
    if num_m == 0:
        result += num_n + 1
    if num_m > 0 and num_n == 0:
        result = ackermann(num_m - 1, 1)
    if num_m > 0 and num_n > 0:
        result = ackermann(num_m - 1, ackermann(num_m, num_n - 1))
    return result

def palindrome(word):
    """
    Checks to see if a word is a palindrome (spelled the same forward or backwards
    :param word: str
    """
    word_check = word[:: -1]
    if word_check.lower() == word.lower():
        return True
    return False

def is_power(num_a, num_b):
    """
    determines if num a is a power of num b
    :param num_a: int
    :param num_b: int
    :return: Boolean
    """
    if num_a == 1:
        return True
    if num_b == 0 or num_a % num_b != 0:
        return False
    return is_power(num_a / num_b, num_b)

def gcd(num_a, num_b):
    """
    adsf
    :param num_a:
    :param num_b:
    :return:
    """
    if num_a % num_b == 0:
        return num_b
    return gcd(num_b, num_a % num_b)

def main():
    """
    main body of program
    :return: 0
    """
    m = 3
    n = 4
    result = ackermann(m, n)
    print("Ackermann(", m, ",", n, ") = ", result, "\n")

    test_word = "tacocat"
    print("Is", test_word, "a palindrome?")
    check_pal = palindrome(test_word)
    if check_pal == True:
        print("Yes it is.\n")
    else:
        print("No it isn't.\n")

    number_a = 16777216
    number_b = 2
    check_for_power = is_power(number_a, number_b)
    print("Is " + str(number_a) + " a power of " + str(number_b) + "?")
    if check_for_power:
        print("Yes it is.")
    else:
        print("No, it isn't.")

    number_a = 70
    number_b = 18
    gcd_of_ab = gcd(number_a, number_b)
    print("What is the greatest common denominator of " + str(number_a) + " and " + str(number_b) + "?")
    print("It is " + str(gcd_of_ab) + ".\n")

main()