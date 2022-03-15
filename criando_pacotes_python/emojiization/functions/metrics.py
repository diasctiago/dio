import emoji

def emoji_count(text):
  emoji_count = 0
  text_count = 0
  for t in text.split():
    if emoji.is_emoji(t):
      emoji_count += 1
    else:
      text_count += 1
  return (emoji_count, text_count)