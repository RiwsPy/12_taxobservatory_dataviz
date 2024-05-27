from taipy.gui import Markdown, navigate


def to_text(val):
    return "{:,}".format(int(val)).replace(",", " ")


# Path to images
data4good_logo_path = "./images/data4good-logo.svg"
eutax_logo_path = "./images/eutax-logo.svg"
taxplorer_logo_path = "./images/taxplorer-logo.svg"


# Initialise navbar items
navbar_items = [
    ("/Home", "Home"),
    ("/KeyStories", "KeyStories"),
    ("/Company", "Company"),
    ("/Methodology", "Methodology"),
    ("/Contact", "Contact"),
    ("/Download", "&#11123;")
]

def goto_d4g_website(state):
    navigate(state, "https://dataforgood.fr/", tab="_blank")


# Generate page from Markdown file
root = Markdown("pages/root.md")
