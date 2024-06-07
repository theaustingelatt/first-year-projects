from urllib.request import urlopen
from tkinter import *
from re import *
from webbrowser import open as urldisplay
from sqlite3 import *
from urllib.request import urlopen, Request

# Create the main window
main_window = Tk()

# Font Constants
font_title = ("times", 30, "normal")

# Title the project
main_window.title('The Ministry of Truth')

main_window.configure(bg = 'light blue')

# Create a connection to SQLite DB
connection = connect(database = 'reliability_ratings.db')
reliability_ratings_db = connection.cursor()

# -------------FORBES HTML DATA--------------------

# Extract and decode the FORBES HTML source code
url = "https://www.forbes.com/digital-assets/news/"
response = urlopen(url)
forbes_html_content = response.read().decode('utf-8')


# Save the downloaded content to a file
with open("forbes.txt", 'w', encoding='utf-8') as file:
    file.write(forbes_html_content)


# Find FORBES latest headline story
forbes_headline_pattern = r'<a\s+[^>]*href="[^"]*"\s+class="UZhxnK9k"\s+data-testid="card-article-title"><h3\s+class="u00AMdzw"><span\s+[^>]*class="ULACyEdG">([^<]*)</span></h3></a>'   
forbes_headline_match = search(forbes_headline_pattern, forbes_html_content)


# Find FORBES date-time of latest headline story
forbes_datetime_pattern = r'<div\s+class="_2zDOJm9X">(\d+\s+hours?\s+ago)</div>'
forbes_datetime_match = search(forbes_datetime_pattern, forbes_html_content)


# Find FORBES website link of latest headline story
forbes_website_pattern = r'<a\s+[^>]*href="(https://www\.forbes\.com/sites/[^/"]+/\d{4}/\d{2}/\d{2}/[^/"]+/)"[^>]*>'
forbes_website_match = search(forbes_website_pattern, forbes_html_content)


# Tries to save the FORBES headline/time/website that is extracted from the regex
# If the pattern is not found for any reason they are set to None in order to avoid errors in displaying further information
# Subsequent functions handle the TypeError this causes in later steps

try:
    forbes_extracted_headline = forbes_headline_match.group(1)
except AttributeError:
    forbes_extracted_headline = None

try:
    forbes_published_time = forbes_datetime_match.group(1)
except AttributeError:
    forbes_published_time = None

try:
    forbes_extracted_website = forbes_website_match.group(1)
except AttributeError:
    forbes_extracted_website = None

#---------------ARS TECHNICA HTML DATA------------------------
    
# Extract, decode and save the ARS TECHNICA HTML source code
url = "https://arstechnica.com/"
response = urlopen(url)
ars_technica_html_content = response.read().decode('utf-8')


# Save the downloaded content to a file
with open("ars_technica.txt", 'w', encoding='utf-8') as file:
    file.write(ars_technica_html_content)


# Find ARS TECHNICA latest headline story
ars_technica_headline_pattern = r'<h2><a href=".*?">(.*?)</a></h2>'
ars_technica_headline_match = search(ars_technica_headline_pattern, ars_technica_html_content)


# Find ARS TECHNICA excerpt from latest headline story
ars_technica_excerpt_pattern = r'<p class="excerpt">(.*?)</p>'
ars_technica_excerpt_match = search(ars_technica_excerpt_pattern, ars_technica_html_content)


# Find ARS TECHNICA date-time of latest headline story
ars_technica_datetime_pattern = r'<time class="date".*?>(.*?)</time>'
ars_technica_datetime_match = search(ars_technica_datetime_pattern, ars_technica_html_content)


# Find ARS TECHNICA website link of latest headline story
ars_technica_website_pattern = r'<a class="overlay" href="([^"]+)"'
ars_technica_website_match = search(ars_technica_website_pattern, ars_technica_html_content)


# Tries to save the ARS TECHNICA headline/time/website that is extracted from the regex
# If the pattern is not found for any reason they are set to None in order to avoid errors in displaying further information
# Subsequent functions handle the TypeError this causes in later steps
try:
    ars_technica_extracted_headline = ars_technica_headline_match.group(1)
except AttributeError:
    ars_technica_extracted_headline = None

try:
    ars_technica_extracted_excerpt = ars_technica_excerpt_match.group(1)
except AttributeError:
    ars_technica_extracted_excerpt = None

try:
    ars_technica_published_time = ars_technica_datetime_match.group(1)
except AttributeError:
    ars_technica_published_time = None

try:
    ars_technica_extracted_website = ars_technica_website_match.group(1)
