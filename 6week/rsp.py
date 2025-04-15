import random as rd

display_names = ['rock', 'scissors', 'paper']  

# Levi-Civita symbol 도입
epsilon = [[0,  1, -1],
           [-1, 0,  1],
           [1, -1, 0]]

# 입력
def user():
    user_input = input("Enter your choice (0: rock, 1: scissors, 2: paper): ")
    if user_input not in ["0", "1", "2"]:
        print("Invalid choice. Please try again.")
        return user()
    return int(user_input)

# 가위바위보 
def play():
    u = user()
    c = rd.randint(0, 2)

    # 선택 출력
    print(f"\nYou chose: {display_names[u]}")
    print(f"Computer chose: {display_names[c]}")

    result = epsilon[u][c]

    if result == 1:
        print("You win!")
    elif result == -1:
        print("You lose!")
    else:
        print(f"It's a draw! You both chose {display_names[u]}.")

play()
