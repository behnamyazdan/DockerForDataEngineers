import json
import time
import redis
import random
from datetime import datetime

# Dictionary of page titles and URLs
page_data = {
    "Homepage": "/",
    "Product_Listings": "/pages/product_listings",
    "The Great Gatsby": "/product_details/classic_literature/the-great-gatsby/1",
    "To Kill a Mockingbird": "/product_details/classic_literature/to-kill-a-mockingbird/2",
    "1984": "/product_details/classic_literature/1984/3",
    "Pride and Prejudice": "/product_details/classic_literature/pride-and-prejudice/4",
    "Harry Potter and the Philosopher's Stone": "/product_details/fantasy/harry-potter-and-the-philosophers-stone/5",
    "The Catcher in the Rye": "/product_details/classic_literature/the-catcher-in-the-rye/6",
    "Animal Farm": "/product_details/classic_literature/animal-farm/7",
    "Lord of the Flies": "/product_details/classic_literature/lord-of-the-flies/8",
    "The Hobbit": "/product_details/fantasy/the-hobbit/9",
    "Brave New World": "/product_details/classic_literature/brave-new-world/10",
    "The Grapes of Wrath": "/product_details/classic_literature/the-grapes-of-wrath/11",
    "Catch-22": "/product_details/classic_literature/catch-22/12",
    "The Lord of the Rings": "/product_details/fantasy/the-lord-of-the-rings/13",
    "The Alchemist": "/product_details/fiction/the-alchemist/14",
    "Fantasy": "/tags/fantasy",
    "Dystopian": "/categories/dystopian",
    "Romance": "/tags/romance",
    "Self-Help": "/tags/self-help",
    "Bestseller": "/tags/bestseller",
    "Classic": "/tags/classic",
    "Award-Winning": "/tags/award_winning",
    "Biography": "/tags/biography",
    "Viking Press": "/publications/viking_press",
    "Alfred A. Knopf": "/publications/alfred_a_knopf",
    "Scribner": "/publications/scribner",
    "Little, Brown and Company": "/publications/little_brown_and_company",
    "Doubleday": "/publications/doubleday",
    "Vintage Books": "/publications/vintage_books",
    "Grand Central Publishing": "/publications/grand_central_publishing",
    "Gallery Books": "/publications/gallery_books",
    "Classic Literature": "/categories/classic_literature",
    "Science Fiction": "/categories/science_fiction",
    "Children's Literature": "/categories/children_literature",
    "Fiction": "/categories/fiction",
    "Contact_Us": "/pages/contact_us",
    "About_Us": "/pages/about_us",
}


def generate_clickstream_data():
    while True:
        user_id = random.randint(100, 999)
        page_title, page_url = random.choice(list(page_data.items()))
        event_type = random.choice(["click", "purchase", "add_to_cart"])
        click_data = {
            "user_id": user_id,
            "page_title": page_title,
            "page_url": page_url,
            "timestamp": datetime.now().isoformat(),
            "event_type": event_type
        }
        yield json.dumps(click_data)
        time.sleep(0.1)  # Simulating some delay between generating each clickstream event


if __name__ == "__main__":
    r = redis.Redis(host='127.0.0.1', port=6379)
    for data in generate_clickstream_data():
        r.rpush('clickstream_queue', data)
        print(data)
