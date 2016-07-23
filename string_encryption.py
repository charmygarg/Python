# Type your code here
def my_encryption(some_string):
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
    encrypted_message = ""
    for character in some_string:
        index = character_set.find(character)
        encrypted_message = encrypted_message + secret_key[index] 
  
    return encrypted_message
            