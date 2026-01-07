import math 

def calculate_distance(x1, y1, x2, y2):
    # Calculate the distance using the distance formula
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def main():
    # Take user input for the coordinates
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    
    # Calculate the distance and print the result formatted to two decimal places
    distance = calculate_distance(x1, y1, x2, y2)
    print(f"{distance:.2f}")

if __name__ == "__main__":
    main()

