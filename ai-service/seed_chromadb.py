import chromadb
import os

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_data")

# Create or get collection
collection = chroma_client.get_or_create_collection(
    name="notification_knowledge",
    metadata={"description": "Domain knowledge for notification engine"}
)

# 10 domain knowledge documents
documents = [
    "High CPU usage above 90% indicates server overload and requires immediate investigation of running processes.",
    "Database connection failures can be caused by network issues, incorrect credentials, or database server being down.",
    "Payment transaction failures should be logged immediately and the finance team notified for reconciliation.",
    "Memory usage above 95% can cause system crashes and services should be restarted to free memory.",
    "API response times above 2 seconds indicate performance issues that need optimization.",
    "Authentication failures with invalid tokens suggest security breach attempts and should trigger alerts.",
    "Successful database backups confirm data integrity and should be logged for compliance.",
    "Network connectivity loss affects all services and requires immediate infrastructure team notification.",
    "File upload failures can be caused by storage limits, network issues or file size restrictions.",
    "New user registrations should trigger welcome emails and account setup workflows automatically."
]

# Document IDs
ids = [f"doc_{i+1}" for i in range(len(documents))]

# Metadata for each document
metadatas = [
    {"category": "performance", "severity": "HIGH"},
    {"category": "database", "severity": "CRITICAL"},
    {"category": "payment", "severity": "CRITICAL"},
    {"category": "memory", "severity": "CRITICAL"},
    {"category": "performance", "severity": "MEDIUM"},
    {"category": "security", "severity": "HIGH"},
    {"category": "backup", "severity": "LOW"},
    {"category": "network", "severity": "CRITICAL"},
    {"category": "storage", "severity": "MEDIUM"},
    {"category": "user", "severity": "LOW"}
]

# Add documents to ChromaDB
collection.upsert(
    documents=documents,
    ids=ids,
    metadatas=metadatas
)

print("ChromaDB seeded successfully!")
print(f"Total documents: {collection.count()}")

# Test query
results = collection.query(
    query_texts=["server performance issue"],
    n_results=3
)

print("\nTest Query Results:")
for i, doc in enumerate(results['documents'][0]):
    print(f"{i+1}. {doc[:80]}...")