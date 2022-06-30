from bs4 import BeautifulSoup
import utils

import requests

def find_birthday(name):
    """
    Scrape information from the wiki to find the birthday of 
    the character with the given name. Error if the name does not 
    belong to a character on the wiki

    Parameters:
        name (str): name of the character we're searching for

    Returns:
        response (str): the birthday or error message
        code (int): the http response code
    """
    # construct search url
    url = f'{utils.SEARCH_URL}{name}'

    # get soup of the page
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")

    # error if we did not find an informational wiki page
    if not utils.was_result_found(soup):
        return f'{name} was not found on the wiki', 404

    # try and find birthday info in info box
    birthday_info = utils.find_infobox_section(soup, 'Birthday')

    # if we couldn't find birthday info in the infobox, return error message
    if not birthday_info:
        return f'Could not find info about the birthday of {name}', 404

    # return info about birthday
    return birthday_info.text.strip(), 200

def find_best_gifts(name):
    """
    Scrape information from the wiki to find the best gifts for 
    the character with the given name. Error if the name does not 
    belong to a character on the wiki

    Parameters:
        name (str): name of the character we're searching for

    Returns:
        response (str): the best gifts or error message
        code (int): the http response code
    """
    # construct search url
    url = f'{utils.SEARCH_URL}{name}'

    # get soup of the page
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")

    # error if we did not find an informational wiki page
    if not utils.was_result_found(soup):
        return f'{name} was not found on the wiki', 404

     # try and find best gifts info in info box
    best_gifts_info = utils.find_infobox_section(soup, 'Best Gifts')

    # if we couldn't find best gifts info in the infobox, return error message
    if not best_gifts_info:
        return f'Could not find info about the best gifts for {name}', 404

    # return human readable form of gift info
    return utils.section_to_readable(best_gifts_info), 200

def find_universal_loves():
    """
    Scrape information from the wiki about the universally loved
    gifts

    Returns:
        response (str): the list of universally loved gifts
        status (int): the http response code
    """
    # construct search url
    url = f'{utils.SEARCH_URL}List of All Gifts'

    # get soup of the page
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")

    # find the universal loves section on the page
    universal_loves_info = soup.findAll('tbody')[1].findAll('tr')[1].findAll('td')[2]

    # return human readable form of universal loves info
    return utils.section_to_readable(universal_loves_info), 200

def find_fish_info(fish):
    """
    Scrapes information from the wiki about the season, time, and
    location info of the given fish. Error if the fish does not 
    belong to a type of fish on the wiki

    Parameters:
        fish (str): the fish we're looking for information about

    Returns:
        response (dict or str): the fish information or an error code
        status (int): the http response code
    """
    # construct search url
    url = f'{utils.SEARCH_URL}{fish}'

    # get soup of the page
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")

    # error if we did not find an informational wiki page
    if not utils.was_result_found(soup):
        return f'{fish} was not found on the wiki', 404

    # try and find all the pertinent info
    season_info = utils.find_infobox_section(soup, 'Season')
    time_info = utils.find_infobox_section(soup, 'Time of Day')
    location_info = utils.find_infobox_section(soup, 'Found in')

    # error if not all the fish info was found
    if not (season_info and time_info and location_info):
        return f'Could not find all fishing information about {fish}', 404

    # convert each set of info into a readable format
    season_info = utils.replace_dots_with_commas(season_info.text)
    time_info = time_info.text.strip()
    location_info = utils.replace_dots_with_commas(location_info.text)

    # return dict with all fish info
    return {'seasons': season_info, 'time': time_info, 'locations': location_info}, 200

def find_crop_info(crop):
    """
    Scrapes information from the wiki about the season and growth
    info of the given crop. Error if the fish does not 
    belong to a type of fish on the wiki

    Parameters:
        crop (str): the fish we're looking for information about

    Returns:
        response (dict or str): the fish information or an error code
        status (int): the http response code
    """
    # construct search url
    url = f'{utils.SEARCH_URL}{crop}'

    # get soup of page
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")

    # error if we did not find an informational wiki page
    if not utils.was_result_found(soup):
        return f'{crop} was not found on the wiki', 404

    # find growth and seasons info if available (season info can be under two different names)
    growth_time_info = utils.find_infobox_section(soup, 'Growth Time')
    seasons_info = utils.find_infobox_section(soup, 'Season') or utils.find_infobox_section(soup, 'Harvest Season')

    # error if not all the crop info was found
    if not (growth_time_info and seasons_info):
        return f'Could not find all agriculture information about {crop}', 404

    # convert each set of info into a readable format
    growth_time_info = growth_time_info.text.strip()
    seasons_info = utils.replace_dots_with_commas(seasons_info.text)

    # return dict with all crop info
    return {'growth_time': growth_time_info, 'seasons': seasons_info}, 200

