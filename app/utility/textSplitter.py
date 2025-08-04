from langchain.text_splitter import RecursiveCharacterTextSplitter

def text_splitter(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,      # max size of each chunk
        chunk_overlap=50    # how much to overlap between chunks
    )
    chunks = text_splitter.split_text(text)
    return chunks