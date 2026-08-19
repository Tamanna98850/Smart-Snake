import sqlite3
import pandas as pd
import numpy as np


# ==========================================
# DATABASE PATH
# ==========================================

DB_PATH = "game_history.db"


# ==========================================
# LOAD GAME DATA
# ==========================================

def load_game_data():

    connection = sqlite3.connect(
        DB_PATH
    )

    query = """
        SELECT
            player_name,
            score,
            snake_length,
            level,
            food_type,
            game_date
        FROM game_history
        ORDER BY score DESC
    """

    df = pd.read_sql_query(
        query,
        connection
    )

    connection.close()

    return df


# ==========================================
# PERFORMANCE ANALYSIS
# ==========================================

def analyze_performance():

    df = load_game_data()

    if df.empty:

        return None


    # ======================================
    # NUMPY ARRAYS
    # ======================================

    scores = np.array(
        df["score"],
        dtype=float
    )

    lengths = np.array(
        df["snake_length"],
        dtype=float
    )

    levels = np.array(
        df["level"],
        dtype=float
    )


    # ======================================
    # STATISTICS
    # ======================================

    total_games = len(scores)

    best_score = np.max(
        scores
    )

    lowest_score = np.min(
        scores
    )

    average_score = np.mean(
        scores
    )

    median_score = np.median(
        scores
    )

    score_difference = (
        best_score -
        lowest_score
    )

    average_length = np.mean(
        lengths
    )

    average_level = np.mean(
        levels
    )

    score_std = np.std(
        scores
    )


    # ======================================
    # PERFORMANCE %
    # ======================================

    if best_score > 0:

        performance_percentage = (
            average_score /
            best_score
        ) * 100

    else:

        performance_percentage = 0


    # ======================================
    # PERFORMANCE CATEGORY
    # ======================================

    if performance_percentage >= 80:

        category = "EXCELLENT"

    elif performance_percentage >= 60:

        category = "GOOD"

    elif performance_percentage >= 40:

        category = "AVERAGE"

    else:

        category = "NEEDS IMPROVEMENT"


    # ======================================
    # BEST GAME
    # ======================================

    best_index = np.argmax(
        scores
    )

    best_game = df.iloc[
        best_index
    ]


    # ======================================
    # SMART RECOMMENDATION
    # ======================================

    if performance_percentage >= 80:

        recommendation = (
            "Excellent performance. "
            "Try increasing the difficulty."
        )

    elif performance_percentage >= 60:

        recommendation = (
            "Good performance. "
            "Try to improve your best score."
        )

    elif performance_percentage >= 40:

        recommendation = (
            "Keep practicing and avoid "
            "obstacles carefully."
        )

    else:

        recommendation = (
            "Practice basic movement and "
            "food collection."
        )


    # ======================================
    # RESULT
    # ======================================

    result = {

        "total_games":
            total_games,

        "best_score":
            best_score,

        "lowest_score":
            lowest_score,

        "average_score":
            average_score,

        "median_score":
            median_score,

        "score_difference":
            score_difference,

        "average_length":
            average_length,

        "average_level":
            average_level,

        "score_std":
            score_std,

        "performance_percentage":
            performance_percentage,

        "category":
            category,

        "best_player":
            best_game["player_name"],

        "best_game_score":
            best_game["score"],

        "best_game_length":
            best_game["snake_length"],

        "best_game_level":
            best_game["level"],

        "recommendation":
            recommendation
    }


    return result


# ==========================================
# EXPORT GAME HISTORY
# ==========================================

def export_game_history():

    df = load_game_data()


    if df.empty:

        print(
            "\nNo game data available."
        )

        return


    file_name = (
        "analytics_game_history.csv"
    )


    df.to_csv(
        file_name,
        index=False
    )


    print(
        "\nGame history exported successfully!"
    )

    print(
        f"File: {file_name}"
    )


# ==========================================
# EXPORT PERFORMANCE REPORT
# ==========================================

