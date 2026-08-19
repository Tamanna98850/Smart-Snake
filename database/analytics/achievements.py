import sqlite3
import pandas as pd


# =================================
# DATABASE CONNECTION
# =================================

connection = sqlite3.connect(
    "game_history.db"
)


# =================================
# GET ACHIEVEMENTS
# =================================

query = """
SELECT
    player_name,
    achievement_name,
    description,
    score,
    unlocked_at

FROM achievements

ORDER BY score DESC
"""


df = pd.read_sql_query(
    query,
    connection
)


connection.close()


# =================================
# CHECK DATA
# =================================

print("\n")
print("==========================================")
print("       🏆 SMART SNAKE ACHIEVEMENTS")
print("==========================================")


if df.empty:

    print("\nNo achievements unlocked yet.")

else:

    print()

    print(df.to_string(
        index=False
    ))