except AttributeError:
    ars_technica_extracted_website = None


#---------------ATLANTIC HTML DATA------------------------
    
# Extract, decode and save the ATLANTIC HTML source code

url = "https://www.theatlantic.com/latest/"
response = urlopen(url)
atlantic_html_content = response.read().decode('utf-8')


# Save the downloaded content to a file
with open("atlantic_news.txt", 'w', encoding='utf-8') as file:
    file.write(atlantic_html_content)


# Find ATLANTIC latest headline story
atlantic_headline_pattern = r'<h2\s+class="LandingRiver_title__wdvvu"[^>]*><span>([^<]+)</span></h2>'
atlantic_headline_match = search(atlantic_headline_pattern, atlantic_html_content)


## Find ATLANTIC excerpt from latest headline story
atlantic_excerpt_pattern = r'<p\s+class="LandingRiver_dek__OyPEv">([^<]+)</p>'
atlantic_excerpt_match = search(atlantic_excerpt_pattern, atlantic_html_content)


# Find ATLANTIC date-time of latest headline story
atlantic_datetime_pattern = r'<time\s+class="LandingMetadata_datePublished__iRPUc"\s+dateTime="[^"]+">([^<]+)</time>'
atlantic_datetime_match = search(atlantic_datetime_pattern, atlantic_html_content)


# Find ATLANTIC website link of latest headline story
atlantic_website_pattern = r'<a\s+href="(https://www\.theatlantic\.com/[^"]+)"\s+class="LandingRiver\_titleLink\_\_nUImQ"[^>]*>'
atlantic_website_match = search(atlantic_website_pattern, atlantic_html_content)


# Tries to save the ATLANTIC headline/time/website that is extracted from the regex
# If the pattern is not found for any reason they are set to None in order to avoid errors in displaying further information
# Subsequent functions handle the TypeError this causes in later steps

try:
    atlantic_extracted_headline = atlantic_headline_match.group(1)
except AttributeError:
    atlantic_extracted_headline = None

try:
    atlantic_extracted_excerpt = atlantic_excerpt_match.group(1)
except AttributeError:
    atlantic_extracted_excerpt = None

try:
    atlantic_published_time = atlantic_datetime_match.group(1)
except AttributeError:
    atlantic_published_time = None

try:
    atlantic_extracted_website = atlantic_website_match.group(1)
except AttributeError:
    atlantic_extracted_website = None
    

#----------NEWS AGENCIES------------------------

# Limits user selection to 1 news agency

def update_agency_selection():
    #Returns the user selected news agency
    news_source = selected_agency.get()
    #Provides communication to user about next steps once they make their news source selection
    if news_source == "Forbes":
        article_information.config(text = 'Please make a selection for Forbes')
        
    elif news_source == "Ars Technica":
        article_information.config(text = 'Please make a selection for Ars Technica News')
        
    elif news_source == "The Atlantic":
        article_information.config(text = 'Please make a selection for Atlantic')
        
# END OF UPDATE_AGENCY_SELECTION




# Opens up the webpage url in a seperate client based on user inputted news source
def full_details():
    #Returns the user selected news agency
        news_source = selected_agency.get()
    #Informs the user the article is opened in a seperate client incase they are unaware
        article_information.config(text = 'The full details for this article have been opened in a seperate window')

# Opens the website url that is extracted from HTML source code
# Try-except block handles any TypeErrors that occur if REGEX pattern renders extraction NONE
        if news_source == 'Forbes':
            try:
                urldisplay(forbes_extracted_website)
            except TypeError:
                article_information.config(text = 'This article from Forbes is unavailable right now.\n\nPlease try again later.')
        elif news_source == 'Ars Technica':
            try:
                urldisplay(ars_technica_extracted_website)
            except TypeError:
                article_information.config(text = 'This article from Ars Technica is unavailable right now.\n\nPlease try again later.')
        elif news_source == 'The Atlantic':
            try:
                urldisplay(atlantic_extracted_website)
            except TypeError:
                article_information.config(text = 'This article from The Atlantic is unavailable right now.\n\nPlease try again later.')
            
# END OF FULL_DETAILS FUNCTION


