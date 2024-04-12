import multiprocessing
import numpy as np
from datetime import datetime
def print_smth(some_inpt):
	arr = []
	for x in range(some_inpt):
		# print("Something " + str(x))
		arr.append(x**3)

def mp_prnt_smth(some_inpt):
	# print("Something " + str(some_inpt))
	some_inpt**3

def main():
	st_time = datetime.now()
	print_smth(10000)
	en_time = datetime.now()
	print("Operation finished in ", en_time-st_time)

	print("*" * 100)

	pool = multiprocessing.Pool(4)
	st_time = datetime.now()
	pool.map(mp_prnt_smth, np.arange(10000))
	en_time = datetime.now()
	print("Operation finished in ", en_time - st_time)

if __name__ == "__main__":
	main()
