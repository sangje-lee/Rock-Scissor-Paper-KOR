# Project 'Rock Paper and Scissor Korean version'
# By Sangjin (Eric) Lee
# Last modified in 1/6/2024
# Project created in April 2020 published in 1/3/2024

import random
# import pandas as pd

from flask import Flask, render_template, request
app = Flask('My_RockScissorPaper_Game')

player_win = 0
player_lost = 0
comp_win = 0
comp_lost = 0
both_win = 0
player_prob_win = 100
num_of_game = 0

# Korean Version
possible_item = ['가위', '바위', '보']
winner_status = ['win', 'lose', 'tie']
possible_winner = ['N/A','플레이어','컴퓨터']

player_item = 0
computer_item = 0

player_drew = []
computer_drew = []
winner_drew = []
combination_drew = []

try:
    f = open("finalScore.txt", "r")
    player_prob_win_overall = str(f.read())
    f.close()

    player_prob_win_overall = player_prob_win_overall.split(" , ")

    player_total_win = int(player_prob_win_overall[0])
    player_total_lost = int(player_prob_win_overall[1])
    player_prob_win_overall = round(float(player_prob_win_overall[2]),2)
except Exception:
    print("Error founded! Score reset")
    player_total_win = 0
    player_total_lost = 0
    player_prob_win_overall = 0

# num_of_game_overall = 0
# page_num = 0

@app.route('/')
@app.route('/<player_win>')
@app.route('/<player_lost>')
@app.route('/<comp_win>')
@app.route('/<comp_lost>')
@app.route('/<prob_win>')
@app.route('/<num_game>')
@app.route('/<player_total_win>')
@app.route('/<player_total_lost>')
@app.route('/<display_scissor>')
@app.route('/<display_rock>')
@app.route('/<display_paper>')
@app.route('/<prob_round_win>')
@app.route('/<player_item_seq>')
@app.route('/<computer_item_seq>')
@app.route('/<winner_drew_seq>')
@app.route('/<combination_item_seq>')
def hello():
    # Set up initial page for Rock Scissor Paper
    return render_template('index.html',
                           player_win=player_win,
                           player_lost=player_lost,
                           comp_win=player_lost,
                           comp_lost=player_win,
                           prob_win=player_prob_win_overall,
                           num_game=str(num_of_game),
                           player_total_win=player_total_win,
                           player_total_lost=player_total_lost,
                           display_scissor=possible_item[0],
                           display_rock=possible_item[1],
                           display_paper=possible_item[2],
                           prob_round_win = player_prob_win,
                           player_item_seq = player_drew,
                           computer_item_seq = computer_drew,
                           winner_drew_seq = winner_drew,
                           combination_item_seq = combination_drew
                           )

