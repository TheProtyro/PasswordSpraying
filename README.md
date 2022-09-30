# Generate password spray

A tool used to generate a password spray wordlist.

Could also be useful to crack some hashes.

## Features

* Generate dynamic passwords based on:
	* The company name (`-c`)
	* The country (`-k`)
	* The bordering countries of the country (from [country_borders.csv](https://github.com/geodatasource/country-borders/))
	* The location (`-l`)
	* The year (`-y`), the next year (+1) and the previous years (-3)

* Add static passwords based on the file `best-passwords.txt`. It is recommended to spray these passwords even if they don't match the password policy. They are added at the end of the wordlist, including the **empty** password.

* Apply the minimum password length from the password policy (`-p`).

* Add special character of your choice at the end of the words (`-s`). You should avoid this option if you use the tool for cracking purpose and use the [OneRuleToRuleThemAll](https://github.com/NotSoSecure/password_cracking_rules/blob/master/OneRuleToRuleThemAll.rule) instead.

## Installation 

	pip3 install -r requirements.txt

## Usage

	python3 generate_password_spray.py -c Company -k France -l Paris -y 2022 -p 12 -s '!'
	python3 generate_password_spray.py -c Company -k Luxembourg -l Kirchberg -y 2022 -p 8 

## Output


	# python3 generate_password_spray.py -c Company -k France -l Paris -y 2022 -p 10 -s '!'
	[+] Generating wordlist...
	[+] Company_wordlist.txt generated !

	/!\ Don't forget to spray with the username as password, an empty password and the best passwords.
	 Even if the passwords don't match the password policy.

	# cat Company_wordlist.txt
	Winter2022
	Spring2022
	Summer2022
	Autumn2022
	Winter2022!
	Spring2022!
	Summer2022!
	Autumn2022!
	Winter2023
	Spring2023
	Summer2023
	Autumn2023
	Winter2023!
	Spring2023!
	Summer2023!
	Autumn2023!
	Winter2021
	Spring2021
	Summer2021
	Autumn2021
	Winter2021!
	Spring2021!
	Summer2021!
	Autumn2021!
	Company123
	Company123!
	Company2022
	Company2022!
	Company2023
	Company2023!
	Company2021
	Company2021!
	Company2020
	Company2020!
	Company2019
	Company2019!
	Paris2022!
	France2022
	France123!
	France2022!
	Andorra123
	Andorra2022
	Andorra123!
	Andorra2022!
	Belgium123
	Belgium2022
	Belgium123!
	Belgium2022!
	Switzerland123
	Switzerland1
	Switzerland2022
	Switzerland123!
	Switzerland1!
	Switzerland2022!
	Germany123
	Germany2022
	Germany123!
	Germany2022!
	Spain2022!
	Italy2022!
	Luxembourg123
	Luxembourg1
	Luxembourg2022
	Luxembourg123!
	Luxembourg1!
	Luxembourg2022!
	Monaco2022
	Monaco123!
	Monaco2022!

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
