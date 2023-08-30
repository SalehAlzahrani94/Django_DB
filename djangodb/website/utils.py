def avrage_rating(reating_list):
    if not reating_list:
        return 0
    return round(sum(reating_list)/len(reating_list))