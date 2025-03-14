from flask import Flask, request, render_template_string
from apify_client import ApifyClient
import pandas as pd

app = Flask(__name__)

# Initialize the ApifyClient with your API token
API_TOKEN = "apify_api_tnYD8c8vY9WRRJG9IG822DfWQGNJRc00SUky"
client = ApifyClient(API_TOKEN)

# Route to render the HTML form
@app.route("/")
def index():
    # Render the HTML file
    return render_template_string(open("templates/index.html").read())

# Route to handle form submission and scrape events
@app.route("/scrape", methods=["POST"])
def scrape_events():
    keyword = request.form.get("keyword")
    city = request.form.get("city")
    state = request.form.get("state")
    country = request.form.get("country")

    try:
        # Prepare the input for the Apify actor
        run_input = {
            "searchKeyword": keyword.strip(),
            "city": city.strip(),
            "state": state.strip(),
            "country": country.strip(),
            "maxResults": 20,
            "scrapeEventName": True,
            "scrapeEventDescription": True,
            "scrapeEventType": True,
            "scrapeEventDate": True,
            "scrapeEventAddress": True,
            "scrapeEventUrl": True,
            "scrapeHostedByGroup": True,
            "scrapeMaxAttendees": True,
            "scrapeActualAttendeesCount": True,
        }

        # Run the actor
        run = client.actor("oHaGcsfmmm2nxYdjA").call(run_input=run_input)

        # Fetch results from the dataset
        results = list(client.dataset(run["defaultDatasetId"]).iterate_items())

        # Convert results to a Pandas DataFrame and render as HTML
        if results:
            df = pd.DataFrame(results)
            return df.to_html(index=False, classes="styled-table")

        else:
            return "<h2>No events found for the specified location.</h2>"

    except Exception as e:
        return f"<h2>An error occurred: {e}</h2>"

if __name__ == "__main__":
    app.run(debug=True)
