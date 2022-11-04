# Generate password spray

A tool used to generate a password spray wordlist.

Could also be useful to crack some hashes.

## Features

* Add static passwords based on the file `best-passwords.txt`. It is recommended to spray these passwords even if they don't match the password policy requirements. They are added at the start of the wordlist, including the **username as password** and the **empty password**.

* Generate dynamic passwords based on:
	* The company name (`-c`)
	* The main business job of the company (`-j`)
	* The location (`-l`)
	* The area code (`-a`)
	* The country (`-k`)
	* The bordering countries of the country (from [country_borders.csv](https://github.com/geodatasource/country-borders/))
	* The year (`-y`), the next year (+1) and the previous years (-3)
	* The seasons, recommended if the password policy requires a password change every three month.
	* The months, recommended if the password policy requires a password change every year.
	* Additional key words related to the company (`-w`)

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
	python3 generate_password_spray.py -c Company -j Consultant -k France -l Paris -a 75 -y 2022 -p 10

	# Optional arguments
	python3 generate_password_spray.py -c Company -j Consultant -k France -l Paris -a 75 -y 2022 -p 10 -s '!' -w 'Eiffel,Tower,Defense,Louvre'

## Wordlist example

	# python3 generate_password_spray.py -c Company -j Consultant -k France -l Paris -a 75 -y 2022 -p 10 -w 'Eiffel,Tower,Defense,Louvre'
	[+] Generating wordlist...
	[+] Company_wordlist.txt generated !

	/!\ Don't forget to spray with the username as password, an empty password and the best passwords.
	 Even if the passwords don't match the password policy.

	# cat Company_wordlist.txt
	[empty password]
	[username as password]
	P@ssw0rd
	P@ssw0rd01
	P@ssw0rd01
	Password123
	Password123
	Password1
	Password1!
	Password1!
	Hello123
	Welcome1
	Welcome1!
	Welcome01
	Welcome01!
	Welcome01!
	Company123
	Company2022
	Company2023
	Company2021
	Company2020
	Company2019
	Consultant123
	Consultant1
	Consultant2022
	Consultant75
	Eiffel2022
	Defense123
	Defense2022
	Louvre2022
	Winter2022
	Spring2022
	Summer2022
	Autumn2022
	Winter2023
	Spring2023
	Summer2023
	Autumn2023
	Winter2021
	Spring2021
	Summer2021
	Autumn2021
	January2022
	January2021
	February2022
	February2021
	August2022
	August2021
	September2022
	September2021
	October2022
	October2021
	November2022
	November2021
	December2022
	December2021
	France2022
	Andorra123
	Andorra2022
	Belgium123
	Belgium2022
	Switzerland123
	Switzerland1
	Switzerland2022
	Germany123
	Germany2022
	Luxembourg123
	Luxembourg1
	Luxembourg2022
	Monaco2022	
