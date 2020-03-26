import os
'''

IMPORTANT NOTE: Do NOT change any of the function names or their signatures
(the parameters they take).
Your functions must behave exactly as described. Please check correctness by
running DocTests  included in function headers. You may not use any print or
input statements in your code.

Manage a calendar database.

A calendar is a dictionary keyed by date ("YYYY-MM-DD") with value being a list
of strings, the events on the specified date.

'''


# -----------------------------------------------------------------------------
# Please implement the following calendar commands
# -----------------------------------------------------------------------------

def command_help():
    """

    () -> str
    This function is already implemented. Please do not change it.
    Returns a help message for the system. That is...
    """

    help_me = """
    Help for Calendar. The calendar commands are

    add DATE START END DETAILS               add the event DETAILS at the specified DATE with specific START and END time
    show                                     show all events in the calendar
    delete DATE NUMBER             delete the specified event (by NUMBER) from
                                   the calendar
    quit                           quit this program
    help                           display this help message

    Examples: user data follows command:

    command: add 2018-10-12 18 19 dinner with jane
    success

    command: show
        2018-10-12 :
            start : 08:00,
			end : 09:00,
			title : Eye doctor

            start : 12:30,
			end : 13:00,
			title : lunch with sid

			start : 18:00,
			end : 19:00,
			title : dinner with jane
        2018-10-29 :
            start : 10:00,
			end : 11:00,
			title : Change oil in blue car

            start : 12:00,
			end : 14:00,
			title : Fix tree near front walkway

            start : 18:00,
			end : 19:00,
			title : Get salad stuff, leuttice, red peppers, green peppers
        2018-11-06 :
            start : 18:00,
			end : 22:00,
			title : Sid's birthday

    command: delete 2018-10-29 10
    deleted

    A DATE has the form YYYY-MM-DD, for example
    2018-12-21
    2016-01-02

    START and END has a format HH where HH is an hour in 24h format, for example
    09
    21

    Event DETAILS consist of alphabetic characters,
    no tabs or newlines allowed.
    """
    return help_me


def command_add(date, start_time, end_time, title, calendar):
    """
    (str, int, int, str, dict) -> boolean
    Add title to the list at calendar[date]
    Create date if it was not there
    Adds the date if start_time is less or equal to the end_time

    date: A string date formatted as "YYYY-MM-DD"
    start_time: An integer from 0-23 representing the start time
    end_time: An integer from 0-23 representing the start time
    title: A string describing the event
    calendar: The calendar database
    return: boolean of whether the even was successfully added

    >>> calendar = {}
    >>> command_add("2018-02-28", 11, 12, "Python class", calendar)
    True
    >>> calendar == {"2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 14, 16, "CSCA08 test 2", calendar)
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 10, 9, "go out with friends after test", calendar)
    False
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-13", 13, 13, "Have fun", calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], \
    "2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    """
    if not is_calendar_date(date):
        return False
    elif not is_natural_number(start_time):
        return False
    elif not is_natural_number(end_time):
        return False
    else:
        if parse_time(start_time) == False or  parse_time(end_time)==False:
            return False


        if int(start_time) > int(end_time):
            return False
        new= [{'start':start_time,'end':end_time,'title':title}]
        for key, value in calendar.items():
            if key == date:
                calendar[key]= new+value
                return True
        else:

            calendar[date] = new
            return True





    # YOUR CODE GOES HERE

    pass

def quit():

    return

