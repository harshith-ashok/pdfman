from langchain_text_splitters import RecursiveCharacterTextSplitter

CHUNK_SIZE = 6000
CHUNK_OVERLAP = 400


def chunk_text(text: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_text(text)

    return chunks
