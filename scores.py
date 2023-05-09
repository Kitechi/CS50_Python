scores = []

for i in range(3):
    try:
        score = int(input("Score:"))
        scores.append(score)
    except ValueError:
        print("Not an integer")
        
average = sum(scores) / len(scores)
print(f"Average: {average}")