# Displays latest headline information if REGEX detects pattern
def latest_details():
    #Returns the user selected news agency
        news_source = selected_agency.get()
    #Displays unavailability message if REGEX patterns renders extraction NONE
        if news_source == 'Forbes':
            if forbes_extracted_headline == None:
                    article_information.config(text = f'Latest news from {news_source} is unavailable at this time.\n\nPlease try again later.')
            else:
                    article_information.config(text = f'Headline: {forbes_extracted_headline}\n\n({forbes_published_time})')
        elif news_source == 'Ars Technica':
            if ars_technica_extracted_headline == None:
                    article_information.config(text = f'Latest news from {news_source} is unavailable at this time.\n\nPlease try again later.')
            else:
                    article_information.config(text = f'Headline: {ars_technica_extracted_headline}\n\nExcerpt: {ars_technica_extracted_excerpt}\n\n({ars_technica_published_time})')
        elif news_source == 'The Atlantic':
            if atlantic_extracted_headline == None:
                    article_information.config(text = f'Latest news from {news_source} is unavailable at this time.\n\nPlease try again later.')
            else:
                    article_information.config(text = f'Headline: {atlantic_extracted_headline}\n\nExcerpt: {atlantic_extracted_excerpt}\n\n({atlantic_published_time})')
            
# END OF LATEST DETAILS FUNCTION


# Inputs the 'truth rating' of a user designated headline and saves it to reliability_ratings.db
def save_truth_rating():
        get_truth_rating = truth_scale.get()
        news_source = selected_agency.get()
    
# Saves the truth rating of selected news agency headline
# Returns error message if REGEX pattern renders extraction NONE
        try:
            if news_source == "Forbes":
                        headline = forbes_headline_match.group(1)
                        time = forbes_datetime_match.group(1)
                        insert_query = f"INSERT INTO ratings('news_source', headline, dateline, rating) VALUES ('{news_source}', '{headline}', '{time}', '{get_truth_rating}')"
                        reliability_ratings_db.execute(insert_query)
                        connection.commit()
                        article_information.config(text=f'Your truth rating of {get_truth_rating} has been updated for this {news_source} article.')
                        truth_scale.set(0)
            elif news_source == "Ars Technica":
                        headline = ars_technica_headline_match.group(1)
                        time = ars_technica_datetime_match.group(1)
                        insert_query = f"INSERT INTO ratings('news_source', headline, dateline, rating) VALUES ('{news_source}', '{headline}', '{time}', '{get_truth_rating}')"
                        reliability_ratings_db.execute(insert_query)
                        connection.commit()
                        article_information.config(text=f'Your truth rating of {get_truth_rating} has been updated for this {news_source} article.')
                        truth_scale.set(0)
            elif news_source == "The Atlantic":
                        headline = atlantic_headline_match.group(1)
                        time = atlantic_datetime_match.group(1)
                        insert_query = f"INSERT INTO ratings('news_source', headline, dateline, rating) VALUES ('{news_source}', '{headline}', '{time}', '{get_truth_rating}')"
                        reliability_ratings_db.execute(insert_query)
                        connection.commit()
                        article_information.config(text=f'Your truth rating of {get_truth_rating} has been updated for this {news_source} article.')
                        truth_scale.set(0)
        except (AttributeError, TypeError, UnboundLocalError):
            article_information.config(text=f'Your truth rating cannot be saved for this {news_source} article.\n\nPlease try again later.')
        
# END OF SAVE_TRUTH_RATING FUNCTION



#-----------NEWS AGENCY WIDGETS-----------------

# Radiobuttons were being initialized pre-selected. This variable and function clears it to start
# Empty string to hold the selected news egency
selected_agency = StringVar(value="")

# Clear the pre-selected Radiobutton selection
def clear_radio_selection():
    selected_agency.set(None)

# END OF CLEAR_RADIO_SELECTION FUNCTION

# Call the function that clears the pre-selected Radiobutton after 100 milliseconds so that the page can fully load and then clear
main_window.after(100, clear_radio_selection)
    

# Create a label frame for displaying news agencies
display_agencies = LabelFrame(main_window,
                              text = 'Choose a news agency',
                              fg = 'black',
                              bg = 'light blue',
                              width = 20,
                              font = font_title,
                              relief = 'groove',
                              pady = 30,
                              padx = 30)

# Create buttons to choose news agency
news_button_1 = Radiobutton(display_agencies,
                            text = 'Forbes',
                            variable = selected_agency,
                            value = "Forbes",
                            font = 10,
                            bg = 'light blue',
                            command = update_agency_selection)

news_button_2 = Radiobutton(display_agencies,
                            text = 'Ars Technica',
                            variable = selected_agency,
                            value = "Ars Technica",
                            font = 10,
                            bg = 'light blue',
                            command = update_agency_selection)