def command_show(calendar):
    r"""
    (dict) -> str
    Returns the list of events for calendar sorted in decreasing date order
    and increasing time order within the date
    as a string, see examples below for a sample formatting
    calendar: the database of events

    Example:
    >>> calendar = {}
    >>> command_add("2018-01-15", 11, 13, "Eye doctor", calendar)
    True
    >>> command_add("2018-01-15", 8, 9, "lunch with sid", calendar)
    True
    >>> command_add("2018-02-10", 12, 23, "Change oil in blue car", calendar)
    True
    >>> command_add("2018-02-10", 20, 22, "dinner with Jane", calendar)
    True
    >>> command_add("2017-12-22", 5, 8, "Fix tree near front walkway", calendar)
    True
    >>> command_add("2017-12-22", 13, 15, "Get salad stuff", calendar)
    True
    >>> command_add("2018-05-06", 19, 23, "Sid's birthday", calendar)
    True
    >>> command_show(calendar)
    "\n2018-05-06 : \n    start : 19:00,\n    end : 23:00,\n    title : Sid's birthday\n2018-02-10 : \n    start : 12:00,\n    end : 23:00,\n    title : Change oil in blue car\n\n    start : 20:00,\n    end : 22:00,\n    title : dinner with Jane\n2018-01-15 : \n    start : 08:00,\n    end : 09:00,\n    title : lunch with sid\n\n    start : 11:00,\n    end : 13:00,\n    title : Eye doctor\n2017-12-22 : \n    start : 05:00,\n    end : 08:00,\n    title : Fix tree near front walkway\n\n    start : 13:00,\n    end : 15:00,\n    title : Get salad stuff"
    """

    cal =sorted(calendar,reverse=True)
    new_calendar={}
    for i in cal:
        new_calendar[i] = sorted(calendar[i], key = lambda k:str(k['start']))


    string_=''
    lnt= len(new_calendar.items())
    check1=1
    for date, detail in new_calendar.items():
        if check1 == 1:
            date='\n' +date +' : '
        elif check1 >1 :
             date='\n'+date +' : '
        string_ +=date
        check=1
        check3=len(detail)
        for i in detail:
            start = i['start']
            end= i['end']
            title= i['title']
            if check==1:
                string_ += '\n    start : ' +parse_time(start)  +',\n    end : ' +parse_time(end) +',\n    '+'title : '+title
                check+=1
                continue

            elif check >1 and check != check3:
                string_ += '\n\n    start : ' +parse_time(start)  +',\n    end : ' +parse_time(end) +',\n    '+'title : '+title+'\n'
                check+=1
                continue
            elif check ==  check3:
                string_ += '\n\n    start : ' +parse_time(start)  +',\n    end : ' +parse_time(end) +',\n    '+'title : '+title

            check+=1
        check1 +=1
    return string_

    pass
def parse_time(time_):
    time__= str(time_)
    if not 0 <int(time__) < 24:
        return False
    valid='1234567890'
    for i in time__:
        if i not in valid:
            return False
        elif i in valid:
            pass
    if len(time__) == 1:
        output= '0'+ time__+':'+'00'
        return output
    elif len(time__) ==2:
        output= str(time__)+':'+'00'
        return output
    else:
        return False
def parse_time2(time_):
    time__= str(time_)
    if not 0 <int(time__) < 24:
        return False
    valid='1234567890'
    for i in time__:
        if i not in valid:
            return False
        elif i in valid:
            pass

    if len(time__) == 1:
        output= '0'+ time__
        return output
    elif len(time__) ==2:
        output= str(time__)
        return output
    else:
        return False

