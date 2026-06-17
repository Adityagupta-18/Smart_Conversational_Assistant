# Smart Conversational Assistant

## Overview

Smart Conversational Assistant is a Python-based AI chatbot that combines conversational memory with real-time web search capabilities. The application uses the Groq API for natural language interactions and Tavily Search for retrieving up-to-date information from the web.

The chatbot maintains conversation history throughout the session, enabling context-aware responses and more natural interactions. For queries requiring current information, such as weather updates, cryptocurrency prices, news, or other real-time topics, the system automatically retrieves relevant information from the web before generating a response.

---

## Features

### Conversational Memory

* Maintains conversation history during the active session.
* Uses previous user messages and assistant responses to provide context-aware answers.
* Supports follow-up questions based on earlier interactions.

### Real-Time Information Retrieval

* Detects queries that require current or up-to-date information.
* Retrieves relevant web results using Tavily Search.
* Generates responses based on the latest available information.

### Intelligent Query Routing

* Automatically determines whether a query requires web search.
* Uses direct AI responses for general knowledge questions.
* Uses web-enhanced responses for real-time information requests.

### Conversation History

* Displays complete conversation history before exiting the application.
* Preserves user and assistant message flow for easy review.

### Interactive Command-Line Interface

* Continuous chat session using a simple terminal interface.
* Supports graceful program termination with conversation review.

---

## Technologies Used

* Python 3.11
* Groq API
* Tavily Search API
* Virtual Environment (venv)

---

## Project Architecture

User Query
│
├── Query Classification
│   ├── Real-Time Query → Tavily Search → Groq Response
│   └── General Query → Groq Response
│
└── Conversation History Management

---

## Example Workflow

### General Query

User:

```text
What is Object-Oriented Programming?
```

Process:

```text
User Query → Groq → Response
```

### Real-Time Query

User:

```text
Today's Gold Price
```

Process:

```text
User Query
    ↓
Query Classification
    ↓
Tavily Search
    ↓
Search Results
    ↓
Groq
    ↓
Final Response
```

---

## Project Structure

```text
Smart-Conversational-Assistant/
│
├── main.py
├── requirements.txt
├── README.md
└── .venv/
```

---

## Future Enhancements

* Persistent conversation memory using JSON storage.
* Voice input integration.
* Text-to-speech responses.
* Graphical User Interface (GUI).
* Multi-session conversation management.
* User authentication and profiles.

---

## Learning Outcomes

This project demonstrates:

* API Integration
* Prompt Engineering
* Conversational Memory Management
* Real-Time Information Retrieval
* Python Application Development
* Context-Aware AI Systems
