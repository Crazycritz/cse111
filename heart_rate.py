heart_beat = 220 - int(input('What is your age? '))
slowest = heart_beat/100 *65
fastest = heart_beat/100 *85

print(f'You should keep your heart rate between {slowest} and {fastest} beats per minute when exercising!')
