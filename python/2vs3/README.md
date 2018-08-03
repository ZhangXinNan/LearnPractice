
# range is a generator object
In python3 range is a generator object - it does not return a list. Convert it to a list before shuffling.
```
allocations = list(range(len(people)))
```
[TypeError: 'range' object does not support item assignment](https://stackoverflow.com/questions/20484195/typeerror-range-object-does-not-support-item-assignment)

# error UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff
[error UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte](https://stackoverflow.com/questions/42339876/error-unicodedecodeerror-utf-8-codec-cant-decode-byte-0xff-in-position-0-in)
```
with open(path, 'rb') as f:
  contents = f.read()
```
That b in the mode specifier in the open() states that the file shall be treated as binary, so contents will remain a bytes. No decoding attempt will happen this way.


# UnicodeDecodeError: 'charmap' codec can't decode byte 0x8d in position 29: character maps to <undefined>


