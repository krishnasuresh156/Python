parrot = "Norwegian Blue"

# To print 5 characters starting from first character
print("parrot[0:6] : " + parrot[0:6]) 
print("parrot[3:5] : " + parrot[3:5])

print()
print("parrot[0:9] : " + parrot[0:9])  #both are same
print("parrot[:9]  : " + parrot[:9])   #both are same

print()
print("parrot[:9]    : " + parrot[:9])
print("parrot[10:14] : " + parrot[10:14])

print()
print("parrot[:6] : " + parrot[:6])
print("parrot[6:] : " + parrot[6:])
print("parrot[:6] + parrot[6:] : " + parrot[:6] + parrot[6:])   
print()
print("parrot[:]  : " + parrot[:])

print()
print('# Negative index in slicing')
print("parrot[0:6]    : " + parrot[0:6])        #Norweg
print("parrot[-14:-8] : " + parrot[-14:-8])     #Norweg
print()
print("parrot[-4:-2] : " + parrot[-4:-2])     #Bl
print("parrot[-4:12] : " + parrot[-4:12])     #Bl

print()
print('# slicing with step')
print("parrot[0:6:2] : " + parrot[0:6:2])
print("parrot[0:6:3] : " + parrot[0:6:3])

