from Google import Create_Service, convert_to_RFC_datetime

CLIENT_SECRET_FILE = 'Client_Secret_File.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
answer = input("Would you like to add, delete, list, or manage events? ").lower()

# ADDING CALENDARS #
if answer == "add":
    name = input('What would you like to call your new calendar? ')
    request_body = {'summary': str(name)}
    response = service.calendars().insert(body=request_body).execute()
    print(response)
    print('Your calendar has been successfully added.')
# ADDING CALENDARS #


# DELETING CALENDARS #
if answer == 'delete':
    response = service.calendarList().list().execute()
    calendar_items = response['items']
    selected_calendar = input(str(calendar_items) + '\nPaste the ID of the Calendar to confirm: ')
    service.calendars().delete(calendarId=selected_calendar).execute()
    print('Your calendar has been successfully deleted.')
# DELETING CALENDARS #


# LISTING CALENDARS #
if answer == 'list':
    response = service.calendarList().list().execute()
    calendar_items = response['items']
    calendar_names = [i['summary'] for i in calendar_items if 'summary' in i]
    print("Your current calendars are: " + str(calendar_names))
# LISTING CALENDARS #


# EVENTS #
if answer == 'manage' or answer == 'events' or answer == 'manage events':
    response = service.calendarList().list().execute()
    calendar_items = response['items']
    selected_calendar = input(str(calendar_items) + '\nPaste the ID of the Calendar to manage events: ')
    event_answer = input('Would you like to add, delete, view, or edit events? ').lower()

    # CREATE EVENTS [ADD ADVANCED OPTIONS SOON] #
    if event_answer == 'add':
        start_year = int(input("Enter YYYY for the event's start year: "))
        start_month = int(input("Enter MM for the event's start month: "))
        start_day = int(input("Enter DD for the event's start day: "))
        start_hour = int(input("Enter HR for the event's start hour: "))
        start_minute = int(input("Enter HR for the event's start minute: "))
        # start_time = start_year, start_month, start_day, start_hour, start_minute
        end_year = int(input("Enter YYYY for the event's end year: "))
        end_month = int(input("Enter MM for the event's end month: "))
        end_day = int(input("Enter DD for the event's end day: "))
        end_hour = int(input("Enter HR for the event's end hour: "))
        end_minute = int(input("Enter HR for the event's end minute: "))
        # end_time = end_year, end_month, end_day, end_hour, end_minute
        event_request_body = {
            'start': {'dateTime': convert_to_RFC_datetime(start_year, start_month, start_day, start_hour, start_minute),
                      'timeZone': 'America/Los_Angeles'},
            'end': {'dateTime': convert_to_RFC_datetime(end_year, end_month, end_day, end_hour, end_minute),
                    'timeZone': 'America/Los_Angeles'},
            'summary': input('What would you like to call this event? '),
            'visibility': input('Should this event be public or private? ').lower()}
        response = service.events().insert(calendarId=selected_calendar, body=event_request_body).execute()
        print(response)
    # CREATE EVENTS [ADD ADVANCED OPTIONS SOON] #


    # DELETE EVENTS #
    if event_answer == 'delete':
        response = service.events().list(calendarId=selected_calendar).execute()
        event_items = response['items']
        selected_event = input(str(event_items) + '\n Paste the ID of the event to confirm: ')
        service.events().delete(calendarId=selected_calendar, eventId=selected_event).execute()
        print('Your event has successfully been deleted.')
    # DELETE EVENTS #


    # VIEW EVENTS #
    if event_answer == 'view':
        response = service.events().list(calendarId=selected_calendar).execute()
        event_items = response['items']
        event_names = [i['summary'] for i in event_items if 'summary' in i]
        print("Your current events for this calendar are: " + str(event_names))
    # VIEW EVENTS #

    # UPDATE EVENTS #
    if event_answer == 'edit':
        response = service.events().list(calendarId=selected_calendar).execute()
        event_items = response['items']
        selected_event = input(str(event_items) + '\n Paste the ID of the event to confirm: ')
        start_year = int(input("Enter YYYY for the event's new start year: "))
        start_month = int(input("Enter MM for the event's new start month: "))
        start_day = int(input("Enter DD for the event's new start day: "))
        start_hour = int(input("Enter HR for the event's new start hour: "))
        start_minute = int(input("Enter HR for the event's new start minute: "))
        # start_time = start_year, start_month, start_day, start_hour, start_minute
        end_year = int(input("Enter YYYY for the event's new end year: "))
        end_month = int(input("Enter MM for the event's new end month: "))
        end_day = int(input("Enter DD for the event's new end day: "))
        end_hour = int(input("Enter HR for the event's new end hour: "))
        end_minute = int(input("Enter HR for the event's new end minute: "))
        # end_time = end_year, end_month, end_day, end_hour, end_minute
        event_request_body = {
            'start': {'dateTime': convert_to_RFC_datetime(start_year, start_month, start_day, start_hour, start_minute),
                      'timeZone': 'America/Los_Angeles'},
            'end': {'dateTime': convert_to_RFC_datetime(end_year, end_month, end_day, end_hour, end_minute),
                    'timeZone': 'America/Los_Angeles'},
            'summary': input('What would you like to call this event? ').lower(),
            'visibility': input('Should this event be public or private? ').lower()}
        res_update = service.events().update(calendarId=selected_calendar, eventId=selected_event, body=event_request_body).execute()
        print(res_update)
        print('Your event has successfully been changed.')
    # UPDATE EVENTS #
# EVENTS #
