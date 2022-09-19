#!/usr/bin/env python3

def main():

    from datetime import date

    name = input('please, type your name: ')

    week = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Saturday', 'Sunday']
    today = week[date.today().weekday()]


    print(f"Hello, {name}! Happy {today}!")


if __name__ == "__main__":

    main()
