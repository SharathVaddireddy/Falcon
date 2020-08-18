import bcrypt


def get_hashed_password(plain_text_password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt(10))


def check_password(plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text_password, hashed_password)


pwd = 'sharath'
hash = get_hashed_password(pwd)
copare = check_password('sharath', hash)

if check_password('sharath', hash):
    print('if')
    print(check_password('sharath', hash))
else:
    print('else')
    print(check_password('sharath', hash))
# print(hash, copare)
