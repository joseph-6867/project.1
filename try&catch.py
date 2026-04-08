import math
import random
import datetime

def calculate_square_root():
    try:
        
        num = int(input("Enter a number: "))
        result = math.sqrt(num)
        print("Square root:", result)
        rand_num = random.randint(1, 10)
        print("Random number between 1 and 10:", rand_num)
        current_time = datetime.datetime.now()
        print("Current date and time:", current_time)

    except ValueError:
        print("Error: Please enter a valid integer.")
    
    except ZeroDivisionError:
        print("Error: Division by zero occurred.")
    
    except Exception as e:
        print("Unexpected error:", e)
    
    finally:
        print("Execution completed (finally block always runs).")

calculate_square_root()
