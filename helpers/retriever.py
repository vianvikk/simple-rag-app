
def retrieve_docs(question, vector_store, similar_docs_count, see_content: bool = False):

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": similar_docs_count}
    )

    retrieved_docs = retriever.invoke(question)

    if see_content:
        print("\n========== RETRIEVED DOCUMENTS ==========")

        for i, doc in enumerate(retrieved_docs, start=1):
            print(f"\nDocument Chunk {i}")
            print("Source:", doc.metadata.get("source", "Unknown"))
            print("Content:", doc.page_content)
            print("-----------------------------------------")

    return retriever
