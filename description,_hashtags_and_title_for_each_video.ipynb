{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ehV2j58eJyiW"
      },
      "outputs": [],
      "source": [
        "if __name__ == '__main__':\n",
        "    main()\n",
        "import pandas as pd\n",
        "import requests\n",
        "\n",
        "# YouTube API key\n",
        "API_KEY = 'xxxxxxxxxxxxxxxxxxxxx'\n",
        "\n",
        "# Load the CSV file\n",
        "df = pd.read_csv('.csv')\n",
        "\n",
        "# Function to extract YouTube video ID from URL\n",
        "def extract_video_id(url):\n",
        "    if \"v=\" in url:\n",
        "        return url.split(\"v=\")[1].split(\"&\")[0]\n",
        "    return None\n",
        "\n",
        "# Function to get video details from YouTube Data API\n",
        "def get_video_details(video_id):\n",
        "    url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={API_KEY}'\n",
        "    response = requests.get(url)\n",
        "    if response.status_code == 200:\n",
        "        data = response.json()\n",
        "        if 'items' in data and len(data['items']) > 0:\n",
        "            video_info = data['items'][0]['snippet']\n",
        "            title = video_info.get('title', '')\n",
        "            description = video_info.get('description', '')\n",
        "            tags = video_info.get('tags', [])\n",
        "            return title, description, tags\n",
        "    return None, None, None\n",
        "\n",
        "# Initialize new columns for the details\n",
        "df['Title'] = ''\n",
        "df['Description'] = ''\n",
        "df['Tags'] = ''\n",
        "\n",
        "# Loop through each row, extract video details, and update the dataframe\n",
        "for index, row in df.iterrows():\n",
        "    video_id = extract_video_id(row['AdLink'])  # Assuming 'AdLink' is the column name\n",
        "    if video_id:\n",
        "        title, description, tags = get_video_details(video_id)\n",
        "        df.at[index, 'Title'] = title\n",
        "        df.at[index, 'Description'] = description\n",
        "        df.at[index, 'Tags'] = ', '.join(tags) if tags else ''\n",
        "\n",
        "# Save the updated CSV\n",
        "df.to_csv('updated_csv_file.csv', index=False)\n",
        "\n",
        "print(\"CSV file updated with YouTube video details.\")\n"
      ]
    }
  ]
}