def command_delete(date, start_time, calendar):
    """
    (str, int, dict) -> str
    Delete the entry at calendar[date][start_time]
    If calendar[date] is empty, remove this date from the calendar.
    If the entry does not exist, do nothing
    date: A string date formatted as "YYYY-MM-DD"
    start_time: An integer indicating the start of the event in calendar[date] to delete
    calendar: The calendar database
    return: a string indicating any errors, True for no errors

    Example:


    >>> calendar = {}
    >>> command_add("2018-02-28", 11, 12, "Python class", calendar)
    True
    >>> calendar == {"2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 14, 16, "CSCA08 test 2", calendar)
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-13", 13, 13, "Have fun", calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], "2018-03-11": \
    [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], "2018-02-28": [{"start": 11, "end": 12, \
    "title": "Python class"}]}
    True
    >>> command_delete("2015-01-01", 1, calendar)
    '2015-01-01 is not a date in the calendar'
    >>> command_delete("2018-03-11", 3, calendar)
    'There is no event with start time of 3 on date 2018-03-11 in the calendar'
    >>> command_delete("2018-02-28", 11, calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], "2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}]}
    True
    >>> command_delete("2018-03-11", 14, calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}]}
    True
    >>> command_delete("2018-03-13", 13, calendar)
    True
    >>> calendar == {}
    True

    """
    # date, start_time, calendar

    if not is_calendar_date(date):
        return False
    elif not is_natural_number(start_time):
        return False

    check =0
    if is_calendar_date(date) and is_natural_number(start_time):
        for _date, _events in calendar.items():
            if _date == date:
                index=0
                for i in _events:
                    if i['start'] == start_time:
                        if len(calendar[_date]) ==1:
                            calendar.pop(_date)
                        elif len(calendar[_date]) >1:
                            calendar[_date].pop(index)
                        check+=1
                        return True
                    index+=1
                return 'There is no event with start time of %s on date %s in the calendar'% (start_time,date)
        return '%s is not a date in the calendar'%date
        if check ==0:
            return False
    else:
        return 'Wrong date or start time format'
    # YOUR CODE GOES HERE
    pass


# -----------------------------------------------------------------------------
# Functions dealing with calendar persistence
# -----------------------------------------------------------------------------

"""
The calendar is read and written to disk.

...

date_i is "YYYY-MM-DD"'
description can not have tab or new line characters in them.

"""


def save_calendar(calendar):
    """
    (dict) -> bool
    Save calendar to 'calendar.txt', overwriting it if it already exists. The calendar events do not have
    to be saved in any particular order

    The format of calendar.txt is the following:

    date_1:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\n
    date_2:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\n
    date_n:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\n

    Example: The following calendar...



        2018-03-13 :
                start : 13:00,
                end : 13:00,
                title : Have fun
        2018-03-11 :
                start : 10:00,
                end : 12:00,
                title : Another event on this date

                start : 14:00,
                end : 16:00,
                title : CSCA08 test 2
        2018-02-28 :
                start : 11:00,
                end : 12:00,
                title : Python class

     appears in calendar.txt as ...

    2018-03-13:13-13 Have fun
    2018-03-11:10-12 Another event on this date    14-16 CSCA08 test 2
    2018-02-28:11-12 Python class

    calendar: dictionary containing a calendar
    return: True if the calendar was saved.
    """


    # YOUR CODE GOES HERE
    # cal =sorted(calendar,reverse=True)
    new_calendar=calendar
    # for i in cal:
    #     new_calendar[i] = sorted(calendar[i], key = lambda k:k['start'],reverse=True)


    dates=[]


    for date, detail in new_calendar.items():
        line=''
        line +=date +':'
        lnt= len(detail)
        check=1
        for i in detail:
            start = i['start']
            end= i['end']
            title= i['title']
            if check== lnt:
                line+=parse_time2(start) + "-"+ parse_time2(end) + ' '+title
            else:
                line+=parse_time2(start) + "-"+ parse_time2(end) + ' '+title + '\t'
            check+=1
        line+='\n'
        dates.append(line)


    with open('calendar.txt', 'w') as file:
        for date in dates:
            file.write(date)
    return True
    pass


def load_calendar():
    '''
    () -> dict
    Load calendar from 'calendar.txt'. If calendar.txt does not exist,
    create and return an empty calendar. For the format of calendar.txt
    see save_calendar() above.

    return: calendar.

    '''
    try:
        with open('calendar.txt', 'r') as file:
            lines= file.readlines()
            dicttion={}
        if len(lines) >0:

            for line in lines:
                line= line.rstrip()
                date, events=line.split(':')
                events= events.split('\t')
                events_=[]
                for event in events:
                    start, rest= event.split('-')
                    lists= rest.split(' ')
                    event={'start':int(start),'end':int(lists[0]),'title':' '.join(lists[1:])}
                    events_.append(event)
                dicttion[date]= events_
                del events_
            return dicttion
        else:
            return dicttion




    except FileNotFoundError:
        with open('calendar.txt', 'w+') as file:
            pass
        return {}


    # YOUR CODE GOES HERE
    pass

