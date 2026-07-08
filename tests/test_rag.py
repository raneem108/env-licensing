from ai.rag import process_document, search_documents 

# Test with your regulation document
pdf_path = "data/regulations/نظام_التصنيف_و_التراخيص_رقم_69_باللغة_الانجليزية.pdf"

print("Processing document...")
vectorstore = process_document(pdf_path)
print("Done!")

# Test search
query = "What category is a dairy factory?"
results = search_documents(query, vectorstore)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)