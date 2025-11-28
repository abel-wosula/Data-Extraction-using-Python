import pandas as pd

# Define the weekly schedule data
schedule_data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Instagram': ['Carousel: Educational tips', 'Reel: Behind-the-scenes', 'Image post: Product highlight', 'Story: Interactive poll', 'Reel: UGC/Client review', 'Story: Tips/Weekend content', 'Story: Highlights recap'],
    'Facebook': ['Blog link + tip', 'Customer testimonial', 'Product promotion', 'Engagement question/post', 'Fun/educational video', 'Light engagement post', 'Inspirational quote/story'],
    'LinkedIn': ['Article summary + insight', 'Industry trend highlight', 'Case study summary', 'Thought leadership post', 'Employee spotlight', 'N/A', 'N/A'],
    'TikTok': ['Short tutorial video', 'Fun/relatable short video', 'Tutorial or “Did you know?” clip', 'Trend/challenge video', 'Trend-based content', 'Short creative video', 'N/A'],
    'Twitter/X': ['Quick tip + relevant hashtag', 'Poll/question to audience', 'Thread on industry news', 'Retweet + comment on industry news', 'Weekly roundup/summary', 'Weekend engagement tweet', 'N/A']
}

# Create a DataFrame
schedule_df = pd.DataFrame(schedule_data)

# Save as Excel file
file_path = 'A:\Projects\pdf_extract\Social_Media_Posting_Schedule.xlsx'
schedule_df.to_excel(file_path, index=False)
file_path
