# Capstone-project
ISS STOXX Capstone Project
# NL2Esgish2 README
Convert ISS Stoxx formal query language: ESGish2 to natural language and vice versa.

## Description
 NL2Esgish2 is a NLP-based tool which converts human-readable text input into the query language Esgish2, with the intent of streamlining non-technical user's interactions with the ISS Stoxx database.

## Features
The scope of this project is an API program capable of conversion to and from Esgish2. This means there are two main functions that will be syncretically developed.
1. Esgish2 -> Natural Language conversion.
This is the initial focus of the project due to its lack of reliance on a pre-generated set of data. Due to the formatting of Esgish2, this conversion does not rely on vast quantiles of data being utilized to train a model. In a perfect world we would utilize a model regardless, however our coordinator at ISS Stoxx has only provided us with a datasheet containing queries in Esgish2 without associated natural language.
This means it will be far simpler if we first implement a simple parser for Esgish2 -> NL as opposed to trying to force a model when we have no relevant data.
2. Natural Language -> Esgish2
Once the Esgish2 -> NL converter has been developed, we can now utilize it in tandem with the data given to us regarding well formatted Esgish2 queries. From here we are now armed with usable data for modelling.
Our goal now is to train a NLP model that can consistently and efficiently convert natural language to well-formatted Esgish2 queries.

## Technologies and Tools
Our current plan revolves around investigating and utilizing a variety of different Python libraries:
* NLTK 
* spaCy
* Transformers
After investigation, choosing the library we believe suits our problem best and investing in learning and understanding it given our goals

## Plan
*  Work to better understand Esgish2 as a query language
*  Begin developing Esgish2 -> NL tool
*  Ensure Esgish2 -> NL tool works sufficiently
*  Utilize the Esgish2 -> NL tool on the dataset we have been given to create the training set.
*  Split the dataset and begin creating the model for the NL -> Esgish2 tool
* Train the model to a high success rate
* Request more data if needed 
* Implement a short demo/dipslay if extra time

