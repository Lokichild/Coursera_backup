#original data
text = "X-DSPAM-Confidence:    0.8475"

#find the number
numbgn = text.find('0')
strnum = text[numbgn:]

#convert and print number
num = float(strnum)
print(num)