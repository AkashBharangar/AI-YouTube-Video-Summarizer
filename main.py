from transcribe import get_transcript
from llm import summarize_video


def main():
    """
    Main entry point of the application.
    """

    youtube_url = input("Enter YouTube URL: ")

    print("\nFetching transcript...\n")
    transcript = get_transcript(youtube_url)

    print("Generating summary...\n")
    result = summarize_video(transcript)

    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(result.summary)

    print("\n")

    print("=" * 60)
    print("KEY INSIGHTS")
    print("=" * 60)

    for insight in result.key_insights:
        print(f"• {insight}")

    print("\n")

    print("=" * 60)
    print("ACTION ITEMS")
    print("=" * 60)

    for item in result.action_items:
        print(f"✓ {item}")


if __name__ == "__main__":
    main()