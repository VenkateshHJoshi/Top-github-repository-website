import pandas as pd
import streamlit as st
import random

# Predefined list of Unsplash coding-related photo URLs
unsplash_photos = [
    "https://images.unsplash.com/photo-1537498425277-c283d32ef9db",
    "https://images.unsplash.com/photo-1518770660439-4636190af475",
    "https://images.unsplash.com/photo-1519241047957-be31d7379a5d",
    "https://images.unsplash.com/photo-1498050108023-c5249f4df085",
    "https://images.unsplash.com/photo-1497493292307-31c376b6e479",
    "https://images.unsplash.com/photo-1517694712202-14dd9538aa97",
    "https://images.unsplash.com/photo-1531482615713-2afd69097998",
]

# Load the CSV file into a DataFrame
df = pd.read_csv("repository_merged_links.csv")

# Extract unique topics from the DataFrame
topics = df['Topic Name'].unique()

# Streamlit application
st.title("Find the Popular Github Repository of Your Topic")

# Dropdown for selecting a topic
selected_topic = st.selectbox("Select a Topic", [""] + list(topics))

# Custom CSS for styling and animations
st.markdown("""
    <style>
        .repo-div {
            display: flex;
            align-items: center;
            justify-content: space-between;
            border: 1px solid #ddd;
            padding: 20px;
            margin: 10px 0;
            border-radius: 5px;
            transition: transform 0.3s ease;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        }
        .repo-div:hover {
            transform: translateY(-10px);
        }
        .repo-button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .repo-button:hover {
            background-color: #45a049;
        }
        .repo-title {
            font-size: 24px;
            color: #333;
        }
        .repo-description {
            font-size: 16px;
            color: #666;
        }
        .repo-image {
            margin-left: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Display a random selection of repositories by default (up to 50)
if selected_topic == '':
    random_topics = random.sample(list(topics), min(50, len(topics)))
    for topic in random_topics:
        st.write(f"Popular repositories for the topic: {topic}")
        filtered_repos = df[df['Topic Name'] == topic]
        for index, row in filtered_repos.iterrows():
            repo_href = row['link']
            repo_name = repo_href.replace("https://github.com/", "").replace("/", " ")
            photo_url = random.choice(unsplash_photos)
            st.markdown(f"""
                <div class='repo-div'>
                    <div>
                        <h4 class='repo-title'>{repo_name}</h4>
                        <p class='repo-description'>Description for {repo_name}. This repository is related to the topic {topic}.</p>
                        <a href="{repo_href}" target="_blank" style="text-decoration: none;">
                            <button class='repo-button'>Visit Repository</button>
                        </a>
                    </div>
                    <img src="{photo_url}" alt="Coding Image" class='repo-image' width="150">
                </div>
            """, unsafe_allow_html=True)
else:
    # Filter repositories for the selected topic
    st.write(f"Popular repositories for the topic: {selected_topic}")
    filtered_repos = df[df['Topic Name'] == selected_topic]
    for index, row in filtered_repos.iterrows():
        repo_href = row['link']
        repo_name = repo_href.replace("https://github.com/", "").replace("/", " ")
        photo_url = random.choice(unsplash_photos)
        st.markdown(f"""
            <div class='repo-div'>
                <div>
                    <h4 class='repo-title'>{repo_name}</h4>
                    <p class='repo-description'>Description for {repo_name}. This repository is related to the topic {selected_topic}.</p>
                    <a href="{repo_href}" target="_blank" style="text-decoration: none;">
                        <button class='repo-button'>Visit Repository</button>
                    </a>
                </div>
                <img src="{photo_url}" alt="Coding Image" class='repo-image' width="150">
            </div>
        """, unsafe_allow_html=True)
