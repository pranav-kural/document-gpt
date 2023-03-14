# Document GPT

A [LlamaIndex]("https://gpt-index.readthedocs.io/en/latest/index.html") powered app to utilize Open AI API's for obtaining responses to queries related to a docoment or a set of documents.

LlamaIndex converts the document's data into a vectorized index and then uses this index to provide context to the GPT model when user makes a query. It further optimizes by finding the most relevant parts of the indexed document to be provided as context, thereby reducing the amount of data that needs to be sent to the GPT model and thus reducing the number of tokens and cost.

## Usage

1. Create a `.env` file in the root directory of the project and add the following variables:

```bash
OPENAI_API_KEY=<your_openai_api_key>
```

2. Edit the program parameters in `parameters.py` file to make any changes to the default parameters and specify:

   1. Directory containing the documents to be indexed
   2. Name of index file to be created or loaded
   3. Queries to be made to the GPT model

3. Run the `document-gpt.py` file to start the program.

```bash
python document-gpt.py
```

## References

Inspired from [A guide to building a chatbot based on your own documents with GPT]("https://bootcamp.uxdesign.cc/a-step-by-step-guide-to-building-a-chatbot-based-on-your-own-documents-with-gpt-2d550534eea5")
