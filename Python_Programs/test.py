binary=[128, 64, 32, 16, 8, 4, 2, 1]
nums=0
def can_convert(number):
  global binary
  global nums
  convert=2
  print(type(binary))
  for i in binary:
    nums+=i
  while number>nums:
    print(type(binary))
    new_binary=binary[0]*convert
    print(type(binary))
    binary.append(new_binary)
    print(type(binary), binary, nums)
    print(type(binary), binary,nums)
    convert+=2
    nums=0
    for i in binary:
      nums+=i
  else:
    binary.sort()
    binary.reverse()
    return binary, nums
print(can_convert(1000))