news_button_3 = Radiobutton(display_agencies,
                            text = 'The Atlantic',
                            variable = selected_agency,
                            value = "The Atlantic",
                            font = 10,
                            bg = 'light blue',
                            command = update_agency_selection)

show_latest = Button(display_agencies,
                     text = 'Show latest',
                     font = 10,
                     bg = 'white',
                     command = latest_details)

show_full_details = Button(display_agencies,
                           text = 'Show full details',
                           font = 10,
                           bg = 'white',
                           command = full_details)




#----------ARTICLE INFORMATION WIDGETS------------------
        
# Create a label frame for displaying article information
display_article = LabelFrame(main_window,
                        text = 'Article Information',
                        fg = 'black',
                        bg = 'light blue',
                        font = font_title,
                        relief = 'groove',
                        pady = 40,
                        padx = 40)

# Create a text window for displaying article information
article_information = Label(display_article,
                            text = 'Article information appears here...',
                            fg = 'black',
                            bg = 'light blue',
                            font = 10,
                            wraplength = 400,
                            anchor = 'w')


#----------TRUTH SCALE WIDGETS--------------------------

# Create a label frame for truthfulness rating
display_truth_rating = LabelFrame(main_window,
                                  text = 'Truthfulness Rating: 1-10',
                                  fg = 'black',
                                  bg = 'light blue',
                                  font = font_title,
                                  relief = 'groove')

truth_scale = Scale(display_truth_rating,
                    from_=0, to=10,
                    orient = HORIZONTAL,
                    fg = 'black',
                    bg = 'white',
                    font = 10,
                    length = 300)

truth_save = Button(display_truth_rating,
                    text = 'Save',
                    fg = 'black',
                    bg = 'white',
                    font = 10,
                    command = save_truth_rating)

#---------HOMEPAGE IMAGE + WEBSITE DESCRIPTION----------------------

# Create a description of the Website
website_title = Label (main_window,
                       text = 'The Ministry of "Truth"',
                       fg = 'black',
                       bg = 'light blue',
                       font =("Roboto", 30, "bold"))

# Create a label to indicate the creator of the website

# Load image for mainpage
the_don_photo = PhotoImage(file="Borowitz-Trump.gif")

# Using subsample method to reduce the Don photo
the_don_width = 400   # Specify the desired width
the_don_height = 300  # Specify the desired height
subsample_x = the_don_photo.width() // the_don_width
subsample_y = the_don_photo.height() // the_don_height

# Reduce the image by returning the largest subsample as a factor
subsample_reduce = max(subsample_x, subsample_y)

# Resize the image using subsample()
resized_photo = the_don_photo.subsample(subsample_reduce)

# Create a label and assign the resized photo image to it
the_don = Label(main_window, image=resized_photo)

# Label for photo credit
description_label = Label(main_window,
                          text="Photograph by James Devaney / Getty",
                          bg = 'light blue')

#----------ARTICLE INFORMATION GEOMETRY-------

# Position of article details label frame
display_article.grid(padx = 5,
                     pady = 10,
                     row = 2,
                     column = 0)

# Place information in the article information label frame
article_information.grid(row = 2,
                         column = 0)

#---------NEWS AGENCY GEOMETRY----------------

# Position of news agency label
display_agencies.grid(padx = 20,
                      pady = 10,
                      row = 1,
                      column = 0)

# Place options in the news agency label frame
news_button_1.grid(row = 1,
                   column = 0,
                   pady = 10,
                   padx = 20)

news_button_2.grid(row = 1,
                   column = 1,
                   pady = 10,
                   padx = 20)

news_button_3.grid(row = 1,
                   column = 2,
                   pady = 10,
                   padx = 20)

show_full_details.grid(row = 2,
                       column = 0,
                       columnspan = 2)

show_latest.grid(row = 2,
                 column = 1,
                 columnspan = 2)


#---------TRUTH SCALE GEOMETRY------------------
display_truth_rating.grid(padx = 20,
                          pady = 10,
                          row = 3,
                          column = 0)

truth_save.grid (row = 2,
                 column = 0)

truth_scale.grid (row = 1,
                  column = 0)

display_truth_rating.grid_columnconfigure(0, weight=1)
display_truth_rating.grid_rowconfigure(0, weight=1)

#---------HOMEPAGE IMAGE GEOMETRY---------------
the_don.grid(row = 2,
             column = 3,
             padx = 60)

website_title.grid(row = 1,
                   column = 3,
                   sticky = 's')

description_label.grid(row=3,
                       column=3,
                       padx=60,
                       sticky = 'nw')



# Start the event loop to detect user inputs
main_window.mainloop()


