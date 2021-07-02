import streamlit as st
from streamlit import config
from src.utils.state import SessionState

def write_page(page):  # pylint: disable=redefined-outer-name
    return page.write()
 
PAGES={ 'Home':home, 'About':intro, 'Stocks':dash}

def main():
    choice=st.sidebar.radio("Click on the pages to explore",tuple(PAGES.keys()))

    if choice ==None:
        write_page(dash) 
    else:
        page=PAGES[choice]
        with st.spinner(f"Loading {choice} ..."):
            write_page(page)


if __name__ == "__main__":
        main()
