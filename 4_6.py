# Simple program to compute an employee's gross pay, including overtime. Assumes time and a half overtime.
def computepay():
    hrs = input("Please provide employee hours: ")
    rate = input("Please provide employee's payrate: ")
    h = float(hrs)
    r = float(rate)
    if h <= 40: 
        tpay = h * r
    else :
        bpay = 40 * r
        ohrs = h - 40
        orate = r * 1.5
        opay = ohrs * orate
        tpay = bpay + opay
    return (tpay)

print('Pay ' + str(computepay()))