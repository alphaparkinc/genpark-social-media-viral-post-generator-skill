from client import SocialPostGeneratorClient

def main():
    client = SocialPostGeneratorClient()
    res = client.generate_post(topic='AI Agents')
    print(f"Result for post_text: {res['post_text']}")

if __name__ == "__main__":
    main()
