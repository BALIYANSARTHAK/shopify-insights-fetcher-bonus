import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

def fetch_shopify_insights(base_url: str) -> dict:
    if not base_url.startswith("http"):
        raise ValueError("Invalid URL format")

    insights = {}

    try:
        # Products
        products_url = urljoin(base_url, "/products.json")
        res = requests.get(products_url, timeout=10)
        insights["product_catalog"] = res.json().get("products", []) if res.ok else []

        # Homepage
        homepage = requests.get(base_url, timeout=10)
        soup = BeautifulSoup(homepage.text, "html.parser")

        # Hero Products
        insights["hero_products"] = [tag.text.strip() for tag in soup.select(".product-title")][:5]

        # Contact Info
        insights["contact_details"] = {
            "emails": re.findall(r"[\w\.-]+@[\w\.-]+", homepage.text),
            "phones": re.findall(r"\+?\d[\d\s\-]{8,}\d", homepage.text)
        }

        # Social Handles
        insights["social_handles"] = {
            "instagram": [a["href"] for a in soup.find_all("a", href=True) if "instagram.com" in a["href"]],
            "facebook": [a["href"] for a in soup.find_all("a", href=True) if "facebook.com" in a["href"]],
            "tiktok": [a["href"] for a in soup.find_all("a", href=True) if "tiktok.com" in a["href"]]
        }

        # About
        about_page = soup.find("meta", attrs={"name": "description"})
        insights["brand_about"] = about_page["content"] if about_page else ""

        # Important Links
        insights["important_links"] = {a.text.strip(): a["href"] for a in soup.find_all("a", href=True) if any(x in a.text.lower() for x in ["blog", "track", "faq", "contact"])}

        return insights
    except Exception as e:
        raise Exception(f"Scraping error: {str(e)}")