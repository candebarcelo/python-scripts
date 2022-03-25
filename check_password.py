# input as many passwords as u want and make it check how many times that password has been hacked.

import requests
import hashlib
import sys


# 3
# input query_char = first 5 digits of the hash
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    if response.status_code != 200:  # 200 is the code for success, 400 is for unsuccessful attempts
        raise RuntimeError(
            f'Error fetching: {response.status_code}, check the api and try again')
    # returns what is on the API page (the tails of the hashes that match the first 5
    return response
    # characters that you input)
    # and go back to #2


# 4
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    # .split splits each line at the : like the text import wizard in excel
    # .text turns it to text so it can be read
    # .splitlines() splits the text into lines, each is a list
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0  # if h != hash_to_check
    # go back to #1


# 2
# hashes the password in sha1
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # u need to encode to utf-8 (standard) bc otherwise it will error out
    # hexdigest returns the hash (otherwise it'd return its place in memory)
    # upper to turn it into uppercase like the hashes we get from the API
    # divides the hash into first 5 char and the rest
    first5char, tail = sha1password[:5], sha1password[5:]
    response2 = request_api_data(first5char)  # jumps to #3
    return get_password_leaks_count(response2, tail)  # jumps to #4


# 1
def main(args):  # args is/are the passwords you input on the terminal
    for password in args:
        count = pwned_api_check(password)  # jumps to #2
        if count:  # if it was found among the pwned passwords:
            print(
                f'{password} was found {count} times... You should probably change it.')
        else:
            print(f'{password} was NOT found. Carry on!')
    return 'done!'


if __name__ == '__main__':
    # sys.exit makes sure the process ends and closes the .py file afterwards
    sys.exit(main(sys.argv[1:]))
