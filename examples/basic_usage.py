"""Basic usage example for TIRAI SDK"""

from TIRAI import AISDKConfig

def main():
    # Create an SDK instance for OpenAI
    sdk = AISDKConfig.create_sdk('gpt-4o')

    # Get a response
    try:
        response, time_taken = sdk.get_response(
            "What is artificial intelligence?",
            model="gpt-4o"
        )
        print(f"Response: {response}")
        print(f"Time taken: {time_taken:.2f}s")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
