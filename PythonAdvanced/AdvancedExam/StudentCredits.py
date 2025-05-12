def students_credits(*args):
    total_credits = 0
    credits_from_classes = {}
    final = []
    for s_class in range(len(args)):
        current_class = args[s_class].split("-")
        total_credits += int(current_class[3]) / (int(current_class[2]) / int(current_class[1]))
        class_credits = int(current_class[3]) / (int(current_class[2]) / int(current_class[1]))
        credits_from_classes[current_class[0]] = class_credits

    sorted_credits = sorted(credits_from_classes.items(), key=lambda x: -x[1])

    if total_credits >= 240:
        final.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        final.append(f"Diyan needs {(240 - total_credits):.1f} credits more for a diploma.")
    for tupal in range(len(sorted_credits)):
        final.append(f"{sorted_credits[tupal][0]} - {sorted_credits[tupal][1]:.1f}")
    return '\n'.join(final)


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)





# (f"{current_class[0]} - {class_credits:.1f}")
