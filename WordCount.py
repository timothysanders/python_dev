# comment for change commit

word_string = 'This is a string that Tim has created. This string has many words from Tim in different orders. This should count the number of characters in the string here.'

word_list = word_string.split()

word_dict = {}

for word in word_list:
  iterWord = word.lower().strip('.')
  if iterWord not in word_dict:
    word_dict[iterWord] = 1
  else:
    word_dict[iterWord] = word_dict[iterWord] + 1
