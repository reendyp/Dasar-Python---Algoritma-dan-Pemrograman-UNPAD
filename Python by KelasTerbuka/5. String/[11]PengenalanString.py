data = "Hello, world. Ini adalah string"
print(data)
print(type(data))

# cara membuat string
'''
    1. menggunakan single quote (' ')
    2. menggunakan double quote (" ")
    
'''

print("ini print menggunakan double quote")
print('ini print menggunakan single quote')
print('"Hello, apa kabar?"')
print("'Hai, baik baik saja'")

# print tanda quote
print('g\'day, isn\'t it?') # gunakan backslash
# print backslash
print('c:user\\data\\data d') # gunakan double backslash

# menggunakan raw string
print(r'c:\user\new folder')

# multiline literal string 
print("""
      Nama  : ucup
      Kelas : kelas 3 SD
      """)

# multiline literal and raw string # semua yang ada didalam multiline and raw string dianggap string.
print(r"""
      Nama  : ucup
      Kelas : 3 SD \new normal
      """)

#fungsi tab
print('ini otong \t ini ucup, mereka berjauhan')
# fungsi backspace 
print('ini ucup \bini otong, mereka berdekatan')

#new line

print("baris pertama. \nbaris kedua") #line feed
print("baris pertama.\rbaris kedua.")# carriage return
print("baris pertama.\r\nbaris kedua ") # line feed carriage return