@app.route('/result', methods=['POST'])
@app.route('/<player_win>')
@app.route('/<player_lost>')
@app.route('/<comp_win>')
@app.route('/<comp_lost>')
@app.route('/<prob_win>')
@app.route('/<num_game>')
@app.route('/<computer>')
@app.route('/<player>')
@app.route('/<winner>')
@app.route('/<final_winner>')
@app.route('/<player_total_win>')
@app.route('/<player_total_lost>')
@app.route('/<display_scissor>')
@app.route('/<display_rock>')
@app.route('/<display_paper>')
@app.route('/<prob_round_win>')
@app.route('/<player_item_seq>')
@app.route('/<computer_item_seq>')
@app.route('/<winner_drew_seq>')
@app.route('/<combination_item_seq>')
def gethello():
    global computer_item
    global player_item

    # if page_num == 0 : # Click me to see who win the game
    # page_num = 1
    player = request.values.get('options')

    if player == None:
        return render_template('index.html',
                           player_win=player_win,
                           player_lost=player_lost,
                           comp_win=player_lost,
                           comp_lost=player_win,
                           prob_win=player_prob_win_overall,
                           num_game=str(num_of_game),
                           player_total_win=player_total_win,
                           player_total_lost=player_total_lost,
                           display_scissor=possible_item[0],
                           display_rock=possible_item[1],
                           display_paper=possible_item[2],
                           prob_round_win = player_prob_win,
                           player_item_seq = player_drew,
                           computer_item_seq = computer_drew,
                           winner_drew_seq = winner_drew,
                           combination_item_seq = combination_drew
                           )
    winner = play_round(player)
    change_score(winner)
    candidate_winner = declare_winner()
    if candidate_winner == possible_winner[1]: # If Player score more than 10 point, Player win.
        final_winner = 1
        print(winner)
        return render_template('index2-end.html',
                                player_win=player_win,
                                player_lost=player_lost,
                                comp_win=player_lost,
                                comp_lost=player_win,
                                prob_win=player_prob_win_overall,
                                num_game=str(num_of_game),
                                computer=str(winner[2]),
                                player=str(winner[1]),
                                winner=str(winner[0]),
                                final_winner=str(final_winner),
                                player_total_win=player_total_win,
                                player_total_lost=player_total_lost,
                                display_scissor=possible_item[0],
                                display_rock=possible_item[1],
                                display_paper=possible_item[2],
                                prob_round_win = player_prob_win,
                                player_item_seq = player_drew,
                                computer_item_seq = computer_drew,
                                winner_drew_seq = winner_drew,
                                combination_item_seq = combination_drew
                                )
    elif candidate_winner == possible_winner[2]: # If Computer score more than 10 point, Computer win.
        final_winner = 2
        print(winner)
        return render_template('index2-end.html',
                                player_win=player_win,
                                player_lost=player_lost,
                                comp_win=player_lost,
                                comp_lost=player_win,
                                prob_win=player_prob_win_overall,
                                num_game=str(num_of_game),
                                computer=str(winner[2]),
                                player=str(winner[1]),
                                winner=str(winner[0]),
                                final_winner=str(final_winner),
                                player_total_win=player_total_win,
                                player_total_lost=player_total_lost,
                                display_scissor=possible_item[0],
                                display_rock=possible_item[1],
                                display_paper=possible_item[2],
                                prob_round_win = player_prob_win,
                                player_item_seq = player_drew,
                                computer_item_seq = computer_drew,
                                winner_drew_seq = winner_drew,
                                combination_item_seq = combination_drew
                                )
    else: # Otherwise, keep playing for next round!
          # This code will show who won in this round before proceed to next round!
        output_winner = winner_status.index(winner) + 1
        return render_template('result.html',
                                player_win=player_win,
                                player_lost=player_lost,
                                comp_win=comp_win,
                                comp_lost=comp_lost,
                                prob_win=player_prob_win_overall,
                                num_game=str(num_of_game),
                                computer=str(computer_item),
                                player=str(player_item),
                                winner=str(output_winner),
                                player_total_win=player_total_win,
                                player_total_lost=player_total_lost,
                                display_scissor=possible_item[0],
                                display_rock=possible_item[1],
                                display_paper=possible_item[2],
                                prob_round_win = player_prob_win,
                                player_item_seq = player_drew,
                                computer_item_seq = computer_drew,
                                winner_drew_seq = winner_drew,
                                combination_item_seq = combination_drew
                                )

@app.route('/round', methods=['POST'])
@app.route('/<player_win>')
@app.route('/<player_lost>')
@app.route('/<comp_win>')
@app.route('/<comp_lost>')
@app.route('/<prob_win>')
@app.route('/<num_game>')
@app.route('/<computer>')
@app.route('/<player>')
@app.route('/<winner>')
@app.route('/<final_winner>')
@app.route('/<player_total_win>')
@app.route('/<player_total_lost>')
@app.route('/<display_scissor>')
@app.route('/<display_rock>')
@app.route('/<display_paper>')
@app.route('/<prob_round_win>')
@app.route('/<player_item_seq>')
@app.route('/<computer_item_seq>')
@app.route('/<winner_drew_seq>')
def gethello2():
    # global page_num

    # Click me to move to next round
    # page_num = 0
    return render_template('index.html',
                           player_win=player_win,
                           player_lost=player_lost,
                           comp_win=player_lost,
                           comp_lost=player_win,
                           prob_win=player_prob_win_overall,
                           num_game=str(num_of_game),
                           player_total_win=player_total_win,
                           player_total_lost=player_total_lost,
                           display_scissor=possible_item[0],
                           display_rock=possible_item[1],
                           display_paper=possible_item[2],
                           prob_round_win = player_prob_win
                           )

