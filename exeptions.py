# # Document original
# def palindrome(string):
#     return string == string[::-1]
#
# print(palindrome(1))

# # Document with Try and Except
# def palindrome(string):
#     return string == string[::-1]
#
#
# try:
#     print(palindrome(1))
# except TypeError:
#     print("solo se puede ingresar texto")

# # Document with Raise
# def palindrome(string):
#     try:
#         if len(string) == 0:
#             raise ValueError("No se permite una cadena vacia")
#         return string == string[::-1]
#     except ValueError as ve:
#         print(ve)
#         return False
#
#
# try:
#     print(palindrome(""))
# except TypeError:
#     print("solo se puede ingresar texto")

# # Document with Finally
# try:
#     f = open("archivo.txt")
#     # Hacer cualquier cosa con nuestro archivo
# finally:
#     f.close()


if __name__ == '__main__':
    palindrome()
