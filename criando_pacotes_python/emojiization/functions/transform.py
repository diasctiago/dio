import emoji

def emoji_transform(text):
  text_new = []
  for t in text.split():
    if emoji.is_emoji(t):
      for e in emoji.demojize(t, language='pt').replace(':','').split('_'):
        text_new.append(e)
    else:
      text_new.append(t)
  return ' '.join(map(str, text_new))

  def emoji_replace(text, new_text):
  text_new = []
  for t in text.split():
    if emoji.is_emoji(t):
      text_new.append(new_text)
    else:
      text_new.append(t)
  return ' '.join(map(str, text_new))