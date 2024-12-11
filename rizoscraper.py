import streamlit as st
import requests
from bs4 import BeautifulSoup
from datetime import date, datetime

def fetch_html(url):
    """Fetch the HTML content of the given URL."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.text

def parse_html(html):
    """Parse the HTML content and extract text from and below <div align="center" class="title*">, excluding <div class="footer hidden-xs">."""
    soup = BeautifulSoup(html, 'html.parser')
    content = []
    # Find the specific <div align="center" with class starting with "title"
    target_div = soup.find('div', align='center', class_=lambda x: x and x.startswith('title'))
    if target_div:
        # Extract the content of the target div
        title = target_div.get_text(separator='\n', strip=True)
        # Extract all content below the target div
        for sibling in target_div.find_next_siblings():
            if 'footer' in sibling.get('class', []) and 'hidden-xs' in sibling.get('class', []):
                break
            content.append(sibling.get_text(separator='\n', strip=True))
        article = '\n'.join(content)
    else:
        title = ""
        article = ""
    return title, article

def scrape_website(url):
    """Scrape text from the given website URL."""
    html = fetch_html(url)
    text = parse_html(html)
    return text

def main():
<<<<<<< HEAD
        # URLs list with the selected date
=======
    st.title('Rizoscraper')
    st.write("Welcome to our site! We leverage the power of Python to bring you the latest news articles from Rizospastis.gr. Our custom scraper, built with BeautifulSoup and requests, efficiently gathers specific articles from Rizospastis.gr. Using Streamlit, we present this curated content in a user-friendly and interactive format. Stay informed with our quick, daily, and streamlined news feed!")
    
    # Add a date picker
    selected_date = st.date_input(
        "Select a date",
        value=date.today(),
        min_value=datetime(2020, 1, 1),  # Set a reasonable minimum date
        max_value=date.today()  # Prevent future dates
    )
    
    # Convert selected date to the required format
    formatted_date = selected_date.strftime("%d/%m/%Y")
    
    st.text("")
    
    # URLs list with the selected date
>>>>>>> origin/main
    urls = [
        (f"https://www.rizospastis.gr/columnPage.do?publDate={formatted_date}&columnId=161", "Από μέρα σε μέρα"),
        (f"https://www.rizospastis.gr/columnStory.do?publDate={formatted_date}&columnId=7389", "Σαν Σήμερα"),
        (f"https://www.rizospastis.gr/columnStory.do?publDate={formatted_date}&columnId=7401", "Η 'Αποψη μας"),
        (f"https://www.rizospastis.gr/columnStory.do?publDate={formatted_date}&columnId=7124", "Αποκαλυπτικά"),
        (f"https://www.rizospastis.gr/columnPage.do?publDate={formatted_date}&columnId=662", "Επιστήμη"),
        (f"https://www.rizospastis.gr/columnPage.do?publDate={formatted_date}&columnId=9046", "Επιστήμη"),
        (f"https://www.rizospastis.gr/columnPage.do?publDate={formatted_date}&columnId=8968", "Πολιτισμός"),
        (f"https://www.rizospastis.gr/columnStory.do?publDate={formatted_date}&columnId=8609", "Κινηματογράφος"),
        (f"https://www.rizospastis.gr/columnPage.do?publDate={formatted_date}&columnId=8966","Βιβλίο"),
        (f"https://www.rizospastis.gr/columnPage.do?publDate={formatted_date}&columnId=8403","Πόλεμος"),
        (f"https://www.rizospastis.gr/columnStory.do?publDate={formatted_date}&columnId=9924", "Σφήνες"),
        (f"https://www.rizospastis.gr/columnStory.do?publDate={formatted_date}&columnId=521", "Πατριδογνωμόνιο"),
        (f"https://www.rizospastis.gr/columnStory.do?publDate={formatted_date}&columnId=9244", "Δαχτυλικά Αποτυπώματα"),
        (f"https://www.rizospastis.gr/columnPage.do?publDate={formatted_date}&columnId=9502", "Παιδί και Οικογένεια")


    st.title('Rizoscraper')
    st.write("Welcome to our site! We leverage the power of Python to bring you the latest news articles from Rizospastis.gr. Our custom scraper, built with BeautifulSoup and requests, efficiently gathers specific articles from Rizospastis.gr. Using Streamlit, we present this curated content in a user-friendly and interactive format. Stay informed with our quick, daily, and streamlined news feed!")
    st.text("")
    
    # Add a date picker
    selected_date = st.date_input(
        "Select a date",
        value=date.today(),
        min_value=datetime(2020, 1, 1),  # Set a reasonable minimum date
        max_value=date.today()  # Prevent future dates
    )        
   
    for url in urls:
        try:
            title, article = scrape_website(url[0])
            if article:
                with st.expander(url[1]):
                    st.write(title)
                    st.markdown(f'<div style="text-align: justify;">{article}</div>', unsafe_allow_html=True)
                    st.text("")
                    st.markdown(f'<p style="text-align: right;">Διάβασε το άρθρο στον <a href="{url[0]}">Ριζοσπάστη</a></p>', unsafe_allow_html=True)
        except Exception as e:
            st.warning(f"Could not fetch article from {url[0]}: {str(e)}")

if __name__ == "__main__":
    main()
