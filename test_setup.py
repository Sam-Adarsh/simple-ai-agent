import os
import sys

def test_setup():
    print("Testing setup...")
    
    # Check for python-dotenv
    try:
        from dotenv import load_dotenv
        load_dotenv()
        print("✅ python-dotenv is installed and loaded.")
    except ImportError:
        print("❌ python-dotenv is NOT installed. Install it with: pip install python-dotenv")

    # Check for GROQ_API_KEY
    api_key = os.getenv("GROQ_API_KEY")
    if api_key:
        print(f"✅ GROQ_API_KEY is set: {api_key[:8]}...{api_key[-4:]}")
    else:
        print("❌ GROQ_API_KEY is NOT set. Check your .env file.")

    # Print System Info
    print("\nSystem Information:")
    print(f"Python Version: {sys.version.split()[0]}")
    print(f"Python Executable: {sys.executable}")

if __name__ == "__main__":
    test_setup()
