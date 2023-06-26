import time

def brackets(response_text):
    start_index = response_text.find('{')  # Find the index of the first opening bracket
    end_index = response_text.rfind('}')  # Find the index of the last closing bracket
    if start_index == -1 or end_index == -1:
        response_text = "error"  # Return None if either bracket is not found
    else:
        response_text = response_text[start_index:end_index + 1]
    return response_text

def format_time(curr_time):
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", curr_time)
    return formatted_time

def get_timeofday(curr_time):
    return curr_time.tm_hour*100 + curr_time.tm_min

def increase_time(curr_time, seconds):
    new_time = time.mktime(curr_time) + seconds
    return time.localtime(new_time)

def set_start_time(year, month, day, hour, minute, second):
    start_time = time.struct_time((year, month, day, hour, minute, second, 1, 1, 0))
    return start_time

def time_prompt(curr_time):
    formatted_time = "It is " + time.strftime("%B %d, %Y, %I:%M %p.", curr_time)
    return formatted_time