import sys

max = int(sys.argv[1]) + 1
# print(f'{max}:' + str(type(max)))
# print(sys.argv[1])
# print(sys.argv[0])

for i in range(1, int(max)):
	if i % 15 == 0:
		print('Fizzbuzz')
	elif i % 3 == 0:
		print('fizz')
	elif i % 5 == 0:
		print('buzz')
	else:
		print(i)

# ----hideo ver---
# import sys

# max = sys.argv[1]

# for num in range(int(max)):
#     str1 = '';
#     if (num +1) % 3 == 0:
#         str1 = 'fizz'
#     if (num +1) % 5 == 0:
#         str1 += 'buzz'
#     if str1 == '':
#         str1 = str(num +1)
#     print(str1)

# if __name__ == '__main__':
# 	if len(sys.argv) < 2:
# 		print("No argument")
# 		sys.exit()
# 	else
# 	    outputs = fizzbuzz()
#     	print(outputs)
