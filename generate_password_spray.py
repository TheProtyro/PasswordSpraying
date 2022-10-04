#!/usr/bin/python3

# Tool used to generate a password spray wordlist
# Also usefull to crack hashes

import argparse
import os
import csv

parser = argparse.ArgumentParser(description="Password spray tool")
parser.add_argument("-c", "--company-name", help="Target company", type=str, required=True)
parser.add_argument("-j", "--job", help="Main job in the company", type=str, required=True)
parser.add_argument("-k", "--country", help="Target country", type=str, required=True)
parser.add_argument("-l", "--location", help="Target location", type=str, required=True)
parser.add_argument("-a", "--area-code", help="Target area code", type=str, required=True)
parser.add_argument("-y", "--year", help="Current year", type=str, required=True)
parser.add_argument("-p", "--password-min-length", help="Password minimum length", type=int, required=True)
parser.add_argument("-s", "--special-char", help="Special char, e.g. '!' or '*'", type=str)
parser.add_argument("-w", "--words", help="List of key words : word1,word2,word3", type=str)
args = parser.parse_args()

company = args.company_name
job = args.job
country = args.country
location = args.location
area_code = args.area_code
year = args.year
min_length = args.password_min_length
special_char = args.special_char
words = args.words.split(',')

# List of +1 and -3 years based on user input
years = [year]
years.append(str(int(year)+1))
years.append(str(int(year)-1))
years.append(str(int(year)-2))
years.append(str(int(year)-3))

# Generate seasons passwords
def generate_seasons():
	"""
	Autumn and fall are used interchangeably as words for the season between summer and winter. 
	Both are used in American and British English, but fall occurs more often in American English.
	Autumn is considered the more formal name for the season.
	"""
	with open(company + '.txt', 'a') as file:
		for year in years[0:3]:
			file.write('Winter' + year + '\n')
			file.write('Spring' + year + '\n')
			file.write('Summer' + year + '\n')
			file.write('Autumn' + year + '\n')
			file.write('Fall' + year + '\n')
			if special_char:
				file.write('Winter' + year + special_char + '\n')
				file.write('Spring' + year + special_char + '\n')
				file.write('Summer' + year + special_char + '\n')
				file.write('Autumn' + year + special_char + '\n')
				file.write('Fall' + year + special_char + '\n')

# Generate company related passwords
def generate_company():
	with open(company + '.txt', 'a') as file:
		file.write(company + '123' + '\n')
		file.write(company + '1' + '\n')
		file.write(company + area_code + '\n')
		if special_char:
			file.write(company + '123' + special_char + '\n')
			file.write(company + '1' + special_char + '\n')
			file.write(company + area_code + special_char + '\n')
		for year in years:
			file.write(company + year + '\n')
			if special_char:
				file.write(company + year + special_char + '\n')


# Generate country related passwords
def generate_country():
	with open(company + '.txt', 'a') as file:
		file.write(country + '123' + '\n')
		file.write(country + '1' + '\n')
		file.write(country + year + '\n')
		file.write(country + area_code + '\n')
		if special_char:
			file.write(country + '123' + special_char + '\n')
			file.write(country + '1' + special_char + '\n')
			file.write(country + year + special_char + '\n')
			file.write(country + area_code + special_char + '\n')

		# Generate passwords based on bordering countries
		# CSV from : https://github.com/geodatasource/country-borders
		countries = []
		csv_file = csv.reader(open('country_borders.csv', "r"), delimiter=",")
		for row in csv_file:
			if country == row[-1]:
				countries.append(row[1])
		for bordering_country in countries:
			file.write(bordering_country + '123' + '\n')
			file.write(bordering_country + '1' + '\n')
			file.write(bordering_country + year + '\n')
			if special_char:
				file.write(bordering_country + '123' + special_char + '\n')
				file.write(bordering_country + '1' + special_char + '\n')
				file.write(bordering_country + year + special_char + '\n')
		
		
# Generate location related passwords
def generate_location():
	with open(company + '.txt', 'a') as file:
		file.write(location + '123' + '\n')
		file.write(location + '1' + '\n')
		file.write(location + year + '\n')
		file.write(location + area_code + '\n')
		if special_char:
			file.write(location + '123' + special_char + '\n')
			file.write(location + '1' + special_char + '\n')
			file.write(location + year + special_char + '\n')
			file.write(location + area_code + special_char + '\n')

# Generate job related passwords
def generate_job():
	with open(company + '.txt', 'a') as file:
		file.write(job + '123' + '\n')
		file.write(job + '1' + '\n')
		file.write(job + year + '\n')
		file.write(job + area_code + '\n')
		if special_char:
			file.write(job + '123' + special_char + '\n')
			file.write(job + '1' + special_char + '\n')
			file.write(job + year + special_char + '\n')
			file.write(job + area_code + special_char + '\n')

# Generate key words related passwords
def generate_words():
	if words:
		with open(company + '.txt', 'a') as file:
			for word in words:
				file.write(word + '123' + '\n')
				file.write(word + '1' + '\n')
				file.write(word + year + '\n')
				file.write(word + area_code + '\n')
				if special_char:
					file.write(word + '123' + special_char + '\n')
					file.write(word + '1' + special_char + '\n')
					file.write(word + year + special_char + '\n')
					file.write(word + area_code + special_char + '\n')

# Apply the password policy
def apply_password_min_length():
	with open('best_passwords.txt','r') as filebp, open(company + '.txt', 'r') as filein, open(company + '_wordlist.txt', 'w') as fileout:
		best_passwords = filebp.readlines()
		for line in filein:
			# best_passwords exception
			if line in best_passwords:
				fileout.write(line)
			if len(line) > min_length:
				fileout.write(line)
	os.remove(company + '.txt')

# Add the "static" passwords based on the file best_passwords.txt
def generate_best_passwords():
	with open('best_passwords.txt','r') as filein, open(company + '.txt', 'a') as fileout:
		fileout.write('[empty password]\n')
		fileout.write('[username as password]\n')
		for password in filein:
			fileout.write(password)

if __name__ == "__main__":
	print("[+] Generating wordlist...")
	generate_best_passwords()
	generate_company()
	generate_job()
	generate_location()
	generate_words()
	generate_seasons()
	generate_country()
	apply_password_min_length()
	print("[+] " + company + "_wordlist.txt generated !\n")
	print("/!\ Don't forget to spray with the username as password, an empty password and the best passwords.\n Even if the passwords don't match the password policy.") 
