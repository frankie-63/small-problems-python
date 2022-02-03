count = 0
for h in range(0, 23):
    for m in range(0, 59):
        if (round(h / 10 % 10) == m % 10) and ((h % 10) == round(m / 10 % 10)):
            count += 1

print(count)