@app.route('/reset', methods=['POST'])
@app.route('/<player_win>')
@app.route('/<player_lost>')
@app.route('/<comp_win>')
@app.route('/<comp_lost>')
@app.route('/<prob_win>')
@app.route('/<num_game>')
@app.route('/<player_total_win>')
@app.route('/<player_total_lost>')
def reset_hello():
    # Restart the game over again
    global player_win
    global player_lost
    global comp_win
    global comp_lost
    global both_win
    global player_item
    global computer_item
    global player_drew
    global computer_drew
    global winner_drew
    global combination_drew
    # global player_prob_win
    global num_of_game
    # global page_num

    # page_num = 0

    player_win = 0
    player_lost = 0
    comp_win = 0
    comp_lost = 0
    both_win = 0
    player_prob_win = 100
    num_of_game = 0

    player_item = 0
    computer_item = 0

    player_drew = []
    computer_drew = []
    winner_drew = []
    combination_drew = []

    return render_template('index.html',
                           player_win=player_win,
                           player_lost=player_lost,
                           comp_win=player_lost,
                           comp_lost=player_win,
                           prob_win=player_prob_win_overall,
                           num_game=str(num_of_game),
                           player_total_win=player_total_win,
                           player_total_lost=player_total_lost,
                           display_scissor=possible_item[0],
                           display_rock=possible_item[1],
                           display_paper=possible_item[2],
                           prob_round_win = player_prob_win,
                           player_item_seq = player_drew,
                           computer_item_seq = computer_drew,
                           winner_drew_seq = winner_drew,
                           combination_item_seq = combination_drew
                           )


# Change the probability of winner that was displayed on the website
def declare_winner():
    global player_prob_win_overall
    global player_total_win
    global player_total_lost
    # global player_prob_win

    # final_winner = ['N/A','플레이어','컴퓨터']
    if player_win == 10:
        player_total_win = player_total_win + 1
        player_prob_win_overall = (player_total_win/(player_total_win+player_total_lost)) * 100
        player_prob_win_overall = round(player_prob_win_overall,2)
        print(str(player_total_win)+"/("+str(player_total_win)+"+"+str(player_total_lost)+") * 100")

        update_file_winner()

        return possible_winner[1]
    elif comp_win == 10:
        player_total_lost = player_total_lost + 1
        player_prob_win_overall = (player_total_win/(player_total_win+player_total_lost)) * 100
        player_prob_win_overall = round(player_prob_win_overall,2)

        update_file_winner()

        return possible_winner[2]
    else:
        return possible_winner[0]

def update_file_winner():
    finalScore = str(player_total_win)+" , "+str(player_total_lost)+" , "+str(player_prob_win_overall)
    f = open("finalScore.txt", "w")
    f.write(finalScore)
    f.close()

# Change the score and update the score both internally and on the website
def change_score(winner):
    global player_win
    global player_lost
    global comp_win
    global comp_lost
    global player_prob_win
    global both_win
    global num_of_game

    if winner == winner_status[0]:
        player_win = player_win + 1
        comp_lost = comp_lost + 1
    elif winner == winner_status[1]:
        player_lost = player_lost + 1
        comp_win = comp_win + 1
    elif winner == winner_status[2]:
        both_win = both_win + 1

    num_of_game = num_of_game + 1
    player_prob_win = (player_win/num_of_game) * 100
    player_prob_win = round(player_prob_win,2)

# Check to see who win the round
def play_round(P1):

    global player_item
    global computer_item
    global possible_item

    # Human Player
    if P1 == '가위':
        P1 = possible_item[0]
    elif P1 == '바위':
        P1 = possible_item[1]
    elif P1 == '보':
        P1 = possible_item[2]
    player_item = possible_item.index(P1) + 1
    player_drew.append(possible_item[player_item-1])

    # Computer Player
    P2 = random.randint(1,3)
    if P2 == 1:
        P2 = possible_item[0]
    elif P2 == 2:
        P2 = possible_item[1]
    elif P2 == 3:
        P2 = possible_item[2]
    computer_item = possible_item.index(P2) + 1
    computer_drew.append(possible_item[computer_item-1])

    if P1 == possible_item[0]: # Scissor (Player)
        if P2 == possible_item[0]: # Scissor (Computer)
            # Tie!
            winner = winner_status[2]
        elif P2 == possible_item[1]: # Rock
            # Computer won!
            winner = winner_status[1]
        elif P2 == possible_item[2]: # Paper
            # Player won!
            winner = winner_status[0]
    elif P1 == possible_item[1]: # Rock
        if P2 == possible_item[0]:  # Scissor
            # Player won!
            winner = winner_status[0]
        elif P2 == possible_item[1]: # Rock
            # Tie!
            winner = winner_status[2]
        elif P2 == possible_item[2]: # Paper           
            # Computer won!
            winner = winner_status[1]
    elif P1 == possible_item[2]: # Paper
        if P2 == possible_item[0]: # Scissor        
            # Computer won!
            winner = winner_status[1]
        elif P2 == possible_item[1]: # Rock
            # Player won!
            winner = winner_status[0]
        elif P2 == possible_item[2]: # Paper
            # Tie!
            winner = winner_status[2]
    winner_drew.append(winner)

    combination_drew.append(str(possible_item[player_item-1]+"-"+
                                possible_item[player_item-1]+"-"+
                                winner))

    return winner

app.run()



