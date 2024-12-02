# lab-7

import matplotlib.pyplot as plt

# Data for Madhya Pradesh
mp_parties = ['BJP', 'INC', 'BSP', 'Others']
mp_seats = [163, 66, 0, 1]

# Data for Rajasthan
raj_parties = ['INC', 'BJP', 'BSP', 'Others']
raj_seats = [69, 115, 2, 13]

# Pie charts with the highest percentage detached
def plot_pie_chart(parties, seats, title):
    plt.figure(figsize=(6, 6))
    explode = [0.1 if seat == max(seats) else 0 for seat in seats]
    plt.pie(seats, labels=parties, autopct='%1.1f%%', explode=explode, startangle=140)
    plt.title(title)
    plt.show()

# Subplot for pie charts
def plot_subplots_pie_charts(mp_parties, mp_seats, raj_parties, raj_seats):
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))

    # Madhya Pradesh
    explode_mp = [0.1 if seat == max(mp_seats) else 0 for seat in mp_seats]
    ax[0].pie(mp_seats, labels=mp_parties, autopct='%1.1f%%', explode=explode_mp, startangle=140)
    ax[0].set_title('Madhya Pradesh Assembly Results 2023')

    # Rajasthan
    explode_raj = [0.1 if seat == max(raj_seats) else 0 for seat in raj_seats]
    ax[1].pie(raj_seats, labels=raj_parties, autopct='%1.1f%%', explode=explode_raj, startangle=140)
    ax[1].set_title('Rajasthan Assembly Results 2023')

    plt.show()

# Bar chart for both states
def plot_bar_chart(mp_parties, mp_seats, raj_parties, raj_seats):
    # Aligning the parties and their respective seat numbers for both states
    parties = ['BJP', 'INC', 'BSP', 'Others']
    mp_seats_aligned = [mp_seats[mp_parties.index(p)] if p in mp_parties else 0 for p in parties]
    raj_seats_aligned = [raj_seats[raj_parties.index(p)] if p in raj_parties else 0 for p in parties]

    # Plotting
    x = range(len(parties))
    width = 0.3

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar([i - width / 2 for i in x], mp_seats_aligned, width, label='Madhya Pradesh', color='blue')
    ax.bar([i + width / 2 for i in x], raj_seats_aligned, width, label='Rajasthan', color='green')

    # Labeling
    ax.set_xlabel('Parties')
    ax.set_ylabel('Seats Won')
    ax.set_title('Comparison of Assembly Election Results 2023')
    ax.set_xticks(x)
    ax.set_xticklabels(parties)
    ax.legend()

    plt.show()

