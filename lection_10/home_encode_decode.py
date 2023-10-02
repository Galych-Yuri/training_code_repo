home_string = b'r\xc3\xa9sum\xc3\xa9'

home_default_decoding = home_string.decode()
print(home_default_decoding)  # résumé
home_encoding_latin1 = home_default_decoding.encode('latin1')
print(home_encoding_latin1)  # b'r\xe9sum\xe9'
home_decoding_latin1 = home_encoding_latin1.decode('latin1')
print(home_decoding_latin1)  # résumé





