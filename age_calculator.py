from datetime import datetime

def check_birthdate(year, month, day):
	birthday = datetime(year, month , day)
	today = datetime.now()
	if birthday > today :
		return false
	else:
		return ture
def calculate_age(year, month, day):
	birthday = datetime(year, month, day)
	today = datetime.now()
	difference = today - birthday
	age_in_days = difference.days
	age = age_in_days // 365
	print("you are {} years old".format(age))
def main():
	year = int(input("Enter year of birth: "))
	month = int(input("Enter month of birth: "))
	day = int(input("Enter day of birth: "))
	if (check_birthdate(year, month , day)):
		calculate_age(year, month,day)
	else:
		print ("Invalid birthdate. please try again")

if __name__ == '__main__':
	main()