def export_performance_report():

    result = analyze_performance()


    if result is None:

        print(
            "\nNo game data available."
        )

        return


    report = pd.DataFrame({

        "Metric": [

            "Total Games",

            "Best Score",

            "Lowest Score",

            "Average Score",

            "Median Score",

            "Score Difference",

            "Average Snake Length",

            "Average Level",

            "Score Variation",

            "Performance Percentage",

            "Performance Category",

            "Best Player",

            "Best Game Length",

            "Best Game Level",

            "Recommendation"
        ],


        "Value": [

            result["total_games"],

            result["best_score"],

            result["lowest_score"],

            round(
                result["average_score"],
                2
            ),

            round(
                result["median_score"],
                2
            ),

            result["score_difference"],

            round(
                result["average_length"],
                2
            ),

            round(
                result["average_level"],
                2
            ),

            round(
                result["score_std"],
                2
            ),

            round(
                result[
                    "performance_percentage"
                ],
                2
            ),

            result["category"],

            result["best_player"],

            result["best_game_length"],

            result["best_game_level"],

            result["recommendation"]
        ]
    })


    file_name = (
        "smart_snake_performance_report.csv"
    )


    report.to_csv(
        file_name,
        index=False
    )


    print(
        "\nPerformance report exported successfully!"
    )

    print(
        f"File: {file_name}"
    )


# ==========================================
# DISPLAY ANALYSIS
# ==========================================

def print_analysis():

    result = analyze_performance()


    if result is None:

        print(
            "\nNo game data available."
        )

        return


    print("\n")

    print(
        "=" * 60
    )

    print(
        "          SMART SNAKE"
    )

    print(
        "       PERFORMANCE REPORT"
    )

    print(
        "=" * 60
    )


    print(
        f"\nTotal Games          : "
        f"{result['total_games']}"
    )

    print(
        f"Best Score           : "
        f"{result['best_score']:.0f}"
    )

    print(
        f"Lowest Score         : "
        f"{result['lowest_score']:.0f}"
    )

    print(
        f"Average Score        : "
        f"{result['average_score']:.2f}"
    )

    print(
        f"Median Score         : "
        f"{result['median_score']:.2f}"
    )

    print(
        f"Score Difference     : "
        f"{result['score_difference']:.0f}"
    )

    print(
        f"Average Length       : "
        f"{result['average_length']:.2f}"
    )

    print(
        f"Average Level        : "
        f"{result['average_level']:.2f}"
    )

    print(
        f"Score Variation      : "
        f"{result['score_std']:.2f}"
    )

    print(
        f"Performance          : "
        f"{result['performance_percentage']:.2f}%"
    )

    print(
        f"Category             : "
        f"{result['category']}"
    )


    print(
        "\n" + "-" * 60
    )

    print(
        "BEST PLAYER"
    )

    print(
        "-" * 60
    )

    print(
        f"Player       : "
        f"{result['best_player']}"
    )

    print(
        f"Score        : "
        f"{result['best_score']:.0f}"
    )

    print(
        f"Snake Length : "
        f"{result['best_game_length']}"
    )

    print(
        f"Level        : "
        f"{result['best_game_level']}"
    )


    print(
        "\n" + "-" * 60
    )

    print(
        "SMART RECOMMENDATION"
    )

    print(
        "-" * 60
    )

    print(
        result["recommendation"]
    )

    print(
        "=" * 60
    )


# ==========================================
# MENU
# ==========================================

def analytics_menu():

    while True:

        print("\n")

        print(
            "=" * 50
        )

        print(
            "       SMART SNAKE ANALYTICS"
        )

        print(
            "=" * 50
        )

        print(
            "1. View Performance"
        )

        print(
            "2. Export Game History CSV"
        )

        print(
            "3. Export Performance Report"
        )

        print(
            "4. Exit"
        )

        print(
            "=" * 50
        )


        choice = input(
            "Enter your choice: "
        )


        if choice == "1":

            print_analysis()


        elif choice == "2":

            export_game_history()


        elif choice == "3":

            export_performance_report()


        elif choice == "4":

            print(
                "Exiting analytics..."
            )

            break


        else:

            print(
                "Invalid choice."
            )


# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":

    analytics_menu()