from statsbombpy import sb

competitions = sb.competitions()

matches = sb.matches(competition_id=9, season_id=42)

print(matches)
