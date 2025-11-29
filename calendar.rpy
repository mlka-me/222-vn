init python:
    def time_callback():
        if (hasattr(store, 'theweekday')):
            if store.theweekday > 7:
                store.theweekday = store.theweekday - 7
            if store.theweekday == 1:
                store.stringweekday = "Monday"
            elif store.theweekday == 2:
                store.stringweekday = "Tuesday"
            elif store.theweekday == 3:
                store.stringweekday = "Wednesday"
            elif store.theweekday == 4:
                store.stringweekday = "Thursday"
            elif store.theweekday == 5:
                store.stringweekday = "Friday"
            elif store.theweekday == 6:
                store.stringweekday = "Saturday"
            elif store.theweekday == 7:
                store.stringweekday = "Sunday"
            else:
                store.stringweekday = "Error"

        if (hasattr(store, 'theday')):
            if store.theday > store.daylim:
                store.theday = store.theday - store.daylim

        if (hasattr(store, 'themonth')):
            if store.themonth == 1:
                store.stringmonth = "January"
                store.daylim = 31
            if store.themonth == 2:
                store.stringmonth = "{a=https://www.youtube.com/watch?v=50QO2BAlAzM}Oh no, February!{/a}"
                #Congratulations! You've been rickrolled! XD
                if ((((int(store.theyear) / 4)*4) - store.theyear) == 0):
                    store.daylim = 29
                else:
                    store.daylim = 28
            if store.themonth == 3:
                store.stringmonth = "March"
                store.daylim = 31
            if store.themonth == 4:
                store.stringmonth = "April"
                store.daylim = 30
            if store.themonth == 5:
                store.stringmonth = "May"
                store.daylim = 31
            if store.themonth == 6:
                store.stringmonth = "June"
                store.daylim = 30
            if store.themonth == 7:
                store.stringmonth = "July"
                store.daylim = 31
            if store.themonth == 8:
                store.stringmonth = "August"
                store.daylim = 31
            if store.themonth == 9:
               store.stringmonth = "September"
               store.daylim = 30
            if store.themonth == 10:
               store.stringmonth = "October"
               store.daylim = 31
            if store.themonth == 11:
               store.stringmonth = "Kaevember"
               #Kaeya Month ^-^
               store.daylim = 30
            if store.themonth == 12:
               store.stringmonth = "December"
               store.daylim = 31

            if (hasattr(store, 'dayofyear') and hasattr(store, 'yearlim')):
               if store.dayofyear > store.yearlim:
                   store.dayofyear = store.dayofyear - store.yearlim
                   store.theyear = store.theyear + 1
               if ((((int(store.theyear) / 4)*4) - store.theyear) == 0):
                   store.yearlim = 366
               else:
                   store.yearlim = 365
    config.python_callbacks.append(time_callback)

    def Calendar():
        ui.frame(xfill=False, xminimum = 400, yminimum=None, xalign=1.0, yalign = 0.805)
        ui.vbox()
        ui.text("(%s) - %s %d %d" % (stringweekday, stringmonth, theday, theyear), xalign=1.0, size=20)
        ui.close()
