## Flask Application Design

### HTML Files

**index.html:**
- The main page of the application.
- Contains the interface for the user to enter the URL of the page they want to scrape.
- Includes a button to trigger the scraping process.

### Routes

**`/`**:
- GET: Renders the `index.html` file, displaying the scraping interface.
- POST: Receives the URL from the form and initiates the scraping process.

**`/scrape`**:
- GET: Scrapes the specified URL and returns the extracted data in JSON format.

**`/result`**:
- GET: Displays the scraped data in a user-friendly format on a new page.

**Additional Notes:**

- The HTML files can be further customized to include additional features or styling as per the specific requirements of the use case.
- Additional routes can be added to handle specific tasks or provide different functionalities as needed.