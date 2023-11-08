def calculate_team_stats():
    games = 30
    total_points = 0
    win_count = 0

    for i in range(1, games + 1):
        points = int(input())
        total_points += points
        if points == 3:
            win_count += 1

    print(f"{total_points}",f"{win_count}" )
  


calculate_team_stats()
