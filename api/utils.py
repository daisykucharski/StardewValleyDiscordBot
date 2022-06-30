# URL used for searching the stardew valley wiki
SEARCH_URL = 'https://stardewvalleywiki.com/mediawiki/index.php?action=opensearch&search='

def was_result_found(soup):
    """
    Determines whether this page is a valid informational wiki page.
    Makes no guarantee that the contents of the page is as expected 
    (i.e. if looking for information about a character, that this page
    has information about a character)

    Parameters:
        soup (BeautifulSoup): the soup of the page requested

    Returns:
        success (boolean): whether the wiki page is valid
    """
    # if we landed on a search page, it is not an information page
    return soup.find(id="firstHeading").text != "Search results"

def find_infobox_section(soup, name):
    """
    Find the details of the section with the given name 
    in the infobox of this page, if it exists.

    Parameters:
        soup (BeautifulSoup): the soup of the page requested
        name (str): the name of the section in the infobox we're
        searching for 

    Returns:
        details (BeautifulSoup): the details of the infobox section named,
        or None if the section does not exist

    """
    # look for infobox
    infobox = soup.find(id="infoboxtable")

    # confirm infobox exists
    if not infobox:
        return None

    table_rows = infobox.findAll('tr')

    # iterate through all rows of the infobox table that contain information
    for row in table_rows[3:]:
        # find title for this row's section
        section = row.find(id='infoboxsection')

        # if we found the info we're looking for, return the details
        if section and section.text.strip() == f'{name}:':
            return row.find(id='infoboxdetail')

    # did not find section with given name
    return None


def section_to_readable(info):
    """
    Convert soup of a section containing information in hyperlinks
    into a readable string

    Parameters:
        info (BeautifulSoup): section of information we're looking to convert

    Returns:
        readable (str): information in section in readable format
    """
    
    return ', '.join(map(lambda item: item.text.strip(), info.findAll('a')))

def replace_dots_with_commas(old_str):
    """
    Replace • seperator with commas and clean up string

    Parameters:
        old_str (str): string seperated by •
    
    Returns:
        new_str (str): clean string seperated by commas

    """

    words = old_str.split('•')
    return ', '.join(map(lambda word: word.strip(), words))
