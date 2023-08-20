number=int(input("Integer number back to binary: "))
binary=[128, 64, 32, 16, 8, 4, 2, 1]
nums=0
convert=0
def can_convert(number):
  global binary
  global nums, convert
  convert=2
  print(type(binary))
  for i in binary:
    nums+=i
  while number>nums:
    new_binary=binary[0]*convert
    binary.append(new_binary)
    convert*=2
    nums=0
    for i in binary:
      nums+=i
  else:
    binary.sort()
    binary.reverse()
    return binary, nums, convert

def convert_to_Binary(number):
  global binary
  can_convert(number)
  if number>255:
    can_convert(number)
  else: 
    pass
  binary_number=""
  binary_int=0
  for x in binary:
    if number>x and number>=binary_int+x:
      binary_number+="1"
      binary_int+=x
    else:
      binary_number+="0"
  return binary_number, binary
while type(number)==int:
  print(convert_to_Binary(number), convert)
  binary=[128, 64, 32, 16, 8, 4, 2, 1]
  number=int(input("Integer number back to binary: "))
else:
  quit()