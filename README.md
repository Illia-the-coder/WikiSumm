# WikiSumm
A simple Flask app that retrieves information from Wikipedia. Users can enter a query and select a language. The app returns a summary of the relevant Wikipedia page, limited to 5 sentences, and a list of related pages. In case of disambiguation, options are presented. Error messages are displayed for any errors.
# WikiFinder

A web application that helps users find information about their desired topics using the power of Wikipedia. The app allows the user to search for any topic and it returns a summary of the information available on that topic along with a list of related pages on Wikipedia. 

## Technologies Used

The project was built using:
- Flask: a micro web framework written in Python
- Wikipedia-API: a python wrapper for the Wikipedia's API
- HTML, CSS, and JavaScript for the front-end design.

## Features

- User-friendly interface
- Search for any topic
- Return a summary of information about the topic
- List of related pages on Wikipedia
- Multiple language support

## Deployment

The application can be deployed using `waitress` by running the following command:

from waitress import serve
serve(app, host="0.0.0.0", port=8080)


The application can be accessed through the browser at `http://0.0.0.0:8080`.

## Conclusion

WikiFinder is a useful tool for anyone who needs quick and reliable information about a particular topic. It helps save time and effort by presenting a summarized version of the information available on Wikipedia along with related pages for further reading.