# -----------------------------------------------------------------------------
# Functions dealing with parsing commands
# -----------------------------------------------------------------------------


def is_command(command):
    '''
    (str) -> bool
    Return whether command is a valid command
    Valid commands are any of the options below
    "add", "delete", "quit", "help", "show"
    You are not allowed to use regular expressions in your implementation.
    command: string
    return: True if command is one of ["add", "delete", "quit", "help", "show"]
    false otherwise
    Example:
    >>> is_command("add")
    True
    >>> is_command(" add ")
    False
    >>> is_command("List")
    False

    '''

    valid =["add", "delete", "quit", "help", "show"]

    if command not in valid:
        return False
    elif command in valid:
        return True

    # YOUR CODE GOES HERE
    pass


def is_calendar_date(date):
    '''
    (str) -> bool
    Return whether date looks like a calendar date
    date: a string
    return: True, if date has the form "YYYY-MM-DD" and False otherwise
    You are not allowed to use regular expressions in your implementation.
    Also you are not allowed to use isdigit() or the datetime module functions.

    Example:

    >>> is_calendar_date("15-10-10") # invalid year
    False
    >>> is_calendar_date("2015-10-15")
    True
    >>> is_calendar_date("2015-5-10") # invalid month
    False
    >>> is_calendar_date("2015-15-10") # invalid month
    False
    >>> is_calendar_date("2015-05-10")
    True
    >>> is_calendar_date("2015-10-55") # invalid day
    False
    >>> is_calendar_date("2015-55") # invalid format
    False
    >>> is_calendar_date("jane-is-gg") # YYYY, MM, DD should all be digits
    False

    Note: This does not validate days of the month, or leap year dates.

    >>> is_calendar_date("2015-04-31") # True even though April has only 30 days.
    True

    '''
    # Algorithm: Check length, then pull pieces apart and check them. Use only
    # basic string
    # manipulation, comparisons, and type conversion. Please do not use any
    # powerful date functions
    # you may find in python libraries.
    # 2015-10-12
    # 0123456789
    valid='0123456789'
    date_split= date.split('-')
    if len(date_split) != 3:
        return False
        flags.append(False)
    year= date_split[0]
    month = date_split[1]
    day = date_split[2]
    for i in year:
        if i not in valid:
            return False

    for i in month:
        if i not in valid:
            return False

    for i in day:
        if i not in valid:
            return False

    if len(str(year)) != 4:
        return False

    if 0  < int(month) <=12 :
        pass
    else:
        return False
    if 0  < int(day) <= 31 :
        pass
    else:
        return False

    return True
    # YOUR CODE GOES HERE
    pass


def is_natural_number(input):
    '''
    (str) -> bool
    Return whether str is a string representation of a natural number,
    that is, 0,1,2,3,...,23,24,...1023, 1024, ...
    In CS, 0 is a natural number
    param str: string
    Do not use string functions
    return: True if num is a string consisting of only digits. False otherwise.
    Example:

    >>> is_natural_number("0")
    True
    >>> is_natural_number("05")
    True
    >>> is_natural_number("2015")
    True
    >>> is_natural_number("9 3")
    False
    >>> is_natural_number("sid")
    False
    >>> is_natural_number("2,192,134")
    False

    '''
    # Algorithm:
    # Check that the string has length > 0
    # Check that all characters are in ["0123456789"]
    flags=[]
    valid="0123456789"
    s_input=str(input)
    if len(s_input) >0:
        for each in s_input:
            if each not in valid:
                return False

        return True
    else:
        return False

    # YOUR CODE GOES HERE
    pass


