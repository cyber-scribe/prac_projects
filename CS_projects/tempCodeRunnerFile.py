import zxcvbn

def analyze_password(pw):
    result = zxcvbn.zxcvbn(pw)
    print("Score:", result['score'])
    print("Crack time:", result['crack_times_display']['offline_slow_hashing_1e4_per_second'])
    print("Feedback:", result['feedback'])

pw = input("Enter password: ")
analyze_password(pw)
