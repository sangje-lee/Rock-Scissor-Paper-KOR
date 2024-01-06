# print("This is game of Rock-paper-scissors")
# print()
# print("First player, what are you going to play?!")
# print("1. scissors")
# print("2. rock")
# print("3. paper")
# P1 = input()
# if P1 == '1':
#     P1 = "scissors"
# elif P1 == '2':
#     P1 = "rock"
# elif P1 == '3':
#     P1 = "paper"
# print()
# print("Second player, what are you going to play?!")
# print("1. scissors")
# print("2. rock")
# print("3. paper")
# P2 = input()
# if P2 == '1':
#     P2 = "scissors"
# elif P2 == '2':
#     P2 = "rock"
# elif P2 == '3':
#     P2 = "paper"
# print()
# print("The first  player played {0}.\nThe second player played {1}.".format(P1,P2))
#
# if P1 == 'scissors':
#     if P2 == 'scissors':
#         print("Tie! Both players are tied!")
#     elif P2 == 'rock':
#         print("{0} player won with {1}!".format('Second',P2))
#     elif P2 == 'paper':
#         print("{0} player won with {1}!".format('First',P1))
# elif P1 == 'rock':
#     if P2 == 'scissors':
#         print("{0} player won with {1}!".format('First',P1))
#     elif P2 == 'rock':
#         print("Tie! Both players are tied!")
#     elif P2 == 'paper':
#         print("{0} player won with {1}!".format('Second',P2))
# elif P1 == 'paper':
#     if P2 == 'scissors':
#         print("{0} player won with {1}!".format('Second',P2))
#     elif P2 == 'rock':
#         print("{0} player won with {1}!".format('First',P1))
#     elif P2 == 'paper':
#         print("Tie! Both players are tied!")

import random

player_win = 0
player_lost = 0
comp_win = 0
comp_lost = 0
both_win = 0
player_prob_win = 0
num_of_game = 0
# page_num = 0
possible_item = ['가위', '바위', '보']

player_total_win = 0
player_total_lost = 0

print("가위 바위 보 게입입니다.")
print()
# print("첫번째 플레이어 무엇을 낼 껀가요?!")
n = 0
while n == 0:
    print("플레이어 무엇을 낼 껀가요?!")
    print("1. 가위")
    print("2. 바위")
    print("3. 보")
    P1 = input()
    if P1 == '1':
        P1 = possible_item[0]
    elif P1 == '2':
        P1 = possible_item[1]
    elif P1 == '3':
        P1 = possible_item[2]
    print()
    P2 = random.randint(1,3)
    if P2 == 1:
        P2 = possible_item[0]
    elif P2 == 2:
        P2 = possible_item[1]
    elif P2 == 3:
        P2 = possible_item[2]
    print("플레이어는 {0}를 내셨습니다.\n컴퓨터는 {1}를 내셨습니다."
          .format(P1,P2))
    if P1 == possible_item[0]:
        if P2 == possible_item[0]:
            print("둘 다 비겼습니다!")
            both_win = both_win + 1
            # player_win = player_win + 1
            # comp_win = comp_win + 1
        elif P2 == possible_item[1]:
            print("{0} 가 {1}로 승리하였습니다!".format('컴퓨터',P2))
            comp_win = comp_win + 1
        elif P2 == possible_item[2]:
            print("{0} 가 {1}로 승리하였습니다!".format('플레이어',P1))
            player_win = player_win + 1
            # n = 1
    elif P1 == possible_item[1]:
        if P2 == possible_item[0]:
            print("{0} 가 {1}로 승리하였습니다!".format('플레이어', P1))
            player_win = player_win + 1
            # n = 1
        elif P2 == possible_item[1]:
            print("둘 다 비겼습니다!")
            both_win = both_win + 1
            # player_win = player_win + 1
            # comp_win = comp_win + 1
        elif P2 == possible_item[2]:
            print("{0} 가 {1}로 승리하였습니다!".format('컴퓨터', P2))
            comp_win = comp_win + 1
    elif P1 == possible_item[2]:
        if P2 == possible_item[0]:
            print("{0} 가 {1}로 승리하였습니다!".format('컴퓨터',P2))
            comp_win = comp_win + 1
        elif P2 == possible_item[1]:
            print("{0} 가 {1}로 승리하였습니다!".format('플레이어',P1))
            player_win = player_win + 1
            # n = 1
        elif P2 == possible_item[2]:
            print("둘 다 비겼습니다!")
            both_win = both_win + 1
            # player_win = player_win + 1
            # comp_win = comp_win + 1
    print("\n")
    print("Player :",player_win)
    print("Computer :",comp_win)
    print("Tie :",both_win)
    if player_win == 10:
        n = 1
        print("플레이어 승리")
    if comp_win == 10:
        n = 1
        print("컴퓨터 승리")

# print("두번째 플레이어 무엇을 낼 껀가요?!")
# print("1. 가위")
# print("2. 바위")
# print("3. 보")
# P2 = input()
# if P2 == '1':
#     P2 = "가위"
# elif P2 == '2':
#     P2 = "바위"
# elif P2 == '3':
#     P2 = "보"
# print()
# print("첫번째 플레이어는 {0}를 내셨습니다.\n두번째 플레이어는 {1}를 내셨습니다."
#       .format(P1,P2))



