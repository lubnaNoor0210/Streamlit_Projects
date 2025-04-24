def main():
    print("This shows how many seconds are there in a year⏳")

days_in_year: int = 365
hours_per_day : int = 24
min_per_hour: int = 60
second_per_minute: int = 60

second_in_year = days_in_year * hours_per_day * min_per_hour * second_per_minute
print(f" There are {second_in_year} in one year")

if __name__ == '__main__':
    main()