def parse_command(line):
    '''
    (str) -> list
    Parse command and arguments from the line. Return a list
    [command, arg1, arg2, ...]
    Return ["error", ERROR_DETAILS] if the command is not valid.
    Return ["help"] otherwise.
    The valid commands are

    1) add DATE START_TIME END_TIME DETAILS
    2) show
    3) delete DATE START_TIME
    4) quit
    5) help

    line: a string command
    return: A list consiting of [command, arg1, arg2, ...].
    Return ["error", ERROR_DETAILS], if line can not be parsed.
    ERROR_DETAILS displays how to use the

    Example:
    >>> parse_command("add 2015-10-21 10 11 budget meeting")
    ['add', '2015-10-21', 10, 11, 'budget meeting']
    >>> parse_command("")
    ['help']
    >>> parse_command("not a command")
    ['help']
    >>> parse_command("help")
    ['help']
    >>> parse_command("add")
    ['error', 'add DATE START_TIME END_TIME DETAILS']
    >>> parse_command("add 2015-10-22")
    ['error', 'add DATE START_TIME END_TIME DETAILS']
    >>> parse_command("add 2015-10-22 7 7 Tims with Sally.")
    ['add', '2015-10-22', 7, 7, 'Tims with Sally.']
    >>> parse_command("add 2015-10-35 7 7 Tims with Sally.")
    ['error', 'not a valid calendar date']
    >>> parse_command("show")
    ['show']
    >>> parse_command("show calendar")
    ['error', 'show']
    >>> parse_command("delete")
    ['error', 'delete DATE START_TIME']
    >>> parse_command("delete 15-10-22")
    ['error', 'delete DATE START_TIME']
    >>> parse_command("delete 15-10-22 11")
    ['error', 'not a valid calendar date']
    >>> parse_command("delete 2015-10-22 3,14")
    ['error', 'not a valid event start time']
    >>> parse_command("delete 2015-10-22 14")
    ['delete', '2015-10-22', '14']
    >>> parse_command("quit")
    ['quit']

    '''
    valid =["add", "delete", "quit", "help", "show"]
    if len(line)>0:
        splits= line.split(' ')
        if splits[0] not in valid:
            return ['help']
    else:
        return ['help']
    splits= line.split(' ')
    if splits[0] == 'quit':
        if len(splits) ==1:
            return ['quit']
        elif len(splits) > 1:
            return ['error', 'quit']
    elif splits[0] =='show':
        if len(splits) ==1:
            return ['show']
        elif len(splits) > 1:
            return ['error', 'show']
    elif splits[0] =='help':
        if len(splits) ==1:
            return ['help']
        elif len(splits) > 1:
            return ['help']
    elif splits[0] =='delete':

        if len(splits) ==3:
            if not is_calendar_date(splits[1]):
                return ['error','not a valid calendar date']
            elif not is_natural_number(splits[2]):
                return ['error','not a valid start time']
            elif 0< int(splits[2]) <=24:
                
                return ['delete', splits[1], int(splits[2])]
            else:
                return ['error','not a valid start time']

        elif len(splits) !=3:
            return ['error', 'delete DATE START_TIME']
    elif splits[0] =='add':
        flag=0
        if len(splits) >=5:
            if not is_calendar_date(splits[1]):
                return ['error','not a valid calendar date']
            elif not is_natural_number(splits[2]):
                return ['error','not a valid start time']
            elif not is_natural_number(splits[3]):
                return ['error','not a valid end time']
            elif len(splits[4:]) <0:
                return ['error','not a valid title']
            elif 0< int(splits[2]) <=24 and 0< int(splits[3]) <=24:
                if int(splits[3]) > int(splits[2]):
                    return  ['add', splits[1],int(splits[2]), int(splits[3]), ' '.join(splits[4:])]
                else:
                    return ['error','End time has to be higher then start time']
            else:
                return ['error','not a valid start and end hour']

                return ['delete', splits[1], splits[2]]
        elif len(splits) <5:
            return ['error', 'add DATE START_TIME END_TIME DETAILS']



    # HINT: You can first split, then join back the parts of
    # the final argument.
    # YOUR CODE GOES HERE
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
