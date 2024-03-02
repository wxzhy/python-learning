from ln_cal import ln

a = float(input())
ln_value, error = ln(a)
print('ln(%.2f)=%.8f error=%.8f' % (a, ln_value, error))
