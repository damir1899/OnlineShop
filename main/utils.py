# from random import choice
# from django.forms import ValidationError

# def valid_price(price):
#     if int(price) <= 0:
#         raise ValidationError("price dont minus")
    
#     if not price.isdigit():
#         raise ValidationError("Prise is int")
    
#     num = "0123456789"
#     for i in price:
#         if i not in num:
#             raise ValidationError("Prise is not int")


# len_phone_text = [
#     "Достаточная длина номера телефона - не менее 12 символов",
#     "Убедитесь, что номер телефона состоит из 12 символов или больше",
#     "Минимальная длина номера телефона - 12 символов, проверьте",
#     "Необходимо ввести номер телефона, состоящий из не менее 12 символов",
#     "Укажите номер телефона длиной не менее 12 символов",
#     "Уточните номер телефона, должно быть не менее 12 символов",
#     "Проверьте длину номера телефона - должно быть не меньше 12 символов",
#     "Уведомление: номер телефона должен содержать не менее 12 символов",
#     "Необходимо ввести номер телефона, длиной не менее 12 символов",
#     "Внимание: допустимая длина номера телефона - 12 символов или больше",
# ]

# format_phone_text = [
#     "Укажите номер в формате международного набора цифр, пожалуйста!",
#     "Пожалуйста, введите номер телефона в международном формате!",
#     "Уточните номер, используя международный формат набора цифр!",
#     "Внимательно запишите номер телефона, соблюдая международный формат!",
#     "Необходимо указать номер в международном формате набора цифр!",
#     "Просим вас предоставить номер телефона в соответствии с международным форматом!",
#     "Уведомление: требуется указать номер в международном формате!",
#     "Запишите номер телефона в формате международного набора цифр, пожалуйста!",
#     "Укажите номер, соблюдая международный формат набора цифр!",
#     "Необходимо ввести номер телефона в международно признанном формате!",
# ]

# exception_phone_text = [
#     "Пожалуйста, исключите символ '{0}' из телефонного номера!",
#     "Убедитесь, что в номере отсутствует символ '{0}'!",
#     "Не допускается использование символа '{0}' в телефонном номере!",
#     "Проверьте номер на наличие символа '{0}', он не допустим!",
#     "Обратите внимание, что символ '{0}' не может быть включен в номер!",
#     "Телефонный номер не должен содержать символ '{0}', убедитесь в этом!",
#     "Укажите номер без символа '{0}', это недопустимо!",
#     "Внимание: символ '{0}' не разрешен в телефонном номере!",
#     "Просим вас исключить символ '{0}' из указываемого номера телефона!",
#     "Запишите номер без символа '{0}', это требование!",
# ]


# def validate_phone_number(phone_number: str):
#     phone_number = phone_number.replace(" ", "")
#     if len(phone_number) < 11:
#         raise ValidationError(choice(len_phone_text))
    
#     if not phone_number.startswith("+"):
#         raise ValidationError(choice(format_phone_text))
    
#     numbers = '+0123456789'
#     for i in phone_number:
#         if i not in numbers:
#             raise ValidationError(choice(exception_phone_text).format(i))

        