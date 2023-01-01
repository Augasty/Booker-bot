from booking.booking import Booking


# inst = Booking()

# inst.land_first_page()
# inst.change_currency()

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='USD')
    bot.select_place_to_go('New York')

    bot.select_dates(check_in_date='2023-01-19', check_out_date='2023-01-25')
    bot.select_adults(3)
    bot.click_search()
    
    bot.apply_filtration()
    bot.refresh()  #refreshes the page to let the bot grab proper data
    bot.report_results()

# once python comes outside this indentation
# then it is going to perform some teardown
# actions, which actions are by convension 
# stored in __exit__() 