def number_to_words(number):
    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одинадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать",
             "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    if number == 0:
        return "ноль"

    result = ""

    if number >= 100:
        result += hundreds[number // 100] + " "
        number %= 100

    if number >= 10 and number < 20:
        result += teens[number - 10]
        return result

    if number >= 20:
        result += tens[number // 10] + " "
        number %= 10

    if number > 0:
        result += units[number]

    return result


try:
    num = int(input("Введите число от 1 до 1000: "))
    if num < 1 or num > 1000:
        print("Число должно быть в диапазоне от 1 до 1000")
    else:
        words = number_to_words(num)
        print(f"{words}")
except ValueError:
    print("Ошибка: Введите целое число.")
