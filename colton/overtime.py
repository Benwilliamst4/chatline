OTP = .5
DTP = 2

NH = 40
OT = 10

PAY = 0.00

HOURS = int(input('Gimme hours poosy:'))
RATE = float(input('Gimme wage poosy:'))

if ((HOURS - NH) >= 10):
    PAY = PAY + (NH * RATE)
    PAY = PAY + ((((OT) * RATE)*OTP) + ((OT * RATE)))
    if ((HOURS - (NH + OT)) >= 0):
        PAY = PAY + (((HOURS - (NH + OT)) * RATE) * DTP)
else:
    if ((HOURS - NH) >= 0):
        PAY = PAY + (NH * RATE)
        PAY = PAY + ((((HOURS - NH) * RATE)*OTP) + ((HOURS - NH) * RATE))
    else:
        PAY = PAY + (HOURS * RATE)

print(f'Pay this boi: {PAY}')
