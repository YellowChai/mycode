#!/usr/bin/env python3

def main():
    
    '''  importing date to get the today's date'''
    from datetime import date

    ''' Getting name input'''
    name = input('please, type your name: ')
    
    ''' Getting today's day of a week ''' 
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Saturday', 'Sunday']
    today = week[date.today().weekday()]

    ''' Print out ''' 
    print(f"Hello, {name}! Happy {today}!")


if __name__ == "__main__":
    
    main()
