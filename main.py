def ankara_taxi_fare():
  distance = float(input("Enter the number of kilometers: "))
  meters = distance * 1000
  fare = 4.60 + ((meters / 100) * 0.34)

  return fare 

def print_fare(fare):
  print(f"Fare is {fare:.2f} ₺")

def main():
  fare = ankara_taxi_fare()
  print_fare(fare)

main()