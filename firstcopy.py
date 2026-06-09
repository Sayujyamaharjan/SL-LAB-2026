Questions = [
    "1. What is the capital of USA?",
    "2. Which is the largest continent?",
    "3. Which is the hotest planet in our solar system?",
    "4. Which is the largest ocean on Earth?",
    "5. Which is the longest river in the world?",
    "6. Which is the highest mountain in the world?",
    "7. Which is the largest desert in the world?",
    "8. Which is the largest country in the world?",
    "9. Which is the largest city in the world?",
    "10. Which is the largest island in the world?",
]
Option  = [
    ["Washington D.C.", "New York", "Los Angeles", "Chicago"],
    ["Asia", "Africa", "Europe", "North America"],
    ["Mercury", "Venus", "Earth", "Mars"],
    ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
    ["Nile River", "Amazon River", "Yangtze River", "Mississippi River"],
    ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
    ["Sahara Desert", "Gobi Desert", "Kalahari Desert", "Arabian Desert"],
    ["Russia", "Canada", "China", "United States"],
    ["Tokyo", "Delhi", "Shanghai", "Sao Paulo"],
    ["Greenland", "New Guinea", "Borneo", "Madagascar"],
]
right_ans = [4, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Prize = [5000, 5000, 5000, 5000, 5000, 25000, 50000, 100000, 100000, 200000]
Current = 0
for i in range(10):
    print(Questions[i])
    print(Option[i])
    choice = int(input("Enter your choice: "))
    if choice == right_ans[i]:
        Current = Current + Prize[i]
        print("Congratulations! You won Rs", Current)
    else:
        print("Wrong answer you lost the game")
        break
print("Your total prize is Rs", Current)
