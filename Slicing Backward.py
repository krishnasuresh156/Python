letters = "abcdefghijklmnopqrstuvwxyz"
print('letters = "abcdefghijklmnopqrstuvwxyz"')
backwards = letters[25:0:-1]
print(backwards)

print()
print("To print above string value in reverse order: letters[25::-1]")
backwards = letters[25::-1]
print(backwards)

print()
print("To print above string value in reverse order: letters[::-1]")
backwards = letters[::-1]
print(backwards)


print()
print("To print qpa: letters[16:13:-1]")
print(letters[16:13:-1])

print()
print("To print edcba: letters[4::-1]")
print(letters[4::-1])

print()
print("To print last 8 characters in reverse order: letters[25:17:-1]")
print(letters[25:17:-1])

print()
print("To print last 8 characters in reverse order: letters[:-9:-1]")
print(letters[:-9:-1])

print()
print("SLICING IDIOMS")
print("letters[-4:] : " + letters[-4:])
print("letters[-1:] : " + letters[-1:])
print("letters[:1] : " + letters[:1])
print("letters[0] : " + letters[0])


