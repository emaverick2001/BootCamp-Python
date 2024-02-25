import pandas as pd
import math
import matplotlib.pyplot as plt
import random
# Maverick Espinosa
# mespin11

# Task 1

def calculate_ratings(past_matches):
    
    """
    Function: calculate_ratings: calculates the match ratings for players 0-7

    Parameters
    ----------
    past_matches : file containing players and match info

    Returns
    -------
    players : dictionary containing player: rating values

    """
    # Initialize player ratings to 1500
    players = {key: 1500 for key in range(8)}
    try:
        # Read CSV file into a DataFrame
        df = pd.read_csv(past_matches, index_col=0)
    
        for index, row in df.iterrows():
            try:
                player_a = row['player_A']
                player_b = row['player_B']
                winner = row['winner']
                
                # Calculate the win probability for Player a and b
                prob_a = math.exp((players[player_a] - players[player_b])/100) / (1 + math.exp((players[player_a] - players[player_b])/100))
                prob_b = 1 - prob_a
                
                # Update player ratings based on match outcome
                if winner == player_a:
                    players[player_a] += 5*(1.0 - prob_a)
                    players[player_b] += 5*(0.0 - prob_b)
                    continue
                players[player_a] += 5*(0.0 - prob_a)
                players[player_b] += 5*(1.0 - prob_b)
            except KeyError as e:
                print(f"Error: Column not found - {e}")
                return players
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                return players
            
    except FileNotFoundError:
        print("Error: File not found")
    else:
        return players


# Task 2

def display_ratings(player_ratings):
    """
    Function: display_ratings: displays players ratings as a bar chart 
    Parameters
    ----------
    player_ratings : dictionary with player id as key and rating as value

    Returns
    -------
    None.

    """
    
    plt.rc('font', family='serif')
    
    plt.figure(figsize=(6,5))
    players = list(player_ratings.keys())
    ratings = list(player_ratings.values())
    
    # Set labels and limits for the plot
    plt.ylabel('Rating', fontsize=24)
    plt.xlabel('Players', fontsize=24)
    plt.ylim(1000,2000)
    
    # set tick marks for x and y axis
    plt.xticks(fontsize=24)
    plt.yticks([i*200 + 0 for i in range(10)], fontsize=24) 
    
    # Create a bar chart
    plt.bar(players,ratings)
    
    # Adjust layout and save the plot as a PDF
    plt.tight_layout()
    plt.savefig('projections.pdf')
    plt.show()
    return


# Task 3

def simulate_match(player_ratings, player_a, player_b):
    """
    Function: simulate_match: helper function that simulates a match between two players

    Parameters
    ----------
    player_ratings : dictionary with player id as key and rating as value
    player_a : player a's id
    player_b : player b's id

    Returns
    -------
    winning player id

    """
    delta = (player_ratings[player_a] - player_ratings[player_b]) / 100
    prob_a = math.exp(delta) / (1 + math.exp(delta))
    return player_a if random.random() < prob_a else player_b

def project_win_probs(player_ratings):
    """
    Function: project_win_probs: calculates each players probability of winning a tournament based on 100 tournament participations

    Parameters
    ----------
    player_ratings : dictionary with player id as key and rating as value

    Returns
    -------
    player_wins : dictionary with player id as key and probability of winning a tournament as a value

    """
    player_wins = {key: 0 for key in range(8)}
    
    # Define the match structure
    match_structure = [(0, 7), (1, 6), (2, 5), (3, 4)]
    
    for _ in range(100):
        # Simulate initial matches
        winners = [simulate_match(player_ratings, a, b) for a, b in match_structure]
        
        # Simulate next round
        winners_next_round = [simulate_match(player_ratings, winners[i], winners[i + 1]) for i in range(0, len(winners), 2)]
        
        # Simulate final round
        tournament_winner = simulate_match(player_ratings, winners_next_round[0], winners_next_round[1])
        
        # Update win count
        player_wins[tournament_winner] += 1
    
    player_wins = {key:value/100 for key, value in player_wins.items()}
    return player_wins

# Task 4

def display_probs(player_wins_prob):
    """
    Function: display_probs: displayes players winning probabilities as a pie chart and organizing them in descending order as a csv file

    Parameters
    ----------
    player_wins_prob : dictionary with player id as key and probability of winning a tournament as a value

    Returns
    -------
    None.

    """
    # Save probabilities to a CSV file
    df_prob = pd.DataFrame(player_wins_prob.items(), columns=['Player', 'Probability'])
    df_prob = df_prob.sort_values(by='Probability', ascending=False)
    df_prob.to_csv('probs.csv', index=False)
    
    # Read the saved CSV file
    dfw = pd.read_csv('probs.csv')
    print(dfw)
    
    # Create a pie chart
    labels = dfw['Player']
    sizes = dfw['Probability']
    explode = (0.1, 0, 0, 0, 0, 0, 0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Save the pie chart as a PDF
    fig1.savefig('projections_pie.pdf')

    plt.show()

    