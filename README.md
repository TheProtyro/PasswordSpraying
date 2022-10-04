# Generate password spray

A tool used to generate a password spray wordlist.

Could also be useful to crack some hashes.

## Features

* Generate dynamic passwords based on:
	* The company name (`-c`)
	* The location (`-l`)
	* The area code (`-a`)
	* The country (`-k`)
	* The bordering countries of the country (from [country_borders.csv](https://github.com/geodatasource/country-borders/))
	* The year (`-y`), the next year (+1) and the previous years (-3)
	* Additional key words related to the company (`-w`)

* Add static passwords based on the file `best-passwords.txt`. It is recommended to spray these passwords even if they don't match the password policy requirements. They are added at the start of the wordlist, including the **username as password** and the **empty password**.

* Apply the minimum password length from the password policy (`-p`). Use `-p 0` for cracking purpose.

* Add special character of your choice at the end of the words (`-s`). You should avoid this option if you use the tool for cracking purpose and use the [OneRuleToRuleThemAll](https://github.com/NotSoSecure/password_cracking_rules/blob/master/OneRuleToRuleThemAll.rule) instead.

## Disclaimer

Password spraying refers to the attack method that takes a large number of usernames and attempt against them a single password.

**You must strictly respect the password policy during sprays to avoid locking all the accounts. DO NOT SPRAY THE WORDLIST AT ONCE !**

Password policy includes among other things:

* The lockout threshold = limit of login attempts before lockout.
* The observation window = minutes after the last failed login before being able to make another attempt.

The maximal number of attempts possible on 24 hours = (Lockout threshold - 1) * (60 / observation window) * 24

## Installation 

	pip3 install -r requirements.txt

## Usage

	# help
	python3 generate_password_spray.py -h

	# Mandatory arguments
	python3 generate_password_spray.py -c Company -j Accountant -k Luxembourg -l Kirchberg -a 57 -y 2022 -p 12

	# Optional arguments
	python3 generate_password_spray.py -c Company -j Accountant -k Luxembourg -l Kirchberg -a 57 -y 2022 -p 12 -s '*' -w 'Excel,Bank,Insurance'

## Output

	
	# python3 generate_password_spray.py -c Company -j Accountant -k Luxembourg -l Kirchberg -a 57 -y 2022 -p 12 -s '*' -w 'Excel,Bank,Insurance'

	# cat Company_wordlist.txt
	[empty password]
	[username as password]
	P@ssw0rd
	P@ssw0rd01
	Password123
	Password1
	Password1!
	Hello123
	Welcome1
	Welcome1!
	Welcome01
	Welcome01!
	Company2022*
	Company2023*
	Company2021*
	Company2020*
	Company2019*
	Accountant123
	Accountant2022
	Accountant57
	Accountant123*
	Accountant1*
	Accountant2022*
	Accountant57*
	Kirchberg123
	Kirchberg2022
	Kirchberg123*
	Kirchberg2022*
	Kirchberg57*
	Insurance123
	Insurance2022
	Insurance123*
	Insurance2022*
	Insurance57*
	Luxembourg123
	Luxembourg2022
	Luxembourg57
	Luxembourg123*
	Luxembourg1*
	Luxembourg2022*
	Luxembourg57*
	Belgium2022*
	Germany2022*
