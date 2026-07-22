"""
AI Chat Assistant — CLI Entry Point

Run: python main.py
"""
from assistant.llm_client import LLMClient
from assistant.memory import Memory
from assistant.knowledge_base import KnowledgeBase

SYSTEM_PROMPT = """You are a helpful, friendly AI assistant running in a terminal.
Keep answers clear and reasonably concise unless the user asks for detail.
If relevant context from the user's knowledge base is provided below a message,
use it to give a more accurate, grounded answer. If it isn't relevant, ignore it."""

HELP_TEXT = """
Available commands:
  /help    - Show this help message
  /reset   - Clear current conversation memory
  /save    - Save current conversation to a JSON file
  /load    - Load the most recently saved conversation
  /docs    - List documents currently in the knowledge base
  /exit    - Quit the assistant
"""


def main():
    print("🤖 AI Chat Assistant — type /help for commands, /exit to quit.\n")

    try:
        llm = LLMClient()
    except ValueError as e:
        print(f"⚠️  Configuration error: {e}")
        return

    memory = Memory()
    kb = KnowledgeBase()

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Bye!")
            break

        if not user_input:
            continue

        # --- Command handling ---
        if user_input == "/exit":
            print("👋 Bye!")
            break
        elif user_input == "/help":
            print(HELP_TEXT)
            continue
        elif user_input == "/reset":
            memory.reset()
            print("🔄 Conversation history clear ho gayi.\n")
            continue
        elif user_input == "/save":
            path = memory.save()
            print(f"✅ Conversation saved as {path}\n")
            continue
        elif user_input == "/load":
            path = memory.load_latest()
            if path:
                print(f"📂 Loaded conversation from {path}\n")
            else:
                print("⚠️  Koi saved conversation nahi mili.\n")
            continue
        elif user_input == "/docs":
            docs = kb.list_documents()
            if docs:
                print(f"📚 Knowledge base me {len(docs)} documents hain: {', '.join(docs)}\n")
            else:
                print("📚 Knowledge base khaali hai. data/knowledge/ me .txt files daalo.\n")
            continue

        # --- Normal chat turn ---
        context = kb.search(user_input)
        message_content = user_input
        if context:
            message_content = (
                f"{user_input}\n\n"
                f"--- Relevant context from knowledge base ---\n{context}"
            )

        memory.add("user", message_content)

        try:
            reply = llm.get_response(memory.get_messages(), SYSTEM_PROMPT)
        except Exception as e:
            print(f"⚠️  Error calling LLM API: {e}\n")
            memory.history.pop()  # remove the failed user turn
            continue

        memory.add("assistant", reply)
        print(f"Assistant: {reply}\n")


if __name__ == "__main__":
    main()
