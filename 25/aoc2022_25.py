def snafu_to_int(s: str) -> int:
    snafu_dict = {'0':0, '1':1, '2':2, '-':-1, '=':-2}
    value = 0
    for digit in s:
        value = 5*value + snafu_dict[digit]
    return(value)

def int_to_snafu(x: int) -> str:
    s = ''
    snafu_digits = '012=-'
    while x:
        rem = (x + 2) % 5 - 2
        s = snafu_digits[rem] + s
        x = (x - rem) // 5
    return s
        
filename = "input.txt"
with open(filename) as f:
    snafus = (line.strip() for line in f.readlines())
s = sum(snafu_to_int(snafu) for snafu in snafus)
print(s, int_to_snafu(s))



