calls = 0
def count_calls():
	global calls
	calls += 1
	return calls
def string_info(string):
	tup = (len(string), string.upper(), string.lower())
	count_calls()
	return tup
def is_contains(string, list_to_search):
	count_calls()
	return any(item in string.lower() for item in list_to_search)
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)