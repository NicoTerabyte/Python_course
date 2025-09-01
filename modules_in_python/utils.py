import	random

#questo file serve solo per spiegare come funzionano i moduli

meters_in_one_km = 1000
team = ["Alessandro Del piero", "Francesco Totti", "Gigi Buffon"]

def	get_file_ext(filename):
	return filename[filename.index(".") + 1]

def	roll_dice(num):
	return random.randint